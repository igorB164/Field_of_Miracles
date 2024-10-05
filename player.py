class Player:
    def __init__(self, name):
        self.name = name  # Сохраняем имя игрока
        self.score = 0  # Можно добавить другие атрибуты по необходимости

    def guess_letter(self):
        # Логика для угадывания буквы
        return input(f"{self.name}, введите букву: ").lower()
