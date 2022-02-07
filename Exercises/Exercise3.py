"""
1. Read in a string and a positive integer n, return a larger string that is n copies of the original
string (e.g. “Hi” and 3 → “HiHiHi”).
"""

def copies_of_string(string,n):
    """note that string must be input as a 'string',
    n must be input as an integer"""
    print(string*n)





"""
2. Make a two-player Rock-Paper-Scissors game. Ask for players’ names first, then ask them to
play, make a comparison, print out a message of congratulations to the winner, and finally
ask if the players want to start a new game.
"""

def rock_paper_scissors():
    p1 = input("what is player 1's name? ")
    p2 = input("what is player 2's name? ")

    loop = True
    while loop == True:
        p1_move = input(p1+": what move? (Choose between rock, paper, scissors) ")
        p2_move = input(p2+": what move? (Choose between rock, paper, scissors) ")
        if p1_move == p2_move:
            print("tie. Next round")
        else:
            if p1_move == 'rock':
                if p2_move == 'paper':
                    print(p2, 'wins')
                    loop = False
                else:
                    print(p1, 'wins')
                    loop = False
            if p1_move == 'paper':
                if p2_move == 'rock':
                    print(p1, 'wins')
                    loop = False
                if p2_move == 'scissors':
                    print(p2, 'wins')
                    loop = False
            if p1_move == 'scissors':
                if p2_move == 'rock':
                    print(p2, 'wins')
                    loop = False
                if p2_move == 'paper':
                    print(p1, 'wins')
                    loop = False




"""
3. Ask the user for a positive integer and determine whether that number is prime or not.
"""
def prime_checker(n):
    """
    idea: number is prime iff it's divisible by 1 and itself
    so iterate from 1 to the number n, and if only 2 remainders are 0, then that number is prime

    this will be O(n) complexity, but I'm sure there's more efficient algorithms by checking GCDs
    """
    num_zero_remainders = 0

    for i in range(1,n+1):
        if n % i == 0:
            num_zero_remainders += 1

    if num_zero_remainders == 2:
        print("number is prime")
    else:
        print("number is not prime")


"""
4. Implement the bisection method to find the minimum of a univariate function f. 
Here f' is assumed unknown.
"""

"""
idea: we will define a function using f(x),
create a function to evaluate its derivative, 
and then define a function bisection_optimisation() to find the optimum
"""


def f(x):
    # define function here
    return (x+1)**2

def bisection_optimization(upper = 1, lower = -1, tolerance = 1.0e-8):
    """
    calculates optimum of function.
    define function using f(x) in previous step
    """

    def derivative_of_function_at_t(t, epsilon=1.0e-5):
        """
        calculates the derivative evaluated at t of function f(x)
        we approximate the derivative of f() using finite differencing

        input: x, f(x)
        output: derivative of function at x
        """
        return ((f(t + epsilon) - f(t - epsilon)) / (2 * epsilon))

    iter = 0
    uncertainty = upper - lower
    while uncertainty > tolerance:
        middle = (upper + lower)/2
        if derivative_of_function_at_t(middle) > 0:
            upper = middle
        else:
            lower = middle
        uncertainty = upper - lower
        iter += 1
    print("Min at:", middle)
    print("Num of iterations:", iter)

# bisection_optimization()


"""
5. Implement the Newton’s method to find the minimum of a univariate function f. 
Here f' and f'' are assumed unknown.
"""

"""
idea: we will define a function using f(x),
create a function to evaluate its derivative and a function to evaluate its 2nd derivative, 
and then define a function newton_optimisation() to find the optimum
"""

def f(x):
    # define function here
    return (x+8)**2

def newton_optimisation(now = 1, past = 0, tolerance = 1.0e-8, max_iter = 1000):
    """
    calculates optimum of function.
    define function using f(x) in previous step
    """

    def derivative_of_function_at_t(t, epsilon=1.0e-5):
        """
        calculates the derivative evaluated at t of function f(x)
        we approximate the derivative of f() using finite differencing

        input: x, f(x)
        output: derivative of function at x
        """
        return ((f(t + epsilon) - f(t - epsilon)) / (2 * epsilon))

    def second_derivative_of_function_at_t(t, epsilon=1.0e-5):
        derivative_pos = (f(t + epsilon) - f(t)) / (epsilon)
        derivative_neg = (f(t) - f(t - epsilon)) / (epsilon)
        second_derivative = (derivative_pos - derivative_neg) / (epsilon)
        return second_derivative

    iter = 0
    # we need to check BOTH delta-x < tolerance and f'(x) < tolerance are satisfied
    while abs(now - past) > tolerance or abs(derivative_of_function_at_t(now)) > tolerance:
        past = now
        now = now - derivative_of_function_at_t(now) / second_derivative_of_function_at_t(now)
        iter += 1
        if iter > max_iter:
            break
    print("Minimum at", now)
    print("Number of total iterations is", iter)

# newton_optimisation()