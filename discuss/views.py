from django.urls import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from discuss.models import Topic, Discuss
from users.models import Message
from discuss.forms import TopicForm, DiscussForm

import re

@login_required
def check_topic_user(request, topic):
    if request.user != topic.topic_owner:
        raise Http404

@login_required
def topics(request, page = 0):
    topics = Topic.objects.order_by('date_added')[10*page : 10*page+10]
    context = { 'topics' : topics }
    return render(request, 'discuss/topics.html', context)

@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    discuss_list = Discuss.objects.filter(topic = topic)
    form = DiscussForm()
    context = {'topic' : topic, 'discuss_list' : discuss_list, 'form': form}
    return render(request, 'discuss/topic.html', context)

@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.topic_owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('discuss:topics'))
    
    context = { 'form': form }
    return render(request, 'discuss/new_topic.html', context)

@login_required
def edit_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    check_topic_user(request, topic)
    if request.method != 'POST':
        form = TopicForm(instance=topic)
    else:
        form = TopicForm(instance=topic, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('discuss:topic', args=[topic_id]))
    context = {
        'topic' : topic,
        'form': form
    }
    return render(request, 'discuss/edit_topic.html', context)

@login_required
def del_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    check_topic_user(request, topic)
    topic.delete()
    return HttpResponseRedirect(reverse('discuss:topics'))
    

@login_required
def new_discuss(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    if request.method != 'POST':
        form = DiscussForm()
    else:
        form = DiscussForm(request.POST)
        if form.is_valid():
            new_discuss = form.save(commit=False)
            new_discuss.topic = topic
            new_discuss.discuss_owner = request.user
            new_discuss.save()
            mention(request, new_discuss.mention, topic.name)
            return HttpResponseRedirect(reverse('discuss:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'discuss/topic.html', context)

@login_required
def mention(request, mention_list, topic_name):
    user_list = re.split('\W+', mention_list)
    for user in user_list:
        try:
            receiver_user = User.objects.get(username=user)
        except ObjectDoesNotExist:
            pass
        else:
            content = str(request.user) + " mention you in topic: " + topic_name
            Message.objects.create(sender=request.user.username, receiver=receiver_user, text=content, is_Read=False)

@login_required
def del_discuss(request, topic_id, dis_id):
    discuss = Discuss.objects.get(id=dis_id)
    discuss.delete()
    return HttpResponseRedirect(reverse('discuss:topic', args=[topic_id]))