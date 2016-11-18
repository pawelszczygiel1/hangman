import utils
import random
import getpass


class Game:

    guesses = 11
    data_base = utils.read_data_base("words_data_base.txt")

    def __init__(self, players_number, rounds_number):
        self.players_number = players_number
        self.rounds_number = rounds_number

    def start_game(self):
        if self.players_number == 1:
            self.single_player_game()
        elif self.players_number == 2:
            self.two_players_game()
        else:
            print("Wrong number of players - end of program")

    def single_player_game(self):
        points = 0
        for i in range(self.rounds_number):
            points += self.guess(list(self.data_base[random.randint(0, len(self.data_base))]))

    def two_players_game(self):
        first_player_points = 0
        second_player_points = 0
        for i in range(self.rounds_number):
            first_player_points += self.guess(list(getpass.getpass("Word for first player to guess")))
            second_player_points += self.guess(list(getpass.getpass("Word for second player to guess")))

        if first_player_points == second_player_points:
            print("draw")
        else:
            print("".join(["First" if first_player_points > second_player_points else "Second", "won"]))

    def guess(self, word):
        current_state_of_guessing = list("_" * len(word))
        guessed_letters = 0
        guesses_left = self.guesses
        print("".join(current_state_of_guessing))
        while guesses_left > 0:
            players_guess = utils.read_guess()
            if len(players_guess) > 1:
                if players_guess == "".join(word):
                    self.correct_guessed_word(word)
                    return 1
                guesses_left -= 1
                self.wrong_guess_message(guesses_left, current_state_of_guessing)
            else:
                if players_guess not in word:
                    guesses_left -= 1
                    self.wrong_guess_message(guesses_left, current_state_of_guessing)
                else:
                    guess_occurrences = [a for a, x in enumerate(word) if x == players_guess]
                    guessed_letters += len(guess_occurrences)

                    if guessed_letters == len(word):
                        self.correct_guessed_word(word)
                        return 1

                    for j in guess_occurrences:
                        current_state_of_guessing[j] = players_guess
                    self.correct_guessed_letter(guesses_left, current_state_of_guessing)

        print("".join(["Hasłem było: ", "".join(word)]))
        return 0

    @staticmethod
    def wrong_guess_message(guesses_left, current_state_of_guessing):
        print("Wrong guess")
        print("".join(current_state_of_guessing))
        print("Guesses left:")
        print(guesses_left)

    @staticmethod
    def correct_guessed_letter(guesses_left, current_message_of_guessing):
        print("Correct guess")
        print("".join(current_message_of_guessing))
        print("Guesses left:")
        print(guesses_left)

    @staticmethod
    def correct_guessed_word(word):
        print("You guessed word")
        print("".join(word))
