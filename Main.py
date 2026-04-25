import numpy as np
import matplotlib.pyplot as plt


#UPPGIFT 1:
def vector_a():
    """Returns a numpy array from 1 to 4."""
    a = np.arange(1,6)
    return a

def vector_b():
    """Returns a numpy array from 0 to 2π with step size 0.1."""
    b = np.arange(0,2*np.pi,0.1)
    return b

def matrix():
    """Returns a 3x2 matrix."""
    a = np.arange(1,7).reshape(3,2)
    return a

def vector_a_extended():
    """Returns vector_a extended with [6,7]."""
    d = np.append(vector_a(), [6,7])
    return d

def vector_a_extended_matrix():
    """Returns vector_a extended with [-1,-2,-3,-4,-5] reshaped into a 2x5 matrix."""
    e = np.append(vector_a(), np.arange(-1,-6,-1)).reshape(2,5)
    return e

def sinus_vector_b():
    """Returns the sine of vector_b."""
    value = np.sin(vector_b())
    return value

#UPPGIFTG 2

def function_a(x):
    """Returns the square of x."""
    return x*x

def function_b1(x):
    """Returns the square of vector x."""
    value = np.square(x)
    return value

def function_b2(x):
    """Returns the dot product of x with itself."""
    scalar = np.dot(x,x)
    return scalar

def function_c1(x):
    """Returns the square of the matrix x."""
    matrix_square = np.square(x)
    return matrix_square

def function_c2():
    """_summary_
    """
    

print(np.arange(1,9).reshape(4,2))
print(function_c1(np.arange(1,9).reshape(4,2)))

#UPPGIFT 3


def plot():
