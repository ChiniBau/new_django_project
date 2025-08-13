from django.shortcuts import render
from django.http import JsonResponse
from .models import BlogPost
from django.core.serializers import serialize
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, 'tasks/post_list.html') 

# Create your views here.
def get_posts(request):
    posts = BlogPost.objects.all().order_by('-published')
    data = [
        {
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'published': post.published.strftime('%Y-%m-%d %H:%M:%S'),
        } for post in posts
    ]
    return JsonResponse(data, safe=False)

@csrf_exempt
def update_or_delete_post(request, pk):
    post=get_object_or_404(BlogPost, pk=pk)

    if request.method == 'PUT':
        data = json.loads(request.body)
        post.title = data.get('title', post.title)
        post.content = data.get('content', post.content)
        post.save()
        return JsonResponse({'message': 'Post updated successfully'})
    
    elif request.method == 'DELETE':
        post.delete()
        return JsonResponse({'message': 'Post deleted successfully'})         

    return JsonResponse({'error': 'Method not allowed'}, status=405)      

