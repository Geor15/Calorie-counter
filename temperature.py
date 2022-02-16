class Temperature:
    """temperature value getting from timeanddate.com/weather"""
    def __init__(self, country: str, city: str):
        self.country = country
        self.city = city

    def get(self):
        pass
