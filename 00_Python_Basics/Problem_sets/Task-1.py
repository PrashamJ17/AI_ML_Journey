"""### Q1 :- Print the given strings as per stated format.

**Given strings**:
```
"Data" "Science" "Mentorship" "Program"
"By" "CampusX"
```
**Output**:
```
Data-Science-Mentorship-Program-started-By-CampusX
```

Concept- [Seperator and End]
"""
def qu1():
    print("Data","Science","Mentorship","Program",sep='-',end='-started-')
    print("By","CampusX")

qu1()


"""### Q2:- Write a program that will convert celsius value to fahrenheit."""

def que2():
    C = float(input("Temperature in Celcius: "))
    F = 32 + (9/5)*C
    print("Temperature in Farenheit:",F,"°F")


"""### Q3:- Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax."""

def que3():
    num1 = int(input("Enter first no. : "))
    num2 = int(input("Enter second no. : "))
    temp = num2
    num2 = num1
    num1 = temp

    print("First no. :",num1,", Second no. :",num2)


"""### Q4:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input."""

def que4():
    print("Enter coordinates of 1st point: \n")
    x1 = float(input("X coordinate of 1st point: "))
    y1 = float(input("Y coordinate of 1st point: "))

    print("Enter coordinates of 2nd point: \n")
    x2 = float(input("X coordinate of 2nd point: "))
    y2 = float(input("Y coordinate of 2nd point: "))

    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
    print(round(distance,2))


"""### Q5:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user."""

def que5():
    p = float(input("Enter principle amount: "))
    i = float(input("Enter intrest rate: "))
    t = float(input("Enter time period: "))

    simple_intrest = (p*i*t)/100
    print(simple_intrest) 


"""### Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.

For example:
Input:
heads -> 4
legs -> 12
<br>
Output:
dogs -> 2
chicken -> 2

"""

def que6():
    heads = int(input("Enter no. of heads: "))
    legs = int(input("Enter no. of legs: "))

    if(legs%2 != 0):
        print("Invalid Input!")
        return 1

# Idea to solve the question is using algebra , 
# x + y = heads
# 4x + 2y = legs
# solve for x and y 

    dogs = int((legs - heads)/3)
    print("No. of dogs :",dogs)
    print("No. of chicken :",heads-dogs)


"""### Q7:- Write a program to find the sum of squares of first n natural numbers where n will be provided by the user."""

def que7():
    n = int(input("Enter integer n: "))
    sum = 0
    for i in range(n+1):
        sum += i*i

    print(sum)


"""### Q8:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user."""

def que8():
    a_0 = int(input("Enter first term: "))
    a_1 = int(input("Enter second term: "))
    d = a_1 - a_0
    n = int(input("Enter the term to find: "))

    a_n = a_0 + (n-1)*d
    print("Nth term:",a_n)

"""### Q9:- Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user."""

def que9():
    n1 = int(input("Enter numerator of first fraction: "))
    d1 = int(input("Enter denominator of first fraction: "))
    
    n2 = int(input("Enter numerator of second fraction: "))
    d2 = int(input("Enter denominator of second fraction: "))

    nr = n1*d2 + n2*d1
    dr = d1*d2

    print(f"sum of the factions: {nr}/{dr}",)

"""### Q10:- Given the height, width and breadth of a milk tank, 
you have to find out how many glasses of milk can be obtained? 
Assume all the inputs are provided by the user.

Input:<br>
Dimensions of the milk tank<br>
H = 20cm, L = 20cm, B = 20cm
<br><br>
Dimensions of the glass<br>
h = 3cm, r = 1cm
"""

def que10():
    ht = int(input("Enter height of the milk tank: "))
    wt = int(input("Enter width of the milk tank: "))
    lt= int(input("Enter length of the milk tank: "))

    hg = int(input("Enter height of the milk glass: "))
    rg = int(input("Enter radius of the milk glass: "))

    volt = ht * wt * lt
    volg = 3.14 * rg*rg*hg

    result = int(volt/volg)
    print("No. of glases of milk:",result)


