def calculate_bmi(height,weight):
    print("Height= " +str(height))
    print("Weight= " ,weight) # can put comma to make it a string type
    bmi= weight/(height*height)
    print("BMI= "+str(round(bmi,2)))
    if bmi<18.5:
        print("Under Weight")
        return -1
    elif bmi>25.0:
        print("Over Weight")
        return 1
    else:
        print("Normal Weight")
        return 0
print(calculate_bmi(weight=30,height=1.8))
print(calculate_bmi(weight=67, height=1.75))
print(calculate_bmi(weight=90,height=1.8))