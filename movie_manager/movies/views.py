from django.shortcuts import render
from .models import MovieInfo
# Create your views here.
from .forms import MovieForm
def create(request):
    frm = MovieForm(request.POST)
    if request.method == 'POST':
        if frm.is_valid():
           frm.save()
        else:
            frm = MovieForm()
  
    return render(request,'create.html',{'frm':frm})

def list(request):
    #movie_set=MovieInfo.objects.all()
    #print(movie_set)
    return render(request,'list.html',{'movies': MovieInfo.objects.all()})

def edit(request,pk):
    return render(request,'edit.html')

def delete(request,pk):
    instance=MovieInfo.objects.get(pk=pk)
    instance.delete()
    movie_set=MovieInfo.objects.all()
    return render(request,'list.html',{'movies':movie_set})