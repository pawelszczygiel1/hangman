from Game import Game


def main():
    game = Game(int(input("Enter players number")), int(input("Enter rounds number")))
    game.start_game()


if __name__ == "__main__":
    main()