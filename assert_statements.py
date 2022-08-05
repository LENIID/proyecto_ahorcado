def divisors(num):
    divisors2 = []
    for i in range (1, num + 1):
         if num % i == 0:
            divisors2.append(i)

      
    return divisors2
    
    # RETO ###################################
def run():
     num = (input("Ingresa un numero: "))
     box = num.count ("-")           
     assert box == 0, "Escribe un numero positivo"
     assert num.isnumeric(), "Debes ingresar un numero"
     print(divisors(int(num)))
     print("Termino mi programa")




if __name__ == "__main__":
    run()