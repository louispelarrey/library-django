from django.shortcuts import render, redirect
from django import views
from board.models import Topic, Post

def board(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        topic = Topic(name=name, description=description)
        topic.save()
        return redirect('board:board')

    topics = Topic.objects.all()
    context = {
        'topics': topics
    }
    return render(request, 'board/index.html', context)

def topic(request, id):
    if request.method == 'POST':
        content = request.POST['content']
        topic = Topic.objects.get(id=id)
        post = Post(content=content, topic=topic)
        post.save()
        return redirect('board:topic', id=id)

    topic = Topic.objects.get(id=id)
    posts = Post.objects.filter(topic=topic)
    context = {
        'topic': topic,
        'posts': posts
    }
    return render(request, 'topic/index.html', context)
    
def delete_topic(request, id):
    topic = Topic.objects.get(id=id)
    topic.delete()
    return redirect('board:board')

def delete_post(request, topic_id, message_id):
    post = Post.objects.get(id=message_id)
    post.delete()
    return redirect('board:topic', id=topic_id)