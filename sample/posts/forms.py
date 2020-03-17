from django import forms

from django_quill.forms import QuillFormField
from .models import QuillPost


class QuillFieldForm(forms.Form):
    normal_content = QuillFormField()


class QuillPostForm(forms.ModelForm):
    class Meta:
        model = QuillPost
        fields = (
            'content',
        )
