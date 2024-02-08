from django.shortcuts import render,redirect,get_object_or_404
from .import form
from .import models

# Create your views here.
def add_album(request):
    if request.method == "POST":
        album_form = form.AlbumForm(request.POST)
        if album_form.is_valid():
           album_form.save()
           return redirect("homepage")
    else:
        album_form=form.AlbumForm()
    return render(request,'album.html',{'album':album_form})


def edit_album(request,id):
    # album=models.Album.objects.get(pk=id)
    album=get_object_or_404(models.Album, pk=id)
    print(album)
    album_form=form.AlbumForm(instance=album)
    # print(album_form)
    if request.method == "POST":
        album_form = form.AlbumForm(request.POST,instance=album)
        if album_form.is_valid():
           album_form.save()
           return redirect("homepage")
    # else:
    #     album_form=form.AlbumForm()
    return render(request,'album.html',{'album':album_form})

def delete_album(request,id):
   post=models.Album.objects.get(pk=id)
   post.delete()
   return redirect('homepage')
