from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def print_hello(request):
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
    return render(request,'hello.html',movie_data)
