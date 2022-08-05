# This program creates a scatter plot of the Barnsley Fern Fractal

import random as rand  # generate random probabilities
import matplotlib.pyplot as fern  # used for scatter plot


def main():
    """
    Driver Function of the program. Asks user how many times to iterate. Calls fractal function on iterations
    :return: A scatter plot
    """
    iterations = int(input("How many times would you like to iterate? "))
    x_values, y_values = fractal(iterations)  # calling fractal function
    fern.scatter(x_values, y_values, s=.1, color='g')  # creating plot
    fern.title('Barnsley Fern Fractal')  # customizing plot
    fern.grid()
    fern.show()


def fractal(iterations):
    """
    This function creates a list of x and y values using a random probability. A for loop is used to iterate in the
    range of iterations. Particular equations used below to determine x and y values based on the probability generated
    :param iterations: int value
    :return: list of x and y values
    """
    x = 0  # initializing x and y values
    y = 0
    x_values = [x]  # creating lists of x and y values
    y_values = [y]
    for i in range(iterations):
        probability = rand.random()
        if probability <= .85:  # most common iteration (%85)
            x = .85 * x + .04 * y
            y = -.04 * x + .85 * y + 1.6
        elif probability <= .92:  # %7
            x = .2 * x - .26 * y
            y = .23 * x + .22 * y + 1.6
        elif probability <= 0.99:  # %7
            x = -.15 * x + .28 * y
            y = .26 * x + .24 * y + .44
        else:  # %1
            x = 0
            y = .16 * y
        x_values.append(x)  # appending lists for every value through the loop
        y_values.append(y)
    return x_values, y_values  # returning to main


if __name__ == '__main__':  # special variable __name__
    main()  # call to main
