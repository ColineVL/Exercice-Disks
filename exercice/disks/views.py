from django.shortcuts import render, get_object_or_404

from .models import Album


# Create your views here.


def tous_albums(request):
    albums = Album.objects.all()
    return render(request, 'disks/tousAlbums.html', {'listeAlbums': albums})


def details_album(request, id, title):
    album = get_object_or_404(Album, id=id)
    return render(request, 'disks/detailsAlbum.html', {'album': album})

def test(request):
    return render(request, 'disks/test.html')