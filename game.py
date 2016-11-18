import utils
import random


class Game:

    guesses = 11
    data_base = utils.read_data_base("words_data_base.txt")

    @staticmethod
    def _single_player_game(self):
        points = 0
        for i in range(self.rounds_number):
            word = self.data_base[random.randint(len(self.data_base))]
            points += self._geuss(word)

    def __init__(self, players_number, rounds_number):
        self.players_number = players_number
        self.rounds_number = rounds_number

    def start_game(self):
        if self.players_number == 1:
            self._single_player_game()

    def wrong_guess_message(self, i, current_state_of_guessing):
        print("Wrong guess")
        print(current_state_of_guessing)
        print("Guesses left:")
        print(self.guesses - i - 1)

    """def correct_guess_message(self, i, current_message_of_guessing):"""



    @staticmethod
    def _guess(self, word):
        current_state_of_guessing = "_" * len(word)
        print(current_state_of_guessing)
        for i in range(self.guesses):
            players_guess = utils.read_guess()
            if len(players_guess) > 1:
                if players_guess == word:
                    print(word)
                    self.points += 1
                else:
                    self.wrong_guess_message(self, i, current_state_of_guessing)
            else:
                if players_guess not in word:
                    self.wrong_guess_message(self, i, current_state_of_guessing)
                else:
                    correct_guess_message(self, i, current_state_of_guessing)



