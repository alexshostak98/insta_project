from django.forms import ModelForm
from ..models import Post


class AddPublicationForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'file', 'text',)
