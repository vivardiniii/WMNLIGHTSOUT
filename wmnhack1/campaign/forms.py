from django import forms
from .models import Campaign
from django.contrib.auth.models import User
from django.utils import timezone
from location_field.models.plain import PlainLocationField
from django.utils.translation import ugettext_lazy as _
from django.forms import fields
from location_field.widgets import LocationWidget


class WaterForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ('user','image', 'title', 'date', 'duration','text', 'isPublic', 'location')
        labels = {
            'user': _('Your Username'),
            'iname': _('Issue Name'),
            'image': _('Image Upload (Optional)'),
            'title': _('Title of Campaign'),
            'date': _('Date of Today'),
            'duration': _('How long is the Campaign? (Optional)'),
            'text': _('A Little Bit About the Campaign'),
            'isPublic': _('Is this a public event (choose yes) or an individual effort (choose no)?'),
            'location': _('If a public event, where is it happening?'),
        }

'''class EditPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'date', 'image','hname')
class UserForm(forms.ModelForm):
    username = forms.CharField(help_text='Enter your last name',
                                widget=forms.TextInput(attrs={'placeholder': 'Username'}), required=False)
    email = forms.EmailField(help_text='Enter your email id',
                             widget=forms.EmailInput(attrs={'placeholder': 'Mail id'}), required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
'''
