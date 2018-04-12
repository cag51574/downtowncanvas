from django.contrib.auth.models import Permission, User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import ArtForm, UserForm, ArtistDataForm
from .models import *
from django.utils import timezone

# Create your views here.


IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def home(request):
    #arts = Art.objects.filter(user=request.user)
    arts = Art.objects.all()
    slides = Art.objects.all()
    stories = Story.objects.all()
    context = {'arts' : arts,
               'slides':slides,
               'stories': stories}
    return render(request, 'art/home.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                arts = Art.objects.filter(user=request.user)
                return render(request, 'art/home.html', {'arts': arts})
            else:
                return render(request, 'art/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'art/login.html', {'error_message': 'Invalid login'})
    return render(request, 'art/login.html')
    
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    return render(request, 'art/login.html', { "form": form })

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        new_user.set_password(password)
        new_user.first_name = new_user.first_name.title()
        new_user.last_name = new_user.first_name.title()
        new_user.save()
        new_user = authenticate(username=username, password=password)
        if new_user is not None:
            if new_user.is_active:
                login(request, new_user)
                return home(request)
            else:
                return render(request, 'art/register.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'art/register.html', {'error_message': 'Invalid login'})
    context = { "form": form }
    return render(request, 'art/register.html', context)


def detail(request, art_id):
    if not request.user.is_authenticated():
        return render(request, 'art/login.html')
    else:
        user = request.user
        art = get_object_or_404(Art, pk=art_id)
        return render(request, 'art/detail.html', {'art': art, 'user': user})


def delete_art(request, art_id):
    art = Art.objects.get(pk=art_id)
    art.delete()
    arts = Art.objects.filter(user=request.user)
    profile = UserData.objects.get(user=request.user)
    user_data = UserData.objects.filter(is_artist=True).get(user=request.user)
    context = {'user': user_data,
               'arts' : arts,
               'slides':slides}
    return render(request, 'art/profile.html', context)


def profile(request):
    try:
        user = User.objects.get(username=request.user)
        if user.userdata.is_artist:
            try:
                if request.method == 'POST':
                    print("CAAAAAAAAAATSSSSSSSS")
                    print(request.POST.get('color2'))
                    artist = ArtistData.objects.get(user=request.user)
                    artist.colorbar = '#' + request.POST.get('color2')
                    print(artist.colorbar)
                    artist.save()
                else: 
                    print("SSSSSSSSShit")
                artist = ArtistData.objects.get(user=request.user)
                arts = Art.objects.filter(user=request.user)
                context = {
                   'artist' : artist,
                   'arts'   : arts,
                }
                return render(request, 'art/profile.html', context)
            except:
                return edit_profile(request)

        else:
            return render(request, 'art/artist_signup.html')
    except:
        print("Exception!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return render(request, 'art/artist_signup.html')
    return render(request, 'art/artist_signup.html')



def artists(request):
    artists = ArtistData.objects.all()
    return render(request, 'art/artists.html', {'artists' : artists } )

def create_art(request):
    try:
        user_data = UserData.objects.get(user=request.user)
        if user_data.is_artist:
            form = ArtForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                art = form.save(commit=False)
                art.user = request.user
                pic = request.FILES['pic']
                file_type = art.pic.url.split('.')[-1]
                file_type = file_type.lower()
                if file_type not in IMAGE_FILE_TYPES:
                    context = {
                        'art': art,
                        'form': form,
                        'error_message': 'Image file must be PNG, JPG, or JPEG',
                    }
                    return render(request, 'art/create_art.html', context)
                art.date_created=timezone.now()
                art.save()
                return render(request, 'art/detail.html', {'art': art})
            context = { "form": form, }
            return render(request, 'art/create_art.html', context)
        return render(request, 'art/artist_signup.html')
    except:
        return render(request, 'art/artist_signup.html')
    return render(request, 'art/artist_signup.html')


def edit_profile(request):
    if not request.user.is_authenticated():
        return render(request, 'art/artist_signup.html')
    else:
#        try:
        user = User.objects.get(username=request.user)
        if(user.userdata.is_artist): 
            form = ArtistDataForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                formInput = form.save(commit=False)
                file_type = formInput.profile_pic.url.split('.')[-1]
                file_type = file_type.lower()
                if file_type not in IMAGE_FILE_TYPES:
                    context = { 'profile': profile,
                                'form': form,
                                'error_message': 'Image file must be PNG, JPG, or JPEG',
                    }
                file_type = formInput.banner_pic.url.split('.')[-1]
                file_type = file_type.lower()
                if file_type not in IMAGE_FILE_TYPES:
                    context = { 'profile': profile,
                                'form': form,
                                'error_message': 'Image file must be PNG, JPG, or JPEG',
                    }
                    return render(request, 'art/edit_profile.html', context)
                artist, created = ArtistData.objects.update_or_create(
                    user=request.user,
                    defaults={
                        'user'       : request.user,
                        'birthdate'  : formInput.birthdate,
                        'profile_pic': formInput.profile_pic,
                        'banner_pic' : formInput.banner_pic,
                        'bio'        : formInput.bio,
                        'description': formInput.description, 
                        'quote1'     : formInput.quote1,
                        'quote2'     : formInput.quote2,
                        'in_college' : formInput.in_college,
                        'address'    : formInput.address,
                        'fav_genre'  : formInput.fav_genre,

                    }

                )
                artist.save()
                arts = Art.objects.filter(user=request.user)
                context = {
                   'artist' : artist,
                   'arts'   : arts,
                }
                return render(request, 'art/profile.html', context)
            context = { "form": form, }
            return render(request, 'art/edit_profile.html', context)
        else:
            return render(request, 'art/artist_signup.html')
#        except:
#            print("Exception!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#            return render(request, 'art/artist_signup.html')


#create search function
def search(request):
    query = request.GET.get("q")
    artists = User.objects.filter(
#        is_artist__gte=True
#    ).filter( 
        Q(first_name__icontains=query)| 
        Q(last_name__icontains=query)
    ).distinct()
    if artists:
        return render(request, 'art/search_results.html', {'artists':artists})
    else:
        print("no artists")
    return render(request, 'art/home.html')
    
def artist_signup(request):
    return render(request, 'art/artist_signup.html')

def update_color(request):
    if request.method == 'POST':
        artist = ArtistData.objects.get(user=request.user)
        artist.colorbar = request.POST.get('color')

