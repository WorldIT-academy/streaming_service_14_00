from django import template
from films_app.models import Film

# Об'єкт для реєстрації тегів шаблонів
register = template.Library()

#Створюємо простий кастомний тег (тег, що протсо повертажє значення к-ті улюблених фільмів)
@register.simple_tag
#функція для тегу
def amount_favourite_films(request):
    #Отримуємо cookie files
    cookies = request.COOKIES.get("favourite_films")
    #Змінні відповідає за к-ть улюблених фільмів
    amount_favourite_films = 0
    #Перевіряємо, чи є кукі
    if cookies:
        #ділимо cookie по пробілу, утворюючи список з pk улюблених фільмів
        pk_list = cookies.split(" ")
        #беремо довжину списку
        amount_favourite_films = len(pk_list)
    #повертає к-ть улюблених фільмів
    return amount_favourite_films

# Створюємо включаючий тег для рендеру банеру найкращого фільм
@register.inclusion_tag("films_app/inclusion_tags/best_film.html")
# Робимо функцію для відображення найкращого фільму
def render_best_film():
    # Отримуємо об'єкт фільму по ключу
    film = Film.objects.get(pk = 1)
    # Повертаємо об'єкт для відображення у best_film.html
    return {"film": film}
    
# створюємо включаючий тег шаблону, що рендерить  HTML-шаблон 'list_of_films.html'
@register.inclusion_tag('films_app/inclusion_tags/list_of_films.html')
# функція відображення тегу для генерації списку фільмів
def render_list_films(list_films):
    # повертає список з фільмами для подальшого відображення у list_of_films.html
    return {'list_films': list_films}

