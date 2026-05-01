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
    """Plots f(x) = 1 + x + 4/(x - 2)^2."""
    # Create x values, avoiding x = 2 where the function is undefined
    x1 = np.linspace(-10, 1.9, 500)  # Left of asymptote
    x2 = np.linspace(2.1, 10, 500)   # Right of asymptote
    
    # Calculate y values for each segment
    y1 = 1 + x1 + 4 / (x1 - 2)**2
    y2 = 1 + x2 + 4 / (x2 - 2)**2
    
    # Create the plot
    plt.plot(x1, y1, 'b-', label='f(x) = 1 + x + 4/(x - 2)²')
    plt.plot(x2, y2, 'b-')
    
    # Add vertical asymptote at x = 2
    plt.axvline(x=2, color='r', linestyle='--', alpha=0.5, label='Asymptote: x = 2')
    
    # Add oblique asymptote y = x + 1
    x_asymptote = np.linspace(-10, 10, 100)
    y_asymptote = x_asymptote + 1
    plt.plot(x_asymptote, y_asymptote, 'g--', alpha=0.5, label='Asymptote: y = x + 1')
    
    # Labels and formatting
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('f(x) = 1 + x + 4/(x - 2)²')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.ylim(-10, 10)  # Limit y-axis for better visualization
    plt.show()


# Call the plot function
plot()
