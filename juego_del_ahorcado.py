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
        word2 = [i for i in word1]
        word2.pop(longuitud)
        word3 = word2
        guion23 = list("_" * longuitud)
        word2 = tuple(word2)
        
       
        
        
        time.sleep(1) 
        
        os.system("cls")
         
        box22 = 1
        LIMITE = 1
        vidas = longuitud + 2
        while box22 != 0:
         box22=box22
         box22 = guion23.count("_")
         print(" ¡Adivina la palabra!\n vidas:" + str(vidas) )
         print(guion23)
         letra=input("Escribe una letra : ")
         assert letra.isalpha, "debes ingresar una letra"
        #  assert len(letra)==1,"Solo puedes poner 1 letra"
         box = word2.count(letra)
         if vidas <= LIMITE:
            break
         elif box == 0:
            vidas -=1
            os.system("cls")
            continue
         elif box == 2:
            box2 = word2.index(letra)
            box24 = word3.index(letra) 
            box2 = box2 +1
            guion23.insert(box2, letra)
            box2 = box2 -1
            guion23.pop(box2)
            guion23 = guion23
            word3.pop(box24)
            word3.insert(box24, "_")
            box24 = 0
            box24 = word3.index(letra)
            box24 = box24 + 1 
            guion23.insert(box24, letra)
            box24 = box24 - 1
            guion23.pop(box24)
            box24 = 0 
            box24 = word3.index(letra)
            word3.pop(box24)
            word3.insert(box24, "_")
            os.system("cls")

         elif box == 1:
            box2 = word2.index(letra)
            box24 = word3.index(letra)
            box2 = box2 +1
            guion23.insert(box2, letra)
            box2 = box2 -1
            guion23.pop(box2)
            guion23 = guion23 
            os.system("cls")
    os.system("cls")
    if box22 == 0:
       print("Felicidades GANASTE!!!\n La palabra era: " + word1)
    elif vidas <=LIMITE:
        print("========PERDISTE============\n La palabra era: " + word1)
    

       


def game():
    pass







def write():
    pass 











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