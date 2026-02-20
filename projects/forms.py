from django.forms import ModelForm
from django import forms
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "featured_image",
            "demo_link",
            "source_link",
            "tags",
        ]
        widgets = {
            "tags": forms.SelectMultiple(attrs={"class": "form-select", "size": "5"})
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update(
            {"class": "form-control", "id": "Title", "placeholder": "Add title"}
        )
        self.fields["description"].widget.attrs.update(
            {
                "class": "form-control",
                "id": "Description",
                "placeholder": "Add description",
            }
        )
        self.fields["featured_image"].widget.attrs.update(
            {"class": "form-control", "id": "Featured image"}
        )
        self.fields["demo_link"].widget.attrs.update(
            {"class": "form-control", "id": "Demo link", "placeholder": "Add demo link"}
        )
        self.fields["source_link"].widget.attrs.update(
            {
                "class": "form-control",
                "id": "Source link",
                "placeholder": "Add source link",
            }
        )
