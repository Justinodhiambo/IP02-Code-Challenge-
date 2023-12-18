class Restaurant:
    def __init__(self, name):
        self.name = name
        self.reviews = []

    def name(self):
        return self.name

    def reviews(self):
        return self.reviews

    @classmethod
    def all(cls):
        return cls.instances

    def customers(self):
        return list(set([review.customer for review in self.reviews]))

    def average_star_rating(self):
        if not self.reviews:
            return 0
        return sum([review.rating for review in self.reviews]) / len(self.reviews)
