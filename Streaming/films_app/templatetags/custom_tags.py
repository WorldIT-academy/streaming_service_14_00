from django import template

register = template.Library()

@register.simple_tag
def amount_favourite_films(request):
    cookies = request.COOKIES.get("favourite_films")
    amount_favourite_films = 0
    if cookies:
        pk_list = cookies.split(" ")
        amount_favourite_films = len(pk_list)
    return amount_favourite_films
  
 