from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.contrib import messages
from authtools import views as authviews
from braces import views as bracesviews
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
from . import forms
from .models import RequestProject
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import WorkProject


class PostProjectView(generic.TemplateView):
    form_class = forms.PostProjectForm
    model = RequestProject
    template_name = 'projects/newproject.html'
    success_url = reverse_lazy('home')
    form_valid_message = "You've successfully posted a project!"
    
    def get(self, request, *args, **kwargs):
        if "post_project_form" not in kwargs:
            kwargs["post_project_form"] = forms.PostProjectForm()
        return super(PostProjectView, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        
        post_project_form = forms.PostProjectForm(request.POST)
        if not (post_project_form.is_valid()):
            messages.error(request, "There was a problem with the form. "
                           "Please check the details.")
            post_project_form = forms.PostProjectForm()
            return super(PostProjectView, self).get(request,
                                                post_project_form=post_project_form)
        # Both forms are fine. Time to save!
        post_project_form.save()
        messages.success(request, "Your project or problem details saved!")
        return redirect("home")

    def form_valid(self, form):
        r = super(PostProjectView, self).form_valid(form)
        title = form.cleaned_data["title"]
        description = form.cleaned_data["description"]
        email = form.cleaned_data["email"]
        return r
    
class SlideShowView(generic.CreateView):
    template_name = 'hello.html'


def listing(request):
    project_list = WorkProject.objects.all()
    paginator = Paginator(project_list, 3) # Show 25 contacts per page

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

class AjaxTemplateMixin(object): 
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'ajax_template_name'):
            split = self.template_name.split('.html')
            split[-1] = '_inner'
            split.append('.html')
            self.ajax_template_name = ''.join(split)
            if request.is_ajax():
                self.template_name = self.ajax_template_name
        return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)