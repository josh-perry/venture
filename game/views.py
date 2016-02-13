from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


class RootView(TemplateView):
    def get(self, request, **kwargs):
        return HttpResponse("hello")

    def post(self, request, **kwargs):
        pass
