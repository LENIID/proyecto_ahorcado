import random
import os
import time



def read():

    num = int(input("bienvenido al juego AHORCADO\n presiona 1 para jugar"))
    assert num == 1, "xd"  
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        words=[line for line in f]
        word1= random.choice(words)
        longuitud = len(word1)
        longuitud= longuitud -1
        word2 = [i for i in word1 ]
        del word2[longuitud]
        guion23 = list("_" * longuitud)
        
       
        time.sleep(1) 
        
        os.system("cls")
         
        box22 = 2

        LIMITE = 0
        vidas = longuitud + 2
        while box22 != 1:
         box22=box22
         box22 = guion23.count("_")
         if vidas <= LIMITE:
            break
         print(" ¡Adivina la palabra!\n vidas:" + str(vidas) )
         print(guion23)
         print(word2)
         letra=input("Escribe una letra : ")
         assert letra.isalpha, "debes ingresar una letra"
         box = word2.count(letra)
        #  if vidas <= LIMITE:
        #     break
         if box == 0:
            vidas -=1
            os.system("cls")
            continue
         elif box > 1:
            
            while box!= 0:
             box2 = word2.index(letra)
             box24 = word2.index(letra) 
             box2 = box2 +1
             guion23.insert(box2, letra)
             box2 = box2 -1
             del guion23[box2]
             guion23 = guion23
             del word2[box24]
             word2.insert(box24, "_")
             box -= 1
             box24 = 0
             box24 = word2.index(letra)
             box24 = box24 + 1 
             guion23.insert(box24, letra)
             box24 = box24 - 1
             del guion23[box24]
             box24 = 0 
             box24 = word2.index(letra)
             del word2[box24]
             word2.insert(box24, "_")
             box -= 1
             os.system("cls")

         elif box == 1:
            box2 = word2.index(letra)
            box24 = word2.index(letra)
            box2 = box2 +1
            guion23.insert(box2, letra)
            box2 = box2 -1
            del guion23[box2]
            guion23 = guion23 
            os.system("cls")
    os.system("cls")
    if box22 <=1:
       print("Felicidades GANASTE!!!\n La palabra era: " + word1)
       time.sleep(2)
       os.system("cls")
       write()
    elif vidas <=LIMITE:
        print("========PERDISTE============\n La palabra era: " + word1)
    

       


def game():
    pass







def write():
    with open("./archivos/registro.txt", "w", encoding="utf-8") as f:
        name = input("Escribe tu nombre: ")
        emal = input("escribe tu correo electronico: ")
        jugador = name + emal
        f.write(jugador)
        f.write("\n")
        print("Has sido agregado a la base de datos")
        print("Termino mi programa :)")




    











# def menu():
#     # read()
    
#         num = input("""                         ----💲💲BIENVENIDO AL JUEGO💲💲 ------ \n
    
#          ###     #    #    #####    ####    #####     ###     #####     ####
#         #   #    #    #   #     #   #   #  #         #   #    #    #   #    #
#        ######    ######  #       #  ####   #        ######    #     # #      #
#       #      #   #    #   #     #   #   #  #       #      #   #    #   #    #
#      #        #  #    #    #####    #    #  ##### #        #  #####     #### \n

#                          INSERTA -- 1 -- PARA JUGAR :)
#     """)


#         # num = (input(""))
#         box = num.count ("-")          
#         assert num != "", "No puedes ingresar un espacio vacio"
#         assert num != " ", "No puedes ingresar un espacio vacio"
#         assert num != "  ", "No puedes ingresar un espacio vacio"
#         assert num != "   ", "No puedes ingresar un espacio vacio"
#         assert num != "    ", "No puedes ingresar un espacio vacio"
#         assert box == 0, "Escribe un numero positivo"
#         assert num.isnumeric(), "debes ingresar solo numeros"
#         # return num
#         print(read(num))
        




def run():
    read()
    
    
    # print(game(read))
    # menu()
    # print(read(num))
    # game()
    # print(read)
    



if __name__ == "__main__":
    run()