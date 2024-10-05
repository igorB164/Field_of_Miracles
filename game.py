from wordlist import WordList
from player import Player
from utils import clear_screen

class Game:
    def __init__(self):
        self.players = []
        self.wordlist = WordList()
        self.current_word = ""
        self.guessed_word = []
        self.current_player_index = 0
        self.max_attempts = 10
        self.selected_category = None
        self.setup_players()

    def setup_players(self):
        # Запрашиваем количество игроков
        while True:
            try:
                num_players = int(input("Введите количество игроков (1-3): "))
                if 1 <= num_players <= 3:
                    break
                else:
                    print("Введите число от 1 до 3.")
            except ValueError:
                print("Пожалуйста, введите число.")
        
        # Запрашиваем имена игроков
        self.players = []
        for i in range(num_players):
            name = input(f"Введите имя игрока {i + 1}: ")
            self.players.append(Player(name))

    def choose_category(self):
        categories = self.wordlist.get_categories()  # Предполагаем, что этот метод возвращает список категорий
        print("Выберите категорию:")
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")
        
        while True:
            try:
                choice = int(input("Введите номер категории: "))
                if 1 <= choice <= len(categories):
                    self.selected_category = categories[choice - 1]
                    break
                else:
                    print("Выберите корректный номер категории.")
            except ValueError:
                print("Пожалуйста, введите номер категории.")

    def start(self):
        clear_screen()
        print("Добро пожаловать в 'Поле Чудес'!")
        self.choose_category()  # Добавляем выбор категории
        self.current_word = self.wordlist.get_random_word(self.selected_category)  # Передаем выбранную категорию
        self.guessed_word = ["_" for _ in self.current_word]
        self.play_round()

    def play_round(self):
        attempts = 0
        while "_" in self.guessed_word and attempts < self.max_attempts:
            player = self.players[self.current_player_index]
            print(f"Current word: {' '.join(self.guessed_word)}")
            letter = player.guess_letter()
            if letter in self.current_word:
                self.update_guessed_word(letter)
            else:
                attempts += 1
                print(f"Неправильная догадка! Осталось попыток: {self.max_attempts - attempts}")
            self.switch_player()

        if "_" not in self.guessed_word:
            print("Поздравляем! Слово угадано!")
        else:
            print(f"Игра окончена! Слово было: {self.current_word}")


    def update_guessed_word(self, letter):
        letter = letter.upper()
        current_word_upper = self.current_word.upper()
        
        for i, char in enumerate(current_word_upper):
            if char == letter:
                self.guessed_word[i] = self.current_word[i]

    def switch_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
