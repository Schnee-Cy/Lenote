from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from users.models import UserInfo, Message
from lenotes.models import Group, Invitation
from users.forms import InfoForm, MsgForm #, ProfileForm

def update_userInfo_unread_count(user):
    userinfo = UserInfo.objects.get(user=user) 
    userinfo.unread_count = Message.objects.filter(receiver=user, is_Read=False).count() +\
        Invitation.objects.filter(receiver=user, is_Read=False).count()
    userinfo.save()

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('lenotes:index'))
    if request.method != 'POST':
        form = AuthenticationForm(request)
    else:
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return HttpResponseRedirect(reverse('lenotes:index'))
    context = {'form': form}
    return render(request, 'users/login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('lenotes:index'))

def register(request):
    if request.method != 'POST':
        user_form = UserCreationForm()
        info_form = InfoForm()
    else:
        print(request.POST)
        user_form = UserCreationForm(data=request.POST)
        info_form = InfoForm(request.POST, request.FILES)
        if user_form.is_valid():
            new_user = user_form.save()
            new_info = info_form.save(commit=False)
            new_info.user = new_user
            new_info.save()
            authenticated_user = authenticate(username = new_user.username,
            password = request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('lenotes:index'))
    
    context = {
        'user_form': user_form,
        'info_form': info_form,    
    }
    return render(request, 'users/register.html' , context)

@login_required
def home(request):
    """显示个人信息的主界面"""
    try:
        userinfo = UserInfo.objects.get(user=request.user) 
    except ObjectDoesNotExist:
        userinfo = UserInfo.objects.create(user=request.user)
    if userinfo.name.strip() == "":
        userinfo.name = "Undefined"
    if userinfo.gender.strip() == "M":
        userinfo.gender = "Male"
    else:
        userinfo.gender = "Female"
    if userinfo.email.strip() == "":
        userinfo.email = "Undefined@example.com"
    if userinfo.intro.strip() == "":
        userinfo.intro = "No introduce"
    update_userInfo_unread_count(request.user)
    groups = Group.objects.filter(members__id = request.user.id).order_by('date_added')
    context = {
        'userinfo': userinfo,
        'groups' : groups,
    }
    return render(request, 'users/home.html', context)

@login_required
def settings(request):
    if request.method != 'POST':
        try:
            info = UserInfo.objects.get(user = request.user)
        except ObjectDoesNotExist:
            info = UserInfo.objects.create(user = request.user)
        info_form = InfoForm(instance = info)
        context = {
        'info_form': info_form,
        }
        return render(request, 'users/settings.html' , context)
    else:
        info_form = InfoForm(request.POST)
        if info_form.is_valid():
            try:
                info = UserInfo.objects.get(user = request.user)
            except ObjectDoesNotExist:
                info = UserInfo.objects.create(user = request.user)
        info.name = info_form.cleaned_data["name"]
        info.gender = info_form.cleaned_data["gender"]
        info.email = info_form.cleaned_data["email"]
        info.intro = info_form.cleaned_data["intro"]
        myprofile = request.FILES.get('profile',None)
        if myprofile:
            info.profile.delete()
            info.profile = myprofile
        info.save()
        return HttpResponseRedirect(reverse('users:home'))
    

@login_required
def reset_password(request):
    if request.method != 'POST':
        form = PasswordChangeForm(user = request.user)
    else:
        form = PasswordChangeForm(user = request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect(reverse('users:reset_done'))
    context = {
        'form': form, 
    }
    return render(request, 'users/reset_password.html', context)

def reset_done(request):
    return render(request, 'users/reset_done.html')

@login_required
def notice(request):
    """用于接收留言以及通知"""
    update_userInfo_unread_count(request.user)
    messages = Message.objects.filter(receiver = request.user).order_by('-date_added')
    invitations = Invitation.objects.filter(receiver=request.user).order_by('-date_added')
    context = {
        'messages': messages,
        'invitations': invitations
    }
    return render(request, 'users/notice.html', context)

@login_required
def send_message(request):
    """向某人发送信息"""
    if request.method != 'POST':
        form = MsgForm()
    else:
        form = MsgForm(request.POST)
        if form.is_valid():
            new_Message = form.save(commit=False)
            new_Message.sender = request.user.username
            new_Message.save()
            return HttpResponseRedirect(reverse('users:home'))
    context = {'form': form}
    return render(request, 'users/send_message.html', context)

@login_required
def read_message(request, message_id):
    """标记消息为已读"""
    try:
        message = Message.objects.get(id=message_id)
        message.is_Read = True;
        message.save()
    finally:
        return HttpResponseRedirect(reverse('users:notice'))

@login_required
def del_message(request, message_id):
    """删除当前消息"""
    try:
        del_message = Message.objects.get(id=message_id)
        del_message.delete()
    finally:
        return HttpResponseRedirect(reverse('users:notice'))

@login_required
def deal_invi(request, invi_id, accept):
    """处理邀请"""
    try:
        invitation = Invitation.objects.get(id=invi_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('users:notice')) 
    invitation.is_Read = True
    invitation.save()
    if accept:
        group = Group.objects.get(id=invitation.groupid)
        group.members.add(invitation.receiver)
        msg = request.user.username + " accpeted to join in group:" + group.name
    else:
        msg = request.user.username + " refused to join in group:" + group.name
    Message.objects.create(sender=request.user.username, text=msg, receiver=group.owner)
    return HttpResponseRedirect(reverse('users:notice'))

@login_required
def quit_group(request, group_id):
    """退出当前群聊"""
    try:
        group = Group.objects.get(id=group_id)
        group.members.remove(request.user)
        msg = request.user.username + " quit the group: " + group.name
        Message.objects.create(sender=request.user.username + "(Group Member)", text=msg, receiver=group.owner)
    finally:
        return HttpResponseRedirect(reverse('users:home'))

@login_required
def del_invi(request, invi_id):
    """删除当前通知"""
    try:
        del_invitation = Invitation.objects.get(id=invi_id)
        del_invitation.delete()
    finally:
        return HttpResponseRedirect(reverse('users:notice'))
