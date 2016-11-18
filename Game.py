import utils
import random


class Game:

    guesses = 11
    data_base = utils.read_data_base("words_data_base.txt")

    def __init__(self, players_number, rounds_number):
        self.players_number = players_number
        self.rounds_number = rounds_number

    def start_game(self):
        self.single_player_game()

    def single_player_game(self):
        points = 0
        for i in range(self.rounds_number):
            word = list(self.data_base[random.randint(1, len(self.data_base))])
            points += self.guess(word)

    def guess(self, word):
        current_state_of_guessing = list("_" * len(word))
        guessed_letters = 0
        print("".join(current_state_of_guessing))
        for i in range(self.guesses):
            players_guess = utils.read_guess()
            if len(players_guess) > 1:
                if players_guess == "".join(word):
                    self.correct_guessed_word(word)
                    return 1

                self.wrong_guess_message(i, current_state_of_guessing)
            else:
                if players_guess not in word:
                    self.wrong_guess_message(i, current_state_of_guessing)
                else:
                    guess_occurrences = [a for a, x in enumerate(word) if x == players_guess]
                    guessed_letters += len(guess_occurrences)

                    if guessed_letters == len(word):
                        self.correct_guessed_word(word)
                        return 1

                    for j in guess_occurrences:
                        current_state_of_guessing[j] = players_guess
                    self.correct_guessed_letter(i, current_state_of_guessing)

        print("".join(["Hasłem było: ", "".join(word)]))
        return 0

    def wrong_guess_message(self, i, current_state_of_guessing):
        print("Wrong guess")
        print("".join(current_state_of_guessing))
        print("Guesses left:")
        print(self.guesses - i - 1)

    def correct_guessed_letter(self, i, current_message_of_guessing):
        print("Correct guess")
        print("".join(current_message_of_guessing))
        print("Guesses left:")
        print(self.guesses - i - 1)

    def correct_guessed_word(self, word):
        print("You guessed word")
        print("".join(word))
