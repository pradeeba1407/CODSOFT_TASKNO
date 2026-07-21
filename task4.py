# Simple Movie Recommendation System (Content-Based Filtering)

movies = {
    "Avengers": ["Action", "Superhero", "Adventure"],
    "Iron Man": ["Action", "Superhero", "Sci-Fi"],
    "Batman": ["Action", "Superhero", "Crime"],
    "Frozen": ["Animation", "Family", "Fantasy"],
    "Moana": ["Animation", "Adventure", "Family"],
    "Interstellar": ["Sci-Fi", "Adventure", "Drama"],
    "Inception": ["Sci-Fi", "Action", "Thriller"]
}

# Get user input
favorite = input("Enter your favorite movie: ")

if favorite in movies:
    fav_genres = movies[favorite]
    recommendations = []

    for movie, genres in movies.items():
        if movie != favorite:
            common = set(fav_genres) & set(genres)
            if len(common) > 0:
                recommendations.append(movie)

    print("\nRecommended Movies:")
    if recommendations:
        for movie in recommendations:
            print("-", movie)
    else:
        print("No recommendations found.")
else:
    print("Movie not found in the database.")