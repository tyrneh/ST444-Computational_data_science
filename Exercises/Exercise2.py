# 1. Read in an integer n, then decide if it is within 10 of 100 or 200.

def within10():
    number = int(input("what is your integer? "))

    if abs(100 - number) <= 10:
        print("within 10 of 100")
    elif abs(200 - number) <= 10:
        print("within 10 of 200")
    else:
        print("not close to 100 or 200")


# within10

# 2. Read in an integer n (say from 1 to 4000), then decide if it represents a leap year or not.

def leapyear():
    year = int(input("year: "))
    if year % 4 != 0:
        print("common")
    elif year % 100 != 0:
        print("leap")
    elif year % 400 != 0:
        print("common")
    else:
        print("leap")


# leapyear()

"""3. We want make a package of M (integer) kilos of chocolate. We have small bars (1 kilo each),
medium bars (5 kilos each) and big bars (10 kilos each). Read in the integer M and print the
minimum number of bars to use. Here you can take for granted that the greedy algorithm
works."""


# greedy solution algo using a loop
def chocolate_loop_algo():
    kilos = int(input("how many kilos of chocolate? "))

    remaining = kilos
    big = 10
    med = 5
    small = 1

    num_big = 0
    num_med = 0
    num_small = 0

    while remaining / big >= 1:
        num_big += 1
        remaining -= big

    while remaining / med >= 1:
        num_med += 1
        remaining -= med

    while remaining / small >= 1:
        num_small += 1
        remaining -= small

    if remaining == 0:
        print("the number of big, med, and small bars are: {}, {}, {}".format(num_big, num_med, num_small))


# chocolate_loop_algo()

# greedy solution algo using closed-form solution
def chocolate_sol_algo():
    kilos = int(input("how many kilos of chocolate? "))

    big = 10
    med = 5

    num_big = kilos // big
    num_med = (kilos % big) // med
    num_small = ((kilos % big) % med)

    print(num_big, num_med, num_small)

# chocolate_sol_algo()gi
