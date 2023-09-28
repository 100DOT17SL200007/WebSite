from PIL.EpsImagePlugin import field
from django.forms import ModelForm
from .models import Project
from django import forms


class ProjectF(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    for n, f in self.fields.items():
        field.widget.attrs.update({'class': 'input'})
#     #
#     self.fields['title'].widget.attrs.update({'class': 'input'})
#     self.fields['description'].widget.attrs.update({'class': 'input'})
