from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Film
import colorama

colorama.init(autoreset= True)
RED = colorama.Fore.RED
# Create your views here.
def render_films(request):
    cookies = request.COOKIES.get('favourite_films')
    response = render(request, "films_app/films.html", context={"all_films": Film.objects.all()})
    if cookies:
        response.set_cookie('favourite_films', cookies)
    else:
        response.set_cookie('favourite_films', '')
        
    # return render(request, "films_app/films.html", context={"all_films": Film.objects.all()})
    return response

def add_to_favourite(request: HttpRequest, film_pk: int):
    try:
        response = redirect("all_films")
        #
        cookies = request.COOKIES.get('favourite_films')
        
        film = Film.objects.get(pk= film_pk)
        if cookies:
            if str(film_pk) not in cookies:
                cookies += " " + str(film_pk)
                film.favourite = True
            else:
                list_cookies=  cookies.split(" ").remove(str(film_pk))
                film.favourite = False
                if list_cookies:
                    for element in list_cookies: cookies += " " + element
        else:
            cookies = str(film_pk)
            film.favourite = True
            #
        film.save()
        response.set_cookie('favourite_films', cookies)
        return response
    except Exception as error:
        print(f"ERROR: -> {RED}{error}")

def render_favourite_films(request):
    cookies = request.COOKIES.get("favourite_films")
    favourite_films = []
    if cookies:
        list_cookies = cookies.split(" ")
        favourite_films = Film.objects.filter(pk__in = list_cookies)
    
    return render(request, 'films_app/favourite_films.html', context = {"favourite_films":favourite_films})