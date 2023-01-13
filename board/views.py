from django.shortcuts import render, redirect
from django import views
from board.models import Topic, Post

def board(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        user = request.user
        topic = Topic(name=name, description=description, user=user)
        topic.save()
        return redirect('board:board')
    topics = Topic.objects.filter(is_valid=True)
    for topic in topics:
        topic.count_post = Post.objects.filter(topic=topic, is_valid=True).count()
        topic.last_post = Post.objects.filter(topic=topic, is_valid=True).order_by('-created_at').first()

    context = {
        'topics': topics
    }
    return render(request, 'board/index.html', context)

def topic(request, slug):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        topic = Topic.objects.get(slug=slug)
        user = request.user
        post = Post(content=content, topic=topic, user=user, title=title)
        post.save()
        return redirect('board:topic', slug=slug)

    topic = Topic.objects.get(slug=slug, is_valid=True)
    posts = Post.objects.filter(topic=topic, is_valid=True)

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

def delete_topic(request, id):
    topic = Topic.objects.get(id=id)
    topic.delete()
    return redirect('board:board')