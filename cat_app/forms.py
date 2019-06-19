from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Cat_Topic_Comment, Cat_Topic


class UserCreateForm(UserCreationForm):

	class Meta:
		fields = ("username", "password1", "password2")
		model = get_user_model()

	def __init__(self, *args, **kwargs):
		super(UserCreateForm, self).__init__(*args, **kwargs)
		self.fields["username"].label = "Username:"
		self.fields["username"].help_text = None
		self.fields["password1"].help_text = None
		self.fields["password2"].help_text = None


class CatCommentForm(forms.Form):
	user = forms.ModelChoiceField(queryset=User.objects.all())
	cat_topic = forms.ModelChoiceField(queryset=Cat_Topic.objects.all())
	comment = forms.CharField()
	comment_picture_path = forms.CharField(required=False)

	class Meta:
		fields = ("user", "cat_topic", "comment", "comment_picture_path")
		model = Cat_Topic_Comment


