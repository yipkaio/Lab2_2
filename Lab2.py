def display_main_menu():
    # Display instructions for user input
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    print("get_user_input")   

    arraylist = []                  # List to store numbers entered by user
    numstring = input()             # Read entire line as text (string)
    numlist = numstring.split(",")  # Split string into separate items using comma

    # Convert each split item into a float and store into arraylist
    for eachnum in numlist:
        arraylist.append(float(eachnum))

    print(arraylist)                # Show converted list of floats
    return arraylist                # Return the list back to main program


def calc_average(arraylist):
    print("calc_average")

    total = sum(arraylist)            # Add up all numbers
    average = total / len(arraylist)  # Divide sum by number of items

    print("Average = ", round(average, 2))
    return round(average, 2)          # Return rounded average


def find_min_max(arraylist):
    print("find_min_max")

    templist = sort_temperature(arraylist)  # Sort numbers first
    min_value = templist[0]                 # First element is minimum
    max_value = templist[-1]                # Last element is maximum

    print("MIN = " + str(min_value) + " and MAX= " + str(max_value))
    return [min_value, max_value]           # Return min and max in a list


def sort_temperature(arraylist):
    print("sort_temperature")

    templist = arraylist.copy()   # Make a copy so original list is unchanged
    templist.sort()               # Sort numbers in ascending order

    print("Sorted numbers = ", templist)
    return templist               # Return sorted list


def calc_median_temperature(arraylist):
    print("calc_median_temperature")

    templist = sorted(arraylist)     # Make a sorted version of the list
    numlen = len(templist)           # Number of items

    # If number of items is odd
    if numlen % 2 == 1:
        median = templist[numlen // 2]   # Middle element

    # If number of items is even
    else:
        mid1 = templist[numlen // 2 - 1]  # First middle element
        mid2 = templist[numlen // 2]      # Second middle element
        median = (mid1 + mid2) / 2        # Average of two middle values

    print("median = " + str(median))
    return median


def main():
    # Display title of program
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")  
    
    display_main_menu()              # Step 1: show menu
    arraylist = get_user_input()     # Step 2: read numbers entered
    calc_average(arraylist)          # Step 3: calculate average
    find_min_max(arraylist)          # Step 4: get min & max
    calc_median_temperature(arraylist)  # Step 5: compute median


# Entry point of the program
if __name__ == "__main__":
    main()
