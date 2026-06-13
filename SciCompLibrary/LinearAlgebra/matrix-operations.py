import math

class Matrix:
    def __init__(self, rows: int, cols: int):
        assert (rows > 0 and cols > 0), "Cannot create a Matrix with nonpositive dimensions"
        self.data = [[0.0 for _ in range(cols)] for _ in range (rows)]
        self.rows = rows
        self.cols = cols

    @classmethod
    def from_list(cls, matrix: list):
        """
        Creates a Matrix object from a list (the input list must have uniform row lengths).
        """
        assert(isinstance(matrix[0], list)), "Matrix cannot be created from one-dimensional list, use Vector instead."
        row_size = len(matrix[0])
        for row in matrix:
            assert len(row) == row_size, "List cannot be converted to matrix, inconsistent row lengths"
        rows = len(matrix)
        cols = len(matrix[0])
        fromlist = cls(rows, cols)
        fromlist.data = matrix
        return fromlist
    
    def __str__(self):
        result = ""
        for row in self.data:
            result += f"{row}\n"
        return result
    
    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value
    
    def __add__(self, other):
        assert same_size(self, other), f"Addition can only be performed on matrices with the same dimensions.\nA dimensions: {self.rows}x{self.cols}, B dimensions: {other.rows}x{other.cols}"
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] += (self[i][j] + other[i][j])
        return result
    
    def __sub__(self, other):
        assert same_size(self, other), f"Subtraction can only be performed on matrices with the same dimensions.\nA dimensions: {self.rows}x{self.cols}, B dimensions: {other.rows}x{other.cols}"
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] += (self[i][j] - other[i][j])
        return result
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Matrix):
            return False
        if self.size() != other.size():
            return False
        for i in range(self.rows):
            if self[i] != other[i]:
                return False
        return True
    
    def __len__(self):
        return self.rows * self.cols

    def copy(self):
        """
        Returns a copy of the matrix. Use when creating an identical independent instance.
        """
        return Matrix.from_list(self.data)
    
    def size(self):
        """
        Returns the row and column lengths of the matrix.
        """
        return (self.rows, self.cols)
    
    def transpose(self):
        """
        Returns a transposed copy of the matrix.
        """
        t_matrix = Matrix(self.cols, self.rows)

        for i in range(self.rows):
            for j in range(self.cols):
                t_matrix[j][i] = self[i][j]
        
        return t_matrix
    
    def swap_rows(self, rowA: int, rowB: int):
        """
        Returns a copy of the matrix with the row at index rowA swapped with the row at index rowB.
        """

        result = self.copy()
        result[rowA] = self[rowB]
        result[rowB] = self[rowA]
        return result

    def is_square(self) -> bool:
        """
        Returns *True* if the matrix is square (rows = columns).
        Returns *False* otherwise.
        """
        return self.cols == self.rows
    
    def is_empty(self) -> bool:
        """
        Returns True if matrix has no values except 0.
        Returns false otherwise.
        """

        return self == Matrix(self.rows, self.cols)
    
    def is_upper_triangular(self) -> bool:
        """
        Returns *True* if the matrix contains only zeros below the main diagonal (upper triangular form), returns *False* otherwise.

        Non-square matrices automatically return *False*.
        """
        if (not self.is_square()):
            return False
        for i in range(1, self.rows):
            for j in range(0, i):
                if (self[i][j] != 0):
                    return False
        return True

    def is_lower_triangular(self) -> bool:
        if (not self.is_square()):
            return False
        for j in range(1, self.cols):
            for i in range(0, j):
                if (self[i][j] != 0):
                    return False
        return True

class Vector():
    def __init__(self, length: int):
        self.length = length
        self.data = [0.0 for i in range(length)]
    
    @classmethod
    def from_list(cls, vector: list):
        assert not isinstance(vector[0], list), "Vector cannot be created from two dimensional list, use a matrix instead."
        length = len(vector)
        fromlist = cls(length)
        fromlist.data = vector
        return fromlist
    
    def __str__(self) -> str:
        result = "<"
        for val in self.data:
            result += f"{val}, "
        return result[:-2] + ">\n"

    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value
    
    def __add__(self, other):
        assert len(self) == len(other), f"Addition can only be performed on vectors with the same dimensions.\nA size: {len(self)}, B size: {len(other)}"
        result = Vector(self.length)
        for i in range(self.length):
            result[i] += (self[i] + other[i])
        return result
    
    def __sub__(self, other):
        assert len(self) == len(other), f"Subtraction can only be performed on vectors with the same dimensions.\nA size: {len(self)}, B size: {len(other)}"
        result = Vector(self.length)
        for i in range(self.length):
            result[i] += (self[i] - other[i])
        return result
    
    def __truediv__(self, other):
        assert isinstance(other, (int, float)), "Can only divide a vector by scalars."
        result = Vector(self.length)
        for i in range(self.length):
            result[i] = self[i] / other
        return result

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vector):
            return False
        if self.length != other.length:
            return False
        for i in range(self.length):
            if self[i] != other[i]:
                return False
        return True
    
    def __len__(self):
        return self.length
        
    def copy(self):
        """
        Returns a copy of the vector. Use when creating an identical independent instance.
        """
        return Vector.from_list(self.data)
    
    def transpose(self) -> Matrix:
        """
        Returns a transposed copy of the vector, now in matrix form.
        """
        t_matrix = Matrix.from_list([self.data])
        return t_matrix

    def to_matrix(self) -> Matrix:
        """
        Returns a copy of the vector in Matrix form.
        """
        matrix = []
        for item in self.data:
            matrix.append([item])
        return Matrix.from_list(matrix)
    
    def magnitude(self) -> float:
        """
        Compute the 2-norm (Euclidian distance) of the vector.
        """
        result = 0.0
        for x in self.data:
            result += abs(x)**2
        result = math.sqrt(result)
        return result
    
    def normalize(self):
        mag = self.magnitude()
        return self / mag



def vector_split(self) -> list[Vector]:
        vectors = []
        for col in range(self.cols):
            vec = []
            for row in self.data:
                vec.append(row[col])
            vectors.append(Vector.from_list(vec))
        return vectors

def same_size(A: Matrix, B: Matrix) -> bool:
    """
    Returns true if the dimensions of matrix A match the dimensions of matrix B.
    Returns false otherwise.
    """
    
    return (A.rows == B.rows) and (A.cols == B.cols)

def create_identity(n: int) -> Matrix:
    """
    Returns an identity matrix of size n, e.g., when n=3,

        [1, 0, 0]

    I = [0, 1, 0]

        [0, 0, 1]
    """

    # Create an empty square matrix with dimensions nxn
    identity = Matrix(n, n)

    # Place 1's on the diagonal
    for i in range(n):
        identity[i][i] = 1
    
    return identity

def create_block_matrix(A: Matrix, B: Matrix) -> Matrix:
    """
    Returns a new matrix 
    """
    assert A.rows == B.rows, f"Number of rows in each matrix do not match,\nA rows: {A.rows}, B rows: {B.rows}."
    b_matrix = A.copy()
    for i in range(b_matrix.rows):
        b_matrix[i] += B.data[i]
    
    return b_matrix

def add_matrices(A: Matrix, B: Matrix) -> Matrix:
    assert same_size(A, B), f"Addition can only be performed on matrices with the same dimensions.\nLeft dimensions: {A.rows}x{A.cols}, Right dimensions: {B.rows}x{B.cols}"
    result = Matrix(A.rows, A.cols)
    for i in range(A.rows):
        for j in range(A.cols):
            result[i][j] += (A[i][j] + B[i][j])
        
    return result

def subtract_matrices(A: Matrix, B: Matrix) -> Matrix:
    assert same_size(A, B), f"Addition can only be performed on matrices with the same dimensions.\nLeft dimensions: {A.rows}x{A.cols}, Right dimensions: {B.rows}x{B.cols}"
    result = Matrix(A.rows, A.cols)
    for i in range(A.rows):
        for j in range(A.cols):
            result[i][j] += (A[i][j] + B[i][j])
        
    return result

def multiply_matrices(A: Matrix, B: Matrix) -> Matrix:
    assert int(A.cols) == int(B.rows), f"Number of columns in A must match the number of rows in B\nA columns: {A.cols}, B rows: {B.rows}."
    result = Matrix(A.rows, B.cols)
    for i in range(A.rows):
        for j in range(B.cols):
            for k in range(A.cols):
                result[i][j] += A[i][k] * B[k][j]
    return result


