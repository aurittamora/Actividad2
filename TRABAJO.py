import time
import os
os.system('cls')

ahorcado = {1:'''
      +---+
      |   |
          |
          |
          |
          |
    =========''',2:'''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''',3:'''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''',4:'''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''',5:'''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''',6:'''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''',7:'''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''',8:'''
      +---+
      |   |
      O   |
          |
     /|\  |
     / \  |
    ========= MUERTO!'''

}



abecedario = ['a', 'b','c', 'd','e','f','g','h', 'i', 'j','k','l','m', 'n', 'ñ', 'o','p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def salto():
    print('')
def numLetras():
    numero_letras = 0
    for letra in frase:
        if letra != ' ':
            numero_letras += 1
    return numero_letras



print('Vamos a jugar al ahorcado.')
pregunta_inicial = input('¿Quieres jugar?:\t').lower()

while True:
    if pregunta_inicial == 'si' or pregunta_inicial == 's':
        print('')
        break
    elif pregunta_inicial == 'no' or pregunta_inicial == 'n':
        print('Adiós, jugaremos otro dia')
        exit()
    else:
        os.system('cls')
        print('Tu respuesta no es válida.')
        print('')
        pregunta_inicial = input('¿Quieres jugar?:\t').lower()

frase = input('Introduce una frase:\t').lower()

while True:
    long = len(frase)
    a = 0
    for i in frase:
        if i in abecedario or i == ' ':
            a += 1
    if a == long:
        break
    else:
        os.system('cls')
        print('En la frase introducida hay un valor que no pertenece al abecedario')
        salto()
        frase = input('Introduce una frase:\t').lower()

salto()
salto()
salto()
print('Pásale el ordenador a tu compañero para que intente adivinar tu frase.')
print('Espera a que se borre la pantalla')

time.sleep(2.5)
os.system('cls')

print(f'La frase que tienes que adivinar tiene {numLetras()} letras.')

intentos = 0
intentos = int(intentos)
letras_ocultas= []
letras_vistas = []
letras_borradas = []

for i in frase:
    letras_vistas.append(i)

for hueco in frase:
    if hueco == ' ':
        letras_ocultas.append('  ')
    else:
        letras_ocultas.append(' _')

print("".join(letras_ocultas))
salto()



while True:
    if intentos < 8:
        if "".join(letras_ocultas) == "".join(letras_vistas):
            os.system('cls')
            var_ganador = 'Has ganado!!!'
            lista_var = []
            for l in var_ganador:
                os.system('cls')
                salto()
                lista_var.append(l)
                print("".join(lista_var))
                time.sleep(0.25)
                salto()
            break

        else:
            salto()
            salto()
            ltr = input('Introduce una letra:\t').lower()
            os.system('cls')

            if len(ltr) == 1 and ltr in abecedario:
                for i in range(len(frase)):
                    if letras_vistas[i] == ltr:
                        letras_ocultas[i] = ltr

                abecedario.remove(ltr)
                letras_borradas.append(ltr)

                if ltr not in frase:
                    intentos += 1

                if intentos == 0:
                    print(f'Llevas {intentos} intentos.')
                    salto()
                    print("".join(letras_ocultas))
                    salto()
                    salto()
                    print('¡Sigue asi!')
                    letras_borradas.append(ltr)


                else:
                    print(f'Llevas {intentos} intentos.')
                    print(ahorcado.get(intentos), ' ' ,"".join(letras_ocultas))
                    salto()


            else:
                if len(ltr)== 1:
                    if ltr in letras_borradas:
                        if intentos == 0:
                            print(f'Llevas {intentos} intentos.')
                            salto()
                            print("".join(letras_ocultas))
                            salto()
                            print(f'Ya has introducido la letra {ltr}.')
                            salto()



                        else:
                            print(f'Llevas {intentos} intentos.')
                            salto()
                            print(ahorcado.get(intentos), ' ' ,"".join(letras_ocultas))
                            salto()
                            print(f'Ya has introducido la letra {ltr}.')
                            salto()


                    elif ltr not in letras_borradas and ltr not in abecedario :
                        print(f'Llevas {intentos} intentos.')
                        salto()
                        print(ahorcado.get(intentos), ' ' ,"".join(letras_ocultas))
                        salto()
                        print(f'Los valores introducidos son erroneos.')
                        salto()

                    else:
                        if intentos == 0:
                            print(f'Llevas {intentos} intentos.')
                            salto()
                            print("".join(letras_ocultas))
                            salto()
                            print(f'Ya has introducido la letra {ltr}.')
                            salto()


                        else:
                            print(f'Llevas {intentos} intentos.')
                            salto()
                            print(ahorcado.get(intentos), ' ' ,"".join(letras_ocultas))
                            salto()
                            print(f'Ya has introducido la letra {ltr}.')
                            salto()



                elif len(ltr) > 1:
                    if intentos == 0:
                        print(f'Llevas {intentos} intentos.')
                        salto()
                        print("".join(letras_ocultas))
                        salto()
                        print(f'Los valores introducidos son erroneos.')
                        salto()

                    else:
                        print(f'Llevas {intentos} intentos.')
                        salto()
                        print(ahorcado.get(intentos), ' ' ,"".join(letras_ocultas))
                        salto()
                        print(f'Ya has introducido la letra {ltr}.')
                        salto()

    elif intentos == 0:
        os.system('cls')
        var_ganador = 'Has ganado!!!'
        lista_var = []
        for l in var_ganador:
            os.system('cls')
            salto()
            lista_var.append(l)
            print("".join(lista_var))
            time.sleep(0.25)
            salto()

    else:
        salto()
        var_perdedor = 'Has perdido, la próxima vez será'
        lista_var_per = []
        for l in var_perdedor:
            os.system('cls')
            salto()
            lista_var_per.append(l)
            print("".join(lista_var_per))
            time.sleep(0.25)
            salto()
        os.system('cls')
        print(f'Llevas {intentos} intentos.')
        salto()
        print(ahorcado.get(intentos), ' ', "".join(letras_ocultas))
        salto()
        print(var_perdedor)

        salto()
        break

