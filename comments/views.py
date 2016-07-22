#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, Http404, render
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.models import Permission, User
from django.utils import timezone
from django.views import generic

from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic.base import View

from .models import Comment

#def index (request):
#    latest_comment_list = Comment.objects.order_by('-pub_date')
#    context = {'latest_comment_list': latest_comment_list}
#    return render(request, 'comments/index.html', context)

class IndexView(generic.ListView):
    template_name = 'comments/index.html'
    context_object_name = 'latest_comment_list'

    def get_queryset(self):
        return Comment.objects.order_by('-pub_date')

########## OLD
#    latest_comment_list = Comment.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('comments/index.html')
#    context = RequestContext(request, {
#        'latest_comment_list': latest_comment_list,
#    })
#    return HttpResponse(template.render(context))

#    latest_comment_list = Comment.objects.order_by('-pub_date')[:5]
#    output = ', '.join([q.comment_text for q in latest_comment_list])
#   return HttpResponse(output)
##########

#def detail (request, comment_id):
#    comment = get_object_or_404(Comment, pk = comment_id)
#    return render(request, 'comments/detail.html', {'comment': comment})

class DetailView(generic.DetailView):
    model = Comment
    template_name = 'comments/detail.html'

def add_comment(request):
    return render(request, 'comments/add_comment.html')

def add_comment_form(request):
    try:
        userId = 0
        if request.user.is_authenticated():
            userId = request.user.id
        add = Comment(comment_name = request.POST['name'], 
                      comment_email = request.POST['email'],
                      comment_text = request.POST['comment'],
                      pub_date = timezone.now(),
                      user_id = userId
        )
        add.save()
    except (KeyError, Comment.DoesNotExist):
        #return HttpResponseRedirect(reverse('comments:index'))
        raise Http404('Not found')
    else:
        return HttpResponseRedirect(reverse('comments:index'))

def del_comment_form(request, comment_id):
    try:
        # Check auth
        comment = Comment.objects.get(pk = comment_id)
        if request.user.has_perm('comments.delete_comment') or comment.user_id == request.user.id:
            comment.delete()
    except (KeyError, Comment.DoesNotExist):
        # Not work
        raise Http404('Not found')
    else:
        return HttpResponseRedirect(reverse('comments:index'))

def confirm_comment_form(request, comment_id):
    try:
        # Check auth
        comment = Comment.objects.get(pk = comment_id)
        if request.user.has_perm('comments.change_comment'):
            if comment.enabled == True:
                comment.enabled = False
            else:
                comment.enabled = True
            comment.save()
            return HttpResponseRedirect(reverse('comments:detail', args=(comment_id,)))
    except (KeyError, Comment.DoesNotExist):
        # Not work
        raise Http404('Not found')
    else:
        return HttpResponseRedirect(reverse('comments:index'))

#def edit_comment(request, comment_id):
#   return render(request, 'comments/edit_comment.html')
class EditCommentView(generic.DetailView):
    model = Comment
    template_name = 'comments/edit_comment.html'

def edit_comment_form(request, comment_id):
    try:
        comment = Comment.objects.get(pk = comment_id)
        if request.user.has_perm('comments.change_comment') or comment.user_id == request.user.id:
            comment.comment_text = request.POST['comment']
            comment.save()
        return HttpResponseRedirect(reverse('comments:detail', args=(comment_id,)))
    except (KeyError, Comment.DoesNotExist):
        raise Http404('Not found')
    else:
        return HttpResponseRedirect(reverse('comments:index'))


















