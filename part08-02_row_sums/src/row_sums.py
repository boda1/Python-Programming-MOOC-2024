# Write your solution here

import numpy as np

def row_sums(my_matrix: list):
    """
    my_matrix = np.array(my_matrix)
    row_sums = my_matrix.sum(axis=1).reshape((-1, 1))
    my_matrix = np.concatenate((my_matrix, row_sums), axis=1)
    """

    for item in my_matrix:
        item.append(sum(item))
    
    print(my_matrix)

def main():
    my_matrix = [[1, 1], [2, 2]]
    my_matrix = row_sums(my_matrix)

if __name__ == "__main__":
    main()