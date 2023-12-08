def addition(a,b):    
   return a + b   
def subtraction(a,b):   
   return a - b  
def multiplication(a,b):   
   return a * b 
def division(a,b):   
   return a / b    
print (" Select any Operation.")    
print ("1. Addition")    
print ("2. Subtraction")    
print ("3. Multiplication")    
print ("4. Division")    
    
choice = input(" Enter Choice (1/2/3/4): ")    
    
n1= int (input ("Enter the 1st number: "))    
n2 = int (input ("Enter the 2nd number: "))    
    
if choice == '1':    
   print (n1, " + ", n2, " = ", addition(n1,n2))    
    
elif choice == '2':    
   print (n1, " - ", n2, " = ", subtraction(n1,n2))    
    
elif choice == '3':    
   print (n1, " * ", n2, " = ", multiplication(n1,n2))
   
elif choice == '4':
    if n2 == 0:
        print("Zero division error...Enter valid number")
    else:    
        print (n1, " / ", n2, " = ", division(n1,n2))
   
else:    
   print ("Enter valid input")    
