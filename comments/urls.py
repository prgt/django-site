from django.conf.urls import url

from . import views
app_name = 'comments'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add_comment/$', views.add_comment, name='add_comment'),
    url(r'^add_comment/add/$', views.add_comment_form, name='add_comment_form'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<comment_id>[0-9]+)/delete/$', views.del_comment_form, name='del_comment_form'),
    url(r'^(?P<comment_id>[0-9]+)/confirm/$', views.confirm_comment_form, name='confirm_comment_form'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.EditCommentView.as_view(), name='edit_comment'),
    url(r'^(?P<comment_id>[0-9]+)/edit/edit$', views.edit_comment_form, name='edit_comment_form'),
]
