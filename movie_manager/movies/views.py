from django.shortcuts import render

# Create your views here.

def create(request):
    return render(request,'create.html')

def list(request):
    movie_data={
        'movies' : [{
        'title':'Godfather',
        'year':1990,
        'summary':'story of an untold kin',
        'sucess':True    
        },
        {
        'title':'Titanic',
        'year':1990,
        'summary':'Love story',
        'sucess':False    
        },
        {
        'title':'Kingkong',
        'year':1990,
        'summary':'story of an ape',
        'sucess':True 
        }   
    ]}
    return render(request,'list.html',movie_data)

def edit(request):
    return render(request,'edit.html')
