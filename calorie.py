class Calorie:
    """Represent amount of calories by calculating with
    BMR = 10*weight + 6.25*height - 5*age + 5 - 10*temperature"""

    def __init__(self, weight: float, height: float, age: int, temperature: float):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        pass
