#!/usr/bin/env python3


from brain_games.logic import calc_logic
from brain_games.engine import game_engine


def main():
    game_engine(calc_logic)


if __name__ == '__main__':
    main()