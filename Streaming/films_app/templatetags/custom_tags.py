from django import template
from films_app.models import Film

register = template.Library()

@register.simple_tag
def amount_favourite_films(request):
    cookies = request.COOKIES.get("favourite_films")
    amount_favourite_films = 0
    if cookies:
        pk_list = cookies.split(" ")
        amount_favourite_films = len(pk_list)
    return amount_favourite_films

@register.inclusion_tag("films_app/inclusion_tags/filter_genres.html")
def filter_genres():
    genres = []
    films = Film.objects.all()
    for film in films:
        if film.genre not in genres:
            genres.append(film.genre)
    return {"genres": genres}
  
 