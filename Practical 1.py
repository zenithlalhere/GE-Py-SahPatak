listCoeff=[]

def inputCoeff(listCoeff):
    #asking inputs for coefficients of QUadratic Equation - Keeping in mind, General Equation is ax2 + bx + c = 0
    print("Input the cofficients of Quadratic equation under General form ax^2 + bx + c = 0")
    varInput = (input("Use Space between the coefficients"))
    listCoeff = (varInput.split(" "))
    if len(listCoeff) > 3:
        print("Excess Input")
    print(listCoeff)
    return listCoeff


listCoeff = inputCoeff(listCoeff)
#print(listCoeff)
a = int(listCoeff[0])
b = int(listCoeff[1])
c = int(listCoeff[2])

def quadraticFormulae():

    disc = b**2 - 4*a*c

    def solMath():
        sol1 = (-b+(disc)**0.5)/2*a
        sol2 = (-b-(disc)**0.5)/2*a
        print(f"Solutions are {sol1}, {sol2}")
        return sol1, sol2

    
    if disc > 0:
        print("The Equation has 2 real roots")
        solMath()


    elif disc < 0:
        print("The Equation has no real roots")
        

    else:
        print("Equation has two equal real root")
        solMath()

quadraticFormulae()

