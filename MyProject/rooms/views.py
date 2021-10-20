from django.shortcuts import render
from .models import Room
# Create your views here.

def rooms(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, "rooms/rooms.html", context)

def room(request, pk):
    try:
        room = Room.objects.get(id=pk)
    except Exception as ext:
        return render(request, '404.html')
    context = {'room':room}
    return render(request, 'rooms/room.html', context)