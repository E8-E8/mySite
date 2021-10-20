from django.shortcuts import render

# Create your views here.

def rooms(request):
    return render(request, "rooms/rooms.html")

def room(request):
    return render(request, 'rooms/room.html')