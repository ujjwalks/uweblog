from django.test import TestCase
from projects.models import RequestProject
from projects.forms import PostProjectForm

# Create your tests here.

class ProjectTestCase(TestCase):
    def test_post_project_form(self):
        form_data = {'title': 'test', 'description':'test description', 'deadline':'2016-10-16','email':'ujjwalks01@gmail.com'}
        form = PostProjectForm(data = form_data)
        self.assertTrue(form.is_valid(), True)
    
    def test_missing_field__post_project_form(self):    
        response = self.client.post("/projects/post/", {'title':'test'})
        self.assertFormError(response, 'form', 'email', 'This field is required.')

    def test_listing_projects(self):
        pass
