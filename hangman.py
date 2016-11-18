from Game import Game


def main():
    game = Game(input("Podaj liczbę graczy"), input("Podaj liczbę rund"))
    game.start_game()


if __name__ == "__main__":
    main()