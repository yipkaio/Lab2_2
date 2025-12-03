def display_main_menu():
   print("display_main_menu")
   print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    print("get_user_input")   
    arraylist=[]
    numstring=input()
    numlist=numstring.split(",")
    for eachnum in numlist:
        arraylist.append(float(eachnum))
    print(arraylist)
    return arraylist
    

def calc_average(arraylist):
    print("calc_average")
    total=sum(arraylist) # summing of numbers in list
    average = total/len(arraylist) #len = number of items in array list
    print("Average = ", round(average,2)) 
    return round(average,2)



def find_min_max(arraylist):
    print("find_min_max")
    templist=sort_temperature(arraylist)
    min=templist[0]
    max=templist[-1]
    print("MIN = "+str(min)+" and MAX= "+str(max))
    return [min,max]


def sort_temperature(arraylist):
    print("sort_temperature")
    templist=arraylist.copy()
    templist.sort()
    print("Sorted numbers = ",templist)
    return templist


def calc_median_temperature(arraylist):
    print("calc_median_temperature")
    numlen = len(arraylist)
    remainder= numlen %2
    if remainder == 1:
        median=arraylist[numlen/2]
    else: 
        median =(arraylist[numlen//2]+arraylist[numlen//2 -1])
    print("median= "+str(median))



def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")  
    display_main_menu()
    arraylist = get_user_input()
    calc_average(arraylist)
    find_min_max(arraylist)
    calc_median_temperature(arraylist)

if __name__ == "__main__":
    main()