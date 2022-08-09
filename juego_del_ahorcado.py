import paint
import random
import os
import time



def read(num):
    num = int(num)
    assert num == 1, "xd"  
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        words=[line for line in f]
        word1= random.choice(words)
        longuitud = len(word1)
        longuitud= longuitud -1
        word2 = [i for i in word1 ]
        del word2[longuitud]
        guion23 = list("_" * longuitud)
        entrance= "áéíóúñ"
        out = "aeioun"
        change = str.maketrans(entrance, out)
        word999= "".join(word2)
        word999 =word999.translate(change)
        word2.clear()
        word2= [i for i in word999]

        
        

        
       
        time.sleep(1) 
        
        os.system("cls")
         
        box22 = 2
        hangman = paint.picture
        LIMITE = 0
        vidas = longuitud + 2
        puntos = 100
        while box22 != 1:
         box22=box22
         box22 = guion23.count("_")
         if vidas <= LIMITE:
            break
         print(" ¡Adivina la palabra!\n vidas:" + str(vidas) )
         print(hangman)
         print(" ".join(guion23))
         if puntos <= 70:
            hangman=paint.pictures
         letra=input("Escribe una letra : ")
         assert letra.isalpha, "debes ingresar una letra"
         box = word2.count(letra)
         if box == 0:
            vidas -=1
            puntos -=10
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
             if box == 0:
                break
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
       hangman= paint.picturew
       print(hangman)
       print("Felicidades GANASTE!!!\n La palabra era: " + word1)
       print("Tu puntuacion fue " + str(puntos) + " Puntos :)")
       time.sleep(5)
       os.system("cls")
       write(puntos)
    elif vidas <=LIMITE:
        hangman = paint.picturel
        print(hangman)
        print("========PERDISTE============\n La palabra era: " + word1)
        puntos=0
        print("Tu puntuacion fue " + str(puntos) + " Puntos :)")




def write(puntos):
    with open("./archivos/registro.txt", "a", encoding="utf-8") as f:
        name = input("Escribe tu nombre: ")
        puntos =" Puntos: " + str(puntos)
        jugador = name + puntos
        print(puntos)
        print(jugador)
        f.write(jugador)
        f.write("\n")
        print("Has sido agregado a la base de datos")






def menu():
        num = input("""                         ----💲💲BIENVENIDO AL JUEGO💲💲 ------ \n
    
         ###     #    #    #####    ####    #####     ###     #####     ####
        #   #    #    #   #     #   #   #  #         #   #    #    #   #    #
       ######    ######  #       #  ####   #        ######    #     # #      #
      #      #   #    #   #     #   #   #  #       #      #   #    #   #    #
     #        #  #    #    #####    #    #  ##### #        #  #####     #### \n

                         INSERTA -- 1 -- PARA JUGAR :)
    """)

        box = num.count ("-")          
        assert num != "", "No puedes ingresar un espacio vacio"
        assert num != " ", "No puedes ingresar un espacio vacio"
        assert box == 0, "Escribe un numero positivo"
        assert num.isnumeric(), "debes ingresar solo numeros"
        print(read(num))
        




def run():
    menu()
    
    
    
    print("Termino mi programa :)")

    
    



if __name__ == "__main__":
    run()
