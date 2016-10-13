from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.contrib import messages
from authtools import views as authviews
from braces import views as bracesviews
from django.conf import settings
from . import forms
from .models import RequestProject
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import WorkProject


class PostProjectView(generic.CreateView):
    form_class = forms.PostProjectForm
    model = RequestProject
    template_name = 'projects/newproject.html'
    success_url = reverse_lazy('home')
    form_valid_message = "You've successfully posted a project!"

    def form_valid(self, form):
        r = super(PostProjectView, self).form_valid(form)
        title = form.cleaned_data["title"]
        description = form.cleaned_data["description"]
        email = form.cleaned_data["email"]
        return r

def listing(request):
    project_list = WorkProject.objects.all()
    paginator = Paginator(project_list, 2) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        projects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        projects = paginator.page(paginator.num_pages)

    return render(request, 'projects/list.html', {'projects': projects})