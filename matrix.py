import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices larger than 2x2.")
        
        if self.g[0][0]*self.g[1][1]==self.g[0][1]*self.g[1][0]:
            raise ValueError ('Determinant of matrix is zero')
            
        if self.g==1:
            determinant=[[self.g[0][0]]]
        
        if self.g==2:
            determinant=[[self.g[0][0]*self.g[1][1] - self.g[0][1]*self.g[1][0]]]
            

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        if self.g.is_square():
            for i in range(self.g):
                trace_sum=grid[i][i]

        # TODO - your code here

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")    
        # TODO - your code here
        
        if len(self.g)==1:
            inverse=[[1/self.g[0][0]]]
        
        elif len(self.g)==2:      
        
            if self.g[0][0]*self.g[1][1]==self.g[0][1]*self.g[1][0]:
                raise ValueError ('Determinant of matrix is zero')
            
            if self.g[0][0]*self.g[1][1]!=self.g[0][1]*self.g[1][0]:
                fac = 1/(self.g[0][0]*self.g[1][1] - self.g[0][1]*self.g[1][0])
                inverse = [[fac * self.g[1][1], self.g * -self.g[0][1]],[fac * -self.g[1][0], fac * self.g[0][0]]]
        return inverse 
  
            
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = []
        for row in range(len(self.g)) :
        #print(row)
            rez=[[self.g[i][j] for i in range(len(self.g))] for j in range(len(self.g[0]))]
    #print("\n")
        for row in rez:
            matrix_transpose.append(row)
        
        return matrix_transpose
    
    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        
        
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "To sum two matrices up, size of matrices need to be the same") 
        
        m = zeroes(self.h,self.w)
        for i in range(self.h):
            for j in range(self.w):
                m[i][j] = self[i][j] + other[i][j] 
        return m


    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here (self.h,self.w)

        #neg_matrix=zeroes(self.h,self.w)
        for i in range(self.h):
            for j in range(self.w):
                self[i][j] *= -1
        return self

        
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the sizes are the same") 
        matrix = zeroes(self.h,self.w)
        for i in range(self.h):
            for j in range(self.w):
                matrix[i][j] = self[i][j] - other[i][j] 
        return matrix



    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        if self.w != other.h :
            raise(ValueError, "Number of columns must be equal")
        
        result = zeroes(self.h, other.w) 
        for row in range(result.h):
            for col in range(result.w):
                result[row][col] = sum(self[row][k]*other[k][col] for k in range(self.w))
    
   
        return result

        
        
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            r = []
            for i in range(self.h):
                q = []
                for j in range(self.w):
                    new = other * self[i][j]
                    q.append(new)
                r.append(q)
            
            return Matrix(r)