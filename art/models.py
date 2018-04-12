from django.contrib.auth.models import Permission, User
from django.db import models
#from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from colorfield.fields import ColorField

# Create your models here.

NONE = 'NO'
FRACTALS = 'FR'
SPACE = 'SP'
CARTOON  = 'CA'
PROGRESSIVE = 'PR'
REALISM = 'REA'
RELIGIOUS = 'REL'
PSYCADELIC = 'PS'
ABSTRACT = 'AB'
TAPESTRY = 'TA'
POSTER= 'PO'
SELF_PORTRAIT = 'SE'
WILDLIFE = 'WI'
SYMBOLIC = 'SY'
OTHER = 'OT'

GENRES = (
    (NONE, 'None'),
    (FRACTALS, 'Fractals'),
    (SPACE, 'Space'),
    (CARTOON , 'Cartoon'),
    (PROGRESSIVE , 'Progressive'),
    (REALISM , 'Realism'),
    (RELIGIOUS , 'Religious'),
    (PSYCADELIC , 'Psycadelic'),
    (ABSTRACT , 'Abstract'),
    (TAPESTRY , 'Tapestry'),
    (POSTER, 'Poster'),
    (SELF_PORTRAIT, 'Self-Portrait'),
    (WILDLIFE, 'Wildlife'),
    (SYMBOLIC, 'symbolic'),
    (OTHER, 'Other'),
)

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_artist = models.BooleanField(default=False)
    number_of_logins = models.IntegerField(default=0)

    def __str__(self):
        return 'username = ' + self.user.username  

#Automatically create UserData when account created
@receiver(post_save, sender=User)
def create_user_data(sender, instance, created, **kwargs):
    if created:
        UserData.objects.create(user=instance)

#Automatically create UserData when user.save() is called.
@receiver(post_save, sender=User)
def save_user_data(sender, instance, **kwargs):
    instance.userdata.save()

class ArtistData(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    birthdate = models.DateField()

    profile_pic = ProcessedImageField(
        upload_to='artists/profile_pics',
        processors=[ResizeToFill(400, 400)],
        format='JPEG',
        options={'quality': 60}
    )
#    profile_pic = models.ImageField(upload_to='artists/profile_pics', default='default/fractal.png')
    banner_pic = ProcessedImageField(
        upload_to='artists/banner_pics',
        processors=[ResizeToFill(1600, 175)],
        format='JPEG',
        options={'quality': 60}
    )
#    banner_pic = models.ImageField(upload_to='artists/banner_pics', default='default/fractal.png')
    favorite_art = models.ImageField()
    bio = models.TextField(max_length=3000, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    fav_artists = models.CharField(max_length=300, null=True, blank=True)
    fav_genre = models.CharField(max_length=3, choices=GENRES, null=True, blank=True)
    numberOfArts = models.IntegerField(default=0);
    quote1 = models.CharField(max_length=300, null=True, blank=True)
    quote2 = models.CharField(max_length=300, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    in_college = models.BooleanField()
    number_of_arts_sold = models.IntegerField(default=0)
    total_profile_views = models.IntegerField(default=0)
    total_art_views = models.IntegerField(default=0)
    total_art_likes = models.IntegerField(default=0)
    colorbar = ColorField(default='#FF0000')

    def __str__(self):
        return 'username = ' + self.user.username  

class Art(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=32, null=True, blank=True)
    pic = models.ImageField(upload_to='artists/art')
    description = models.CharField(max_length=300, null=True, blank=True)
    tags = models.CharField(max_length=300, null=True, blank=True)
    likes = models.IntegerField(default=0)
    date_created = models.DateField()
    #price is in cents
    price = models.DecimalField(max_digits=6, decimal_places=2)
    genre = models.CharField(max_length=3, choices=GENRES, null=True, blank=True)

    def __str__(self):
        return 'title = ' + self.title

class ArtCreativeProcess(models.Model):
    final_art = models.ForeignKey(Art, related_name='creative_process')
    process = models.ImageField(upload_to='artists/creative_process')
    description = models.CharField(max_length=64, null=True, blank=True)

class Story(models.Model):
    artist = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    pic = ProcessedImageField(
        upload_to='artists/banner_pics',
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 60}
    )
    title = models.CharField(max_length=32)
    date_created = models.DateField(default=timezone.now)
    text = models.CharField(max_length=1000)
    preview = models.CharField(max_length=100)







#class UserData(models.Model):
#    user = models.ForeignKey(User, default=1)
#    first_name = models.CharField(max_length=20, default='')
#    last_name = models.CharField(max_length=20, default='')
#    pic = models.ImageField(upload_to='artists/profilePictures', default='default/fractal.png')
#    bio = models.TextField(max_length=3000, null=True, blank=True)
#    description = models.CharField(max_length=500, null=True, blank=True)
#    favorite_artists = models.CharField(max_length=300, null=True, blank=True)
#    favorite_genres = models.CharField(max_length=300, null=True, blank=True)
#    is_artist = models.BooleanField(default=False)
#
#    def __str__(self):
#        return 'username = ' + self.user.username  


#class Art(models.Model):
#    user = models.ForeignKey(User, default=1)
#    title = models.CharField(max_length=64, null=True, blank=True)
#    pic = models.ImageField(upload_to='artists/profilePictures')
#    description = models.CharField(max_length=300, null=True, blank=True)
#    genre = models.CharField(max_length=64, null=True, blank=True)
#    tags = models.CharField(max_length=300, null=True, blank=True)
#    likes = models.IntegerField(default=0)
#    date_created = models.DateField()
#
#    def __str__(self):
#        return 'title = ' + self.title



