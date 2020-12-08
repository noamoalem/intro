import numpy as np
import ex8


def test_sudokos():
    for i in range(1, 25):
        verify_sudoku_solution(i,
            "data/sudoku_"+str(i)+"_in.csv", "data/sudoku_"+str(i)+"_out.csv")


def verify_sudoku_solution(i, input_filename, output_filename):
    actual = np.loadtxt(input_filename, delimiter=",", encoding="utf",
                        dtype="int")
    ex8.solve_sudoku(actual)
    expected = np.loadtxt(output_filename, delimiter=",", encoding="utf",
                          dtype="int")
    if (expected == actual).all():
        print("test " + str(i) + " passed.")
    else:
        print("test " + str(i) + " FAILED!")


if __name__ == '__main__':
    test_sudokos()
