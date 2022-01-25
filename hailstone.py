# Author: Esteban Cajamarca GitHub username: EstebanCajamarca Date: 1/24/2022 Write a function named hailstone that
# takes a positive integer parameter as the initial number of a hailstone sequence and returns how many steps it
# takes to reach 1 (technically you could keep going 1, 4, 2, 1, 4, 2, etc. but you will stop when you first reach
# 1). If the starting integer is 1, the return value should be 0, since it takes no steps to reach 1 (we're already
# there).

# Creating function hailstone.
def hailstone(n):
    # counter starts at zero.
    count = 0
    # defining condition to repeat action when numbers are positive different from one.
    while n != 1 and n > 1:
        # if remainder is equal to zero, program divides n/2.
        if n % 2 == 0:
            """Remainder has to be zero, so it is even."""
            n = (n / 2)
        else:
            # for any other case, program will multiply n by three and add one to make it odd.
            n = (n * 3) + 1
            """When n is an odd number."""
        # counter keeps track of iterations.
        count = count + 1
    # print(n)

    # returns value, number of iterations.
    return count


# Testing
answer = hailstone(1000)
print(answer)