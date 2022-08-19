# This is a metric function calculator. The program prompts the user for 2 points and computes the distance between
# them given the metric input

def main():  # driver function
    option = input("Press <enter> to continue or q to quit: ")
    while option != 'q':  # while loop used for 'infinite user' entries
        a = input("\nEnter the first point (x1,y1): ").split(',')  # split into a list by comma
        b = input("Enter the second point (x2,y2): ").split(',')
        metric = input("Enter the metric of your choice: ").capitalize()
        if metric == 'Euclidean':  # conditional statements used to call a particular function
            euclidean(a, b)  # call euclidean metric
        elif metric == 'Manhattan':
            manhattan(a, b)  # call manhattan metric
        else:
            discrete(a, b)  # call discrete metric
        option = input("\nPress <enter> to continue or q to quit: ")
    print("\nThank you for using the Metric Calculator")  # break from while loop


def euclidean(a, b):
    d = (((int(b[0]) - int(a[0])) ** 2) + ((int(b[1]) - int(a[1])) ** 2)) ** .5  # Euclidean distance function
    print(f"Metric: {round(d, 2)}")


def manhattan(a, b):
    d = (int(b[0]) - int(a[0])) + (int(b[1]) - int(a[1]))  # Manhattan distance function
    print(f"Metric: {d}")


def discrete(a, b):
    if a == b:  # discrete conditionals
        print("Metric: 0")
    else:
        print("Metric: 1")


if __name__ == '__main__':  # special variable __name__
    main()  # call to main
