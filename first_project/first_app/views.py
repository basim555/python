from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
   # return HttpResponse("<h1>Welcome to home</h1>")
   my_greetings = {'insert_me':'Hello class'}
   return render(request, 'first_app/index.html', context=my_greetings)