from django.shortcuts import render, redirect 
from .models import Musician
from .form import MusicianForm

# Create your views here.
def add_musician(request):
      if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
      else:
        form = MusicianForm()
      return render(request,'musician.html',{'musician':form})

def edit_musician(request,id):
      musician=Musician.objects.get(pk=id)
      form=MusicianForm(instance=musician)
      if request.method == 'POST':
        form = MusicianForm(request.POST,instance=musician)
        if form.is_valid():
            form.save()
            return redirect('homepage')
   
      return render(request,'musician.html',{'musician':form})
