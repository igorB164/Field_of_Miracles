class WordList:
    def __init__(self):
        self.words = {
            "Животные": ["Собака", "Жираф", "Тигр"],
            "Города": ["Пориж", "Лондон", "Москва"],
            "Фрукты": ["Яблоко", "Банан", "Апельсин"]
        }
    
    def get_categories(self):
        return list(self.words.keys())
    
    def get_random_word(self, category):
        import random
        return random.choice(self.words.get(category, []))
