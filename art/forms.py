from django.contrib.auth.models import User
from django import forms
from django.forms import extras 
from .models import UserData, Art, ArtistData

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','email','password','first_name','last_name']

#class UserDataForm(forms.ModelForm):
#    
#    class Meta:
#        model = UserData 
#        fields = ['first_name', 'last_name', 'pic', 'bio', 'description', 'favorite_artists', 'favorite_genres']

class ArtForm(forms.ModelForm):
    class Meta:
        model = Art
        fields = ['pic', 'title', 'description', 'genre', 'price']


class ArtistDataForm(forms.ModelForm):
    birthdate = forms.DateField(widget=extras.SelectDateWidget(years=range(1920,2015)))
    profile_pic = ProcessedImageField(spec_id='art:artist:profile_pic',
                                           processors=[ResizeToFill(400, 400)],
                                           format='JPEG',
                                           options={'quality': 60})

    banner_pic = ProcessedImageField(spec_id='art:artist:banner_pic',
                                           processors=[ResizeToFill(1600, 175)],
                                           format='JPEG',
                                           options={'quality': 60})


    class Meta:
        model = ArtistData
        fields = [
            'birthdate', 
            'profile_pic', 
            'banner_pic', 
            'bio',
            'description', 
            'quote1',
            'quote2',
            'in_college',
            'address',
        ]
