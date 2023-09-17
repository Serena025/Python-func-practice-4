#Write a Python function called max_num()to find the maximum of three numbers.

#def max_num(a, b, c):

#    if (a >= b) and (a >= c):
#        largest = a
    
#    elif (b >= a) and (b >= c):
#        largest = b
    
#    else:
#        largest = c 

#    return largest

#a = 5
#b = 7
#c = 4
#print(max_num(a, b, c))

#Write a Python function called mult_list() to multiply all the numbers in a list.

#def mult_list(myList):
#    result = 1
#    for x in myList:
#        result = result * x
#    return result 

#list1 = [2, 3, 4]
#print(mult_list(list1))


#Write a Python function called rev_string() to reverse a string.

#import string


#def rev_string(x):
#    return x[::-1]

#mytxt = rev_string("Serena")  
#print (mytxt)  



#Write a Python function called num_within() to check whether a number falls in a given range.

#def num_within(n):
#    if n in range(2,8):
#        print(" %s is in the range"%str(n))
#    else:
#        print("The number is outside the given range.")
#num_within(6)


#Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

def pascal(n):
     row = [1]
     yield row
     for _ in range(n):
         row = [1] + [x + y for x, y in zip(row[:-1], row[1:])] + [1]
         yield row
 
for row in pascal(5):
     print(row)
