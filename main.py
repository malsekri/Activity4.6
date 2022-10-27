x = input("What is your name?") #This asks for your name

#This asks for the values of the equation
a = float(input("What is your a?"))
b = float(input("What is your b?"))
c = float(input("What is your c?"))

#These are some calculations
d = b**2 - 4*a*c
roota = (-b + d**0.5)/(2*a)
rootb = (-b - d**0.5)/(2*a)

#This provides the solution to the equation
print("Hello", x , "the roots for this equation are", roota , "and", rootb)

quit()
