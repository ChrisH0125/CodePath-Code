#Understand the problem
#We first define a function 
#It takes an integer n and essentially returns a 1-indexed string array 
#Return a variable answer
#We would need to add parameters for the function
#We need a empty list to store all of the values
#For an edge case like a negative number, we can simply just do a conditional (if statement)
#Use a for loop to loop through the ranges starting at 1 and ends at n + 1
#use if and elif statements 
#Append
#Return at the end

#Plan
#Define our function
#Create the empty list, answer = []
#for loop through the ranges n to n + 1
#if statements
#append it to the list
#return answer
def hulk_smash(n):
    answer = []
    for i in range(1, n+1):
        if i % 3 and i % 5 == 0:
            answer.append("HulkSmash")
        elif i % 3 == 0:
            answer.append("Hulk")
        elif i % 5 == 0:
            answer.append("Smash")
        else:
            answer.append(str(i))
    return answer
n = 15
print(hulk_smash(n))
