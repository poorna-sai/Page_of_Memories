from django import forms
from django.forms import ModelForm
from .models import *
from ckeditor.widgets import CKEditorWidget
class postform(ModelForm):
	description = forms.CharField(widget=CKEditorWidget())
	class Meta:
		model = Posts
		fields = '__all__'

