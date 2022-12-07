import numpy as np
from pprint import pprint as pp

def create_square_matrix(size: int) -> np.ndarray:
    '''Creates a square matrix based on size

    Args:
        size (int): Size of the matrix

    Returns:
        np.ndarray: NumPy object containing the array
    '''
    matrix = np.random.randint(10,1000, size=(size, size))
    return matrix

def search_consecutive(matrix: np.ndarray, consecutive: int = 4) -> bool:
    '''Searchs for consecutive number on a matrix

    Args:
        matrix (np.ndarray): NumPy matrix
        consecutive (int, optional): Number of consecutive numbers to find. Defaults to 4.

    Returns:
        bool: If consecutive numbers has been found it returns True, otherwise False.
    '''
    for v in np.vstack((matrix, matrix.T)):
        count = 1         
        current_num = 0   
        for i in range(1, len(v)):
            diff = v[i] - v[i-1]

            if diff == 1:  
                if current_num != 1: 
                    count = 1
                current_num = 1
                count += 1
            elif diff == -1:
                if current_num != -1: count = 1
                current_num = -1
                count += 1
            else:
                current_num = 0
                count = 1
            if count == consecutive:
                return True
    return False


if __name__ == '__main__':
    matrix = create_square_matrix(5)
    print(
        search_consecutive(matrix)
    )