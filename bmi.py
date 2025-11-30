def calculate_bmi(height,weight):
    print("Height= " +str(height))
    print("Weight= " ,weight) # can put comma to make it a string type
    bmi= weight/(height*height)
    print("BMI= "+str(round(bmi,2)))
    if bmi<18.5:
        print("Under Weight")
    elif bmi>25.0:
        print("Over Weight")
    else:
        print("Normal Weight")
calculate_bmi(weight=67, height=1.75)