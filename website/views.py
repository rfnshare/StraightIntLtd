from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.views import View


class HomeView(View):
    def get(self, request, guess):
        var = {
            'guess': int(guess)
        }
        return render(request, 'website/index.html', var)

    def post(self, request):
        return HttpResponse('Class based view')
