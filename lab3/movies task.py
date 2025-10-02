# 1. Проверка: у фильма рейтинг > 5.5
def is_high_rating(movie):
    return movie["imdb"] > 5.5

# 2. Фильмы с рейтингом > 5.5
def high_rating_movies(movies):
    return [m for m in movies if m["imdb"] > 5.5]

# 3. Фильмы по категории
def movies_by_category(movies, category):
    return [m for m in movies if m["category"] == category]

# 4. Средний рейтинг всех фильмов
def average_imdb(movies):
    return sum(m["imdb"] for m in movies) / len(movies)

# 5. Средний рейтинг по категории
def average_category_imdb(movies, category):
    category_movies = movies_by_category(movies, category)
    return sum(m["imdb"] for m in category_movies) / len(category_movies)


if __name__ == "__main__":
    movies = [
        {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
        {"name": "Hitman", "imdb": 6.3, "category": "Action"},
        {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
        {"name": "The Help", "imdb": 8.0, "category": "Drama"},
        {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
        {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
        {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    ]

    print(is_high_rating(movies[0]))                # True
    print(high_rating_movies(movies))               # фильмы > 5.5
    print(movies_by_category(movies, "Romance"))    # только Romance
    print(average_imdb(movies))                     # средний рейтинг
    print(average_category_imdb(movies, "Romance")) # средний рейтинг Romance
