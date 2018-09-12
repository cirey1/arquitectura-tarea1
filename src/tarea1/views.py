from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CommentForm
from .models import Comment
# Create your views here.

def home_view(request, *args, **kwargs):
    context = {}
    return render(request, 'home.html', context)

def comment_create_view(request):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        new_comment = Comment(text=form.cleaned_data['text'], client_ip=ip)
        new_comment.save()
        return  HttpResponseRedirect('/')
    else:
        context = {'form':form}
        return render(request, "comment_create.html", context)



def comment_view(request, *args, **kwargs):
    context = {'lista': Comment.objects.order_by('-comment_date')}

    return render(request, 'comments.html', context)
