""" Python simulator for conways game of life
"""
from copy import deepcopy
from os import system
from random import random
from sys import argv
from sys import exit as exit_
from time import sleep

from termcolor import colored

SIZE = int(argv[1]) if len(argv) > 1 else 10
PROB = float(argv[2]) if len(argv) > 2 else .7


def create_empty_matrix(size: int) -> list[list[str]]:
    """
    Create an empty life matrix.

    Args:
        size (int): Height and width of matrix

    Returns:
        list[list[str]]: a 2D matrix made of lists of "-" of size `size`
    """
    return [["-"] * size for _ in range(size)]


def random_matrix(size: int, prob: float) -> list[list[str]]:
    """
    Generate matrix of size `size` with random spots of life

    Args:
        size (int): size of matrix
        prob (float): likelihood of each cell being alive

    Returns:
        list[list[str]]: a 2D matrix made of lists
    """
    matrix = create_empty_matrix(size)
    for i in range(1, size-1):
        for j in range(1, size-1):
            if random() <= prob:
                matrix[i][j] = "*"
    return matrix


def print_matrix(matrix: list[list[str]]) -> None:
    """
    Function to print matrix.

    Args:
        matrix (list[list[str]]): Matrix to print
    """
    system("clear")
    for row in matrix:
        for item in row:
            if item != "*":
                print(" ", "", end="")
            else:
                print(colored(item, "green", attrs=['bold']), "", end="")
        print("", end="\n")
    print()


def update_matrix(matrix: list[list[str]]) -> list[list[str]]:
    """
    Update matrix using conways rules

    Any live cell with two or three live neighbours survives.
    Any dead cell with three live neighbours becomes a live cell.
    All other live cells die in the next generation. Similarly, all other dead
        cells stay dead.

    Args:
        matrix (list[list[str]]): Matrix to update

    Returns:
        list[list[str]]: Update Matrix
    """
    size = len(matrix)
    out = create_empty_matrix(size)
    for i in range(1, size-1):
        for j in range(1, size-1):
            if matrix[i][j] == "-":  # dead cell
                out[i][j] = dead_cell_logic(matrix, i, j)
            else:  # alive cell
                out[i][j] = alive_cell_logic(matrix, i, j)
    return out


def dead_cell_logic(matrix: list[list[str]], i: int, j: int) -> str:
    """
    Logic of whether a dead cell lives or not.

    Any dead cell with three live neighbours becomes a live cell.

    Args:
        matrix (list[list[str]]): Matrix to update
        i (int): Row of cell to update
        j (int): Column of cell to update

    Returns:
        str: "*" if cell should be alive, "-" else
    """
    alive_neighbors = 0 + (1 if matrix[i-1][j-1] == "*" else 0)
    alive_neighbors += 1 if matrix[i-1][j] == "*" else 0
    alive_neighbors += 1 if matrix[i-1][j+1] == "*" else 0
    alive_neighbors += 1 if matrix[i][j-1] == "*" else 0
    alive_neighbors += 1 if matrix[i][j+1] == "*" else 0
    alive_neighbors += 1 if matrix[i+1][j-1] == "*" else 0
    alive_neighbors += 1 if matrix[i+1][j] == "*" else 0
    alive_neighbors += 1 if matrix[i+1][j+1] == "*" else 0
    return "*" if alive_neighbors == 3 else "-"


def alive_cell_logic(matrix: list[list[str]], i: int, j: int) -> str:
    """
    Logic of whether an alive cell lives or not.

    Any live cell with two or three live neighbours survives.

    Args:
        matrix (list[list[str]]): Matrix to update
        i (int): Row of cell to update
        j (int): Column of cell to update

    Returns:
        str: "*" if cell should be alive, "-" else
    """

    alive_neighbors = 0 + (1 if matrix[i-1][j-1] == "*" else 0)
    alive_neighbors += 1 if matrix[i-1][j] == "*" else 0
    alive_neighbors += 1 if matrix[i-1][j+1] == "*" else 0
    alive_neighbors += 1 if matrix[i][j-1] == "*" else 0
    alive_neighbors += 1 if matrix[i][j+1] == "*" else 0
    alive_neighbors += 1 if matrix[i+1][j-1] == "*" else 0
    alive_neighbors += 1 if matrix[i+1][j] == "*" else 0
    alive_neighbors += 1 if matrix[i+1][j+1] == "*" else 0
    return "*" if alive_neighbors in {2, 3} else "-"


def check_alive(matrix) -> bool:
    for row in matrix:
        for item in row:
            if item == "*":
                return True
    return False


def main():
    """main()"""
    outs = random_matrix(SIZE, PROB)
    print_matrix(outs)
    while True:
        old_outs = deepcopy(outs)
        outs = update_matrix(outs)
        if old_outs == outs:
            exit_(0)
        print_matrix(outs)
        if not check_alive(outs):
            exit_(0)
        sleep(.5)


if __name__ == '__main__':
    main()
