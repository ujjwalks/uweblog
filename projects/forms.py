from django import forms

from .models import RequestProject
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field

class PostProjectForm(forms.ModelForm):

    class Meta:
        model = RequestProject
        fields = ('title', 'description','deadline','email',)
        
#     def __init__(self, *args, **kwargs):
#         super(PostProjectForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.fields["title"].widget.input_type = "project"  # ugly hack
# 
#         self.helper.layout = Layout(
#             Field('title', placeholder="Title of Project"),
#             Field('description', placeholder="Description of Project"),
#             Field('email', placeholder="Enter Email", autofocus=""),
#             Submit('post_project', 'Post Project', css_class="btn-warning"),
#             )