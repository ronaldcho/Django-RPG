from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Character, Fighter, Mage, Cleric, thread_info()


def index(request):
    return HttpResponse("Character Creator App!")


@login_required(next='/charactercreator/characters/')
def view_all_characters(request):
    characters = Character.objects.all()
    context = {'characters': characters}
    thor = character.objects.get(pk=2)
    context = {'header': 'My cool header message!', 'characters': 'godly_character': thor}
    return render(request, 'character/index.html', context)


def view_character(request):
    pass
