from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from game.models import Player, Room


class RootView(TemplateView):
    def get(self, request, **kwargs):
        return HttpResponse("hello")

    def post(self, request, **kwargs):
        pass


class RoomView(TemplateView):
    def get(self, request, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponse("Not authenticated!")

        player = Player.objects.filter(user=request.user).first()

        room = player.current_room
        resp = "<h1>{0}</h1>{1}".format(room.name, room.description)

        resp += "<h2>Exits</h2>"
        for exit in room.exits.all():
            resp += exit.name + "<br/>"

        return HttpResponse(resp)

    def post(self, request, **kwargs):
        pass


class Command(View):
    def get(self, request, **kwargs):
        return Http404()

    def post(self, request, **kwargs):
        command = request.POST.get("request", None)
