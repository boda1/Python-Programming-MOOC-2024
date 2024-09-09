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
    filtered_series = filter(lambda x: x.avg_rating >= rating, series_list)
    print(list(filtered_series))
    return filtered_series

def includes_genre(genre: str, series_list: list):
    filtered_genres = filter(lambda x: genre in x.genres, series_list) 
    return filtered_genres


s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.rate(5)

s2 = Series("South Park", 24, ["Animation", "Comedy"])
s2.rate(3)

s3 = Series("Friends", 10, ["Romance", "Comedy"])
s3.rate(2)

series_list = [s1, s2, s3]

print("a minimum grade of 4.5:")
for series in minimum_grade(4.5, series_list):
    print(series.title)

print("genre Comedy:")
for series in includes_genre("Comedy", series_list):
    print(series.title)