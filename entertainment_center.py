# Importing Dependencies for this script to run
import media
import fresh_tomatoes

# Transformers Movie: movie title, storyline, poster image, and movie trailer
transformers_thelastknight = media.Movie(
    "Transformers: The Last Knight",
    "Robots doing stuff and lots of explosions",
    "https://upload.wikimedia.org/wikipedia/en/2/26/Transformers_The_Last_Knight_poster.jpg", # NOQA
    "https://www.youtube.com/watch?v=AntcyqJ6brc"
)

#  The Hunger Games: movie title, storyline, poster image, and movie trailer
the_hunger_games = media.Movie(
    "The Hunger Games",
    "People are hungry in this movie",
    "https://s2982.pcdn.co/wp-content/uploads/2015/11/Hunger-Games-Teaser-Poster-Large.jpg", # NOQA
    "https://www.youtube.com/watch?v=LrXIG4oK7Ew"
)

# Pokemon Movie: movie title, storyline, poster image, and movie trailer
pokemon_the_first_movie = media.Movie(
    "Pokemon: The First Movie",
    "Trailer description here but I miss the old pokemon",
    "https://mvpo.us/img/P805.jpg", # NOQA
    "https://www.youtube.com/watch?v=sSLuNZFa_3k"
)

# Attack on Titan Movie: movie title, storyline, poster image, and movie trailer
attack_on_titan = media.Movie(
    "Attack on Titan (film)",
    "Surprisingly bad but good watch when buzzed",
    "https://i.pinimg.com/originals/c1/2d/10/c12d10c1ee602d7684a82d7e70a30811.jpg", # NOQA
    "https://www.youtube.com/watch?v=InF16sp7J0M"
)

# Spirited Away: movie title, storyline, poster image, and movie trailer
spirited_away = media.Movie(
    "Spirited Away",
    "The best animated film of all time, don't @me",
    "https://i.ebayimg.com/images/g/th8AAOSwKoRZY0id/s-l1600.jpg", # NOQA
    "https://www.youtube.com/watch?v=nsrWpFmB2bQ"
)

# Set the movies that will be passed to the media file
movies = [
    transformers_thelastknight,
    the_hunger_games,
    pokemon_the_first_movie, 
    attack_on_titan, 
    spirited_away
]

# Open the HTML file in a webbrowser via the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)