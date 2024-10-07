import random

#This function decides whether an element of the vector is complex or not.
def imaginaryChoice(c):

    num=random.randint(1,100) #A random number from 1-100 is produced

    #If c is greater than or equal to num, f is complex
    if c>=num:
        f=1j
    
    #Otherwise, f is real
    else:
        f=1

    return f #f is returned to be multiplied by the random number produced by numgen, making it either complex or real

#This function generates a random integer between lower-bound x1 and upper-bound x2
def numGen(x1,x2):
    return random.randint(x1,x2) #Returns the random integer

#This function generates a random vector of length n composed of numbers between x1 and x2 with a c% chance of being complex.
def vectorGen(n,x1,x2, c):

    v=[] #Empty vector is declared so that it may have elements appended.

    for i in range(n): #Loops through vector-length n.

        v.append(imaginaryChoice(c)*numGen(x1,x2)) #n-elements are appended to v, defined by numGen multiplied by imaginaryChoice
        
    return v #The vector is returned

#Here is a bit of code to test different inputs for creating a vector. 
print(vectorGen(5,-10,10,50))
