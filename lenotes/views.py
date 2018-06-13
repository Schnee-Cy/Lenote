from django.urls import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from lenotes.models import Group, Diary, Invitation
from users.models import UserInfo, Message
from lenotes.forms import GroupForm, DiaryForm, InvitationForm
from users.views import update_userInfo_unread_count
 
def index(request):
    if request.user.is_authenticated:
        update_userInfo_unread_count(request.user)
    return render(request, 'lenotes/new_index.html')

def about_us(request):
    return render(request, 'lenotes/about_us.html')

@login_required
def groups(request):
    """用户的群组主页"""
    groups = Group.objects.filter(owner=request.user).order_by('date_added')
    context = {'groups': groups}
    return render(request, 'lenotes/groups.html', context)

@login_required
def group(request, group_id):
    """群组主页"""
    group = Group.objects.get(id=group_id)
    diarys = group.diary_set.order_by('-date_added')
    context = {'group': group, 'diarys': diarys}
    return render(request, 'lenotes/group.html', context)
    # diary_id = diarys[0].id
    # return HttpResponseRedirect(reverse('lenotes:group_diary', args=[group_id,diary_id]))

@login_required
def group_diary(request, group_id, diary_id):
    """分日记"""
    group = Group.objects.get(id=group_id)
    diarys = group.diary_set.order_by('-date_added')
    tarDiary = Diary.objects.get(id = diary_id)
    idx = 0
    for d in diarys:
        if d==tarDiary:
            break;
        idx += 1
    size = len(diarys)
    pastid = []
    showdate = []
    num = 0
    offset = -3
    while num<5:
        offset += 1
        nowidx = idx + offset
        if nowidx>=0 and nowidx<size:
            pastid.append(diarys[nowidx].id)
            showdate.append(diarys[nowidx].date_added)
            num += 1
        elif nowidx>=size:
            break
        
    for i in range(len(pastid),5):
        pastid.append(diarys[0].id)
        showdate.append(' ')
    context = {'group': group, 'diarys': diarys,
    'pastid' : pastid,
    'showdate' : showdate
    }
    return render(request, 'lenotes/group_diary.html', context)

@login_required
def manage(request, group_id):
    """修改群组资料，邀请功能，管理用户"""
    if request.method != 'POST':
        try:
            group = Group.objects.get(id=group_id)
        except ObjectDoesNotExist:
            group = Group.objects.create(id=group_id)
        group_form = GroupForm(instance = group)
    else:
        group_form = GroupForm(request.POST, request.FILES)
        if group_form.is_valid():
            try:
                group = Group.objects.get(id=group_id)
            except ObjectDoesNotExist:
                group = Group.objects.create(id=group_id)
        group.name = group_form.cleaned_data["name"]
        group.intro = group_form.cleaned_data["intro"]
        group.profile = group_form.cleaned_data["profile"]
        group.save()
        return HttpResponseRedirect(reverse('lenotes:group', args=[group.id]))
    members = group.members.all()
    memberInfos = []
    for member in members:
        info = UserInfo.objects.get(user=member)
        memberInfos.append(info)
    context = {
        'group': group,
        'memberInfos': memberInfos,
        'group_form': group_form,
    }
    return render(request, 'lenotes/manage.html' , context)

@login_required
def del_member(request, group_id, info_id):
    group = Group.objects.get(id=group_id)
    info = UserInfo.objects.get(id=info_id)
    group.members.remove(info.user)
    msg = "You have been removed from group: " + group.name
    Message.objects.create(sender = group.owner.username + "(Group Owner)", text=msg, receiver=info.user)
    return HttpResponseRedirect(reverse('lenotes:manage', args=[group_id]))

@login_required
def send_invite(request, group_id):
    if request.method == 'POST':
        try:
            invite_user = User.objects.get(username=request.POST['invite_id'])
        except ObjectDoesNotExist:
            context = {'group_id': group_id}
            return render(request, 'lenotes/userIsNotExist.html' , context)
        group = Group.objects.get(id = group_id)
        msg = request.user.username + " invite you to join Group: " + group.name 
        Invitation.objects.create(receiver=invite_user, message=msg, groupid=group_id, is_Read=False)
        return HttpResponseRedirect(reverse('lenotes:manage', args=[group_id]))
    context = { 'group_id': group_id }
    return render(request, 'lenotes/send_invite.html', context)

@login_required
def new_group(request):
    if request.method != 'POST':
        form = GroupForm()
    else:
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            new_group = form.save(commit=False)
            new_group.owner = request.user
            new_group.save()
            new_group.members.add(request.user)
            new_group.save()
            return HttpResponseRedirect(reverse('users:home'))
    
    context = {'form': form}
    return render(request, 'lenotes/new_group.html', context)

@login_required
def del_group(request, group_id):
    """删除当前群组"""
    del_group = Group.objects.get(id=group_id)
    members = del_group.members.all()
    senderName = del_group.owner.username + "(Group Owner)"
    for member in members:
        msg = "The group: " + del_group.name + " have been deleted."
        Message.objects.create(sender=senderName, text=msg, receiver=member)
    del_group.delete()
    return HttpResponseRedirect(reverse('users:home'))

@login_required
def new_diary(request, group_id):
    group = Group.objects.get(id = group_id)
    if request.method != 'POST':
        form = DiaryForm()
    else:
        form = DiaryForm(data = request.POST)
        if form.is_valid():
            new_diary = form.save(commit=False)
            new_diary.group = group
            new_diary.save()
            return HttpResponseRedirect(reverse('lenotes:group', args=[group_id]))
    context = {'group': group, 'form': form}
    return render(request, 'lenotes/new_diary.html', context)

@login_required
def edit_diary(request, diary_id):
    """编辑既有条目"""
    diary = Diary.objects.get(id=diary_id)
    group = diary.group
    if request.method != 'POST':
        form = DiaryForm(instance=diary)
    else:
        form = DiaryForm(instance=diary, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lenotes:group', args=[group.id]))
    context = {'diary': diary, 'group': group, 'form': form}
    return render(request, 'lenotes/edit_diary.html', context)

@login_required
def del_diary(request, diary_id):
    """删除当前群组"""
    del_diary = Diary.objects.get(id=diary_id)
    group_id = del_diary.group.id
    del_diary.delete()
    return HttpResponseRedirect(reverse('lenotes:group', args=[group_id]))


@login_required
def add_diary(request,group_id):
    get_group = Group.objects.get(id=group_id)
    Diary.objects.all().create(group = get_group)
    return HttpResponseRedirect(reverse('lenotes:group', args=[group_id]))