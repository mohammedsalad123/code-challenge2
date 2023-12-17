class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def get_name(self):
        return self.name
    #stopped
    def reviews(self):
        return self.reviews

    def customers(self):
        return list(set([review.customer for review in self.reviews]))

    @classmethod
    def all(cls):
        return cls.all_restaurants

    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_ratings = sum(review.rating for review in self.reviews)
        return total_ratings / len(self.reviews)