def gaussian_elimination(A: Matrix) -> Matrix:
    result = A.copy()

    noZeroPivots = True
    num_pivots = min(A.cols, A.rows)
    for pivot in range(0, num_pivots):
        if result[pivot][pivot] == 0:
            noZeroPivots = False
            # Search the rows below the current pivot to find a suitable swap
            for i in range(pivot + 1, A.rows):
                if result[i][pivot] != 0:
                    result = result.swap_rows(pivot, 1)
                    noZeroPivots = True
                    break
        # If the zero pivot cannot be resolved, elimination fails
        if noZeroPivots == False:
            print("Zero pivot encountered, Gaussian Elimination failed")
            return A
        
        elimination_matrix = create_identity(A.rows)
        for i in range(pivot+1, A.rows):
            elimination_matrix[i][pivot] = -(result[i][pivot]/ result[pivot][pivot])
        result = multiply_matrices(elimination_matrix, result)
        
    while (pivot < A.cols and pivot < A.rows):
        if result[pivot][pivot] == 0: # A zero pivot has been encountered
            noZeroPivots = False
            # Search the rows below the current pivot to find a suitable swap
            i = pivot + 1
            while i < A.rows:
                if result[i][pivot] != 0:
                    result = result.swap_rows(pivot, i)
                    noZeroPivots = True
                    break
                i += 1
        # If the zero pivot cannot be resolved, elimination fails
        if noZeroPivots == False:
            print("Zero pivot encountered, Gaussian Elimination failed")
            return A

        elimination_matrix = create_identity(A.rows)
        i = pivot + 1
        while i < A.rows:
            elimination_matrix[i][pivot] = -(result[i][pivot]/ result[pivot][pivot])
            i += 1
        result = multiply_matrices(elimination_matrix, result)
        pivot += 1
    return result

def gauss_jordan_elimination(A: Matrix) -> Matrix:
    # Step 1: Perform Gaussian Elimination
    ref_form = gaussian_elimination(A)
    if ref_form == A: # If unsuccessful, return original matrix
        print("Gauss-Jordan failed, Gaussian elimination unsuccessful.")
        return A
    
    # Step 2: Normalize the matrix (divide each row by its pivot)
    normalized_form = ref_form.copy()
    normal_rows = normalized_form.rows
    normal_cols = normalized_form.cols
    num_pivots = min(normal_cols, normal_rows)
    for i in range(num_pivots):
        pivot = normalized_form[i][i]
        for j in range(i, normal_cols):
            normalized_form[i][j] = normalized_form[i][j] / pivot
    
    # Step 3: Backwards elimination
    result = normalized_form.copy()
    multiplier = 0
    # For every row with a pivot, starting at the last pivot row working upwards
    for i in range(num_pivots-1, 0, -1): # 0 is inclusive since we will never consider the pivot on the first row
        # For every row above the current pivot row, iterating upwards
        for j in range(i-1, -1, -1):
            multiplier = result[j][i]
            # Starting at the cell above the current pivot on the current pivot row. Any cells to the left will be
            # added with 0 (because of upper triangular form), so they can be skipped
            for k in range(i, normal_cols):
                result[j][k] -= (multiplier * result[i][k])
    
    return result

def invert_matrix(A: Matrix) -> Matrix:
    # Step 0: Confirm the input is a square matrix
    assert A.is_square(), "Matrix is not square and cannot be inverted."
    # Step 1: Create a block matrix with the input matrix and an Identity matrix [A I]
    block = create_block_matrix(A, create_identity(A.rows))
    elimination = gauss_jordan_elimination(block)
    if elimination == A:
        return A
    GJ_form = elimination.copy()
    size = GJ_form.rows
    inverted = Matrix(size, size)
    for i in range(size):
        for j in range(size):
            inverted[i][j] = GJ_form[i][j + size]
    
    return inverted


def diddy():
    print('diddy')


A = [[1,2,3],
     [0,1,3],
     [0,0,3]]
B = [[4, 5, 6],
     [4, 5, 6],
     [4, 5, 6]]
C = [[0], [0], [0]]
D = [[1,2,3,4],
     [0,9,7,8],
     [0,10,11,12]]

E = Vector.from_list([1, 1, 1, 1])

A = Matrix.from_list(A)
B = Matrix.from_list(B)
C = Matrix.from_list(C)
D = Matrix.from_list(D)
I = create_identity(3)

print(vector_split(D))