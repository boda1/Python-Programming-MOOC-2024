# Write your solution here:

class Series:
    def __init__(self, title: str, num_seasons: int, genres: list):
        self.title = title
        self.num_seasons = num_seasons
        self.genres = genres
        self.count_ratings = 0
        self.avg_rating = 0
        self.total_ratings = 0

    def __str__(self):
        genre_string = ", ".join(self.genres)
        if self.count_ratings > 0:
            return f"{self.title} ({self.num_seasons} seasons)\ngenres: {genre_string}\n{self.count_ratings} ratings, average {self.avg_rating:.1f} points"    
        else:
            return f"{self.title} ({self.num_seasons} seasons)\ngenres: {genre_string}\nno ratings"
    
    def rate(self, rating: int):
        self.total_ratings += rating
        self.count_ratings += 1
        self.avg_rating = self.total_ratings / self.count_ratings


def minimum_grade(rating: float, series_list: list):
    filtered_series = list(filter(lambda x: x.avg_rating >= rating, series_list))
    return filtered_series

def includes_genre(genre: str, series_list: list):
    filtered_genres = list(filter(lambda x: genre in x.genres, series_list) )
    return filtered_genres
