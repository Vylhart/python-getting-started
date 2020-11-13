from django.shortcuts import render
from .models import Room
# Create your views here.
def chat_room(req, label):
    room, created = Room.objects.get_or_create(label=label)
    messages = reversed(room.messages.order_by('-timestamp')[:50])

    return render(req, 'chat/room.html', {
        'room': room,
        'messages': messages,
    })
    