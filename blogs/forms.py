from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'maincontent','image']

    def clean_image(self):
        image = self.cleaned_data.get('image')

        if image:
            if image.size > 2 * 1024 * 1024:  # 2MB limit
                raise forms.ValidationError("Image too large. Max size is 2MB.")

        return image

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']