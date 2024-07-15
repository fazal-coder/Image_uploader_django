from django import forms
from .models import Image  # Ensure you have imported your Image model

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'  # Include all fields from the Image model in the form
        labels = {'photo': ''}  # Set the label for the 'photo' field to an empty string

