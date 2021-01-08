from django.shortcuts import render
from django.views.generic import ListView,DetailView
from blog.models import post

from django.http import JsonResponse

# Create your views here.
class postlist(ListView):
    model=post

class postdetail(DetailView):
    model=post

def likeview(request):
    if request.method == "GET":
        i=request.GET.get('i',None)
        p=post.objects.get(id=1)
        p.likes=p.likes+1
        p.save()
        data={'i':p.likes}
    return JsonResponse(data)
