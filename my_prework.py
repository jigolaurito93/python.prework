# Question 1:
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(username):
    print("hello_" + username + "!")

hello_name('USERNAME')

print("\n")

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.

def first_odds():
    for odd in range(100):
        if odd % 2 == 1:
            print(odd) 

first_odds()

print("\n")

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    numbers = max(a_list)
    print(numbers)
    
numbers = [2, 9, 10, 80, 30, 38]
 
max_num_in_list(numbers)

print("\n")



# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

#def is_leap_year(a_year):
#series of if sttements

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] 
# are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.


def is_consecutive(a_list):
    for i in range(1, len(a_list)):
        if a_list[i] - a_list[i-1] != 1:
            return False 
    return True

numbers1 = [1,2,3,4,5]
numbers2= [1,2,4,5,6]

print(is_consecutive(numbers1))
print(is_consecutive(numbers2))