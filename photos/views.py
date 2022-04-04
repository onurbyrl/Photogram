from django.shortcuts import render
from photos.models import Photo
from photos.forms import AddPhoto
from django.contrib.auth.decorators import login_required

def photos_view(request):
    photos = Photo.objects.all()
    

    return render(request, 'photos/photos.html', {
        'photos': photos
    })

@login_required
def add_photo(request):
    if request.method == 'POST':
        add_photo_form = AddPhoto(request.POST, request.FILES)

        if add_photo_form.is_valid():
            add_photo_form.save()
            # Get the current instance object to display in the template
            photo_obj = add_photo_form.instance

            return render(request, 'photos/photos.html', {
                'add_photo_form': add_photo_form,
                'photo_obj': photo_obj
            })
    else:
        add_photo_form = AddPhoto()

    return render(request, 'photos/add_photo.html', {
        'add_photo_form': add_photo_form
    })