# def divisors(num):
    # divisors = []
    # for i in range (1, num + 1):
    #     if num % i == 0:
    #          divisors.append(i)
    # return divisors

# RETO ################################################################

def divisors(num):

    try:
        
        
        divisors2 = [i  for i in range (1, num + 1) if num % i == 0]
        if divisors2 == []:
           raise ValueError("Debes poner un numero positivo") 
        return divisors2
    
    except ValueError as ve :
        print(ve)
        return False
    
##############################################################

def run():
    try:
        num = int(input("Ingresa un numero: "))
        print(divisors(num))
        print("Termino mi programa")
    except ValueError:
        print("Debes ingresar un numero")




if __name__ == "__main__":
    run()