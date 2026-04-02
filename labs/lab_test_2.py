#MUHAMMAD SYAHDIQ ASYRAF BIN TIPILIL @ RAPAHIL
#CO2T
#LAB TEST 2 OF LISTS

#ASK USER TO INSERT FIVE NUMBERS
num_1 = int(input("Enter number 1: "))
num_2 = int(input("Enter number 2: "))
num_3 = int(input("Enter number 3: "))
num_4 = int(input("Enter number 4: "))
num_5 = int(input("Enter number 5: "))

#MAKE THE FIVE NUMBERS INTO A LIST
num_list = [num_1,num_2,num_3,num_4,num_5]

#MAKE A FUNCTION FOR ORDERING LIST
def ordering_list(num_list):

    #MAKE THE LIST ORDERED
    order = sorted(num_list)

    #RETURN OUTCOME FOR ORDERED LIST
    return order

#MAKE A FUNCTION FOR SUMMARY OF NUMBERS IN THE LIST
def summary_num(num_list):

    #CALCULATE THE SUMMARY OF NUMBERS IN THE LIST
    summary = sum(num_list)

    #RETURN OUTCOME FOR SUMMARY NUMBERS IN THE LIST
    return summary

#MAKE A FUNCTION TO FIND MAXIMUM NUMBER IN THE LIST
def max_num(num_list):

    #FIND THE LARGEST NUMBER AMONG NUMBERS IN THE LIST 
    largest = max(num_list)

    #RETURN THE MAXIMUM NUMBER
    return largest

#PRINT ALL THE OUTPUT BASED ON THE OPERATION
result1 = ordering_list(num_list)
result2 = summary_num(num_list)
result3 = max_num(num_list)
print (f"Numbers in ascending order: {result1}")
print (f"Sum of all numbers: {result2}")
print (f"Largest number: {result3}")

