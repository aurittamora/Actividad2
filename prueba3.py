import time
import os

os.system('cls')

##Definición de diccionario a cada valor se le asigna un dibujo del ahorcado

ahorcado = {0: '''
      +---+
      |   |
          |
          |
          |
          |
    =========''', 1: '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', 2: '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', 3: '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', 4: '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', 5: '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', 6: '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''', 7: '''
      +---+
      |   |
      O   |
          |
     /|\  |
     / \  |
    ========= MUERTO!'''
            }


## Aqui estarán todas las def que se utilizarán a lo largo del programa
def salto():
    print('')


def numLetras():
    numero_letras = 0
    for letra in frase:
        if letra != ' ':
            numero_letras += 1
    return numero_letras


abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z']

pregunta_inicial = input('¿Quieres jugar al ahorcado?:\t').lower()

while True:
    if pregunta_inicial == 'si' or pregunta_inicial == 's':
        salto()
        print('¡Empecemos a jugar!')
        break
    elif pregunta_inicial == 'no' or pregunta_inicial == 'n':
        salto()
        print('Adiós, jugaremos otro dia')
        exit()
    else:
        os.system('cls')
        print('Tu respuesta no es válida.')
        salto()
        pregunta_inicial = input('¿Quieres jugar?:\t').lower()

salto()
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
print('Pásale el ordenador a tu compañero para que intente adivinar tu frase.')
print('Espera a que se borre la pantalla')

time.sleep(2.5)
os.system('cls')

##Desde aquí vamos a adivinar la palabra escrita

print(f'La frase que tienes que adivinar tiene {numLetras()} letras.')

##variables

intentos = 0
intentos = int(intentos)
letras_ocultas = []
letras_vistas = []
letras_borradas = []

for i in frase:
    letras_vistas.append(i)

for hueco in frase:
    if hueco == ' ':
        letras_ocultas.append('  ')
    else:
        letras_ocultas.append(' _')

print(ahorcado.get(intentos), ' ', "".join(letras_ocultas))
salto()

while True:
    salto()
    salto()
    ltr = input('Introduce una letra:\t').lower()
    os.system('cls')
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
        if intentos < 7:
            if len(ltr) > 1:
                print(f'Llavas {intentos} intentos.')
                print(ahorcado.get(intentos))
                salto()
                print('Has introducido más de un caracter')
            ## tiene más de un caracter
            else:
                if ltr in abecedario:
                    for i in range(len(frase)):
                        if letras_vistas[i] == ltr:
                            letras_ocultas[i] = ltr

                    if ltr not in frase:
                        intentos += 1

                    os.system('cls')
                    print(f'Llevas {intentos} intentos.')
                    salto()
                    print(ahorcado.get(intentos), ' ', "".join(letras_ocultas))

                    abecedario.remove(ltr)
                    letras_borradas.append(ltr)

                elif ltr in letras_borradas:

                    os.system('cls')
                    print(f'Llevas {intentos} intentos.')
                    salto()
                    print(ahorcado.get(intentos), ' ', "".join(letras_ocultas))
                    salto()
                    print(f'Ya has introducido la letra {ltr}.')

                elif ltr == ' ':

                    os.system('cls')
                    print(f'Llevas {intentos} intentos.')
                    salto()
                    print(ahorcado.get(intentos), ' ', "".join(letras_ocultas))
                    salto()
                    print(f'No has introducido ningún valor.')


                elif ltr.isdigit() == True:

                    os.system('cls')
                    print(f'Llevas {intentos} intentos.')
                    salto()
                    print(ahorcado.get(intentos), ' ', "".join(letras_ocultas))
                    salto()
                    print(f'Los valores numéricos no están permitidos.')


                else:

                    os.system('cls')
                    print(f'Llevas {intentos} intentos.')
                    salto()
                    print(ahorcado.get(intentos), "".join(letras_ocultas))
                    salto()
                    print(f'Has introducido un caracter erróneo.')


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
                break
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





