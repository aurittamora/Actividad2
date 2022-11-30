import  time
import os

os.system('cls')

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

##funcion para imprimir
def imprimir(x, intentos, frase_oculta):
    print(f'Llevas {intentos} intentos.')
    print(ahorcado.get(intentos), ' ', ''.join(frase_oculta))
    print('')
    print(x)
    print('')

def numLetras():
    numero_letras = 0
    for letra in frase:
        if letra != ' ':
            numero_letras += 1
    return numero_letras
def ganaste():
    var_ganador = 'Has ganado!!!'
    lista_var = []
    for l in var_ganador:
        os.system('cls')
        print(f'Llevas {intentos} intentos.')
        print(ahorcado.get(intentos), ' ', frase)
        print('')
        lista_var.append(l)
        print("".join(lista_var))
        time.sleep(0.25)
        print('')

abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z']

pregunta = input('¿Quieres jugar al ahorcado? si/no:\t').lower()

##Comprobación de la respuesta de pregunta.

while True:
    if pregunta == 'si' or pregunta == 's':
        print('')
        print('¡Empecemos a jugar!')
        break
    elif pregunta == 'no' or pregunta == 'n':
        print('Jugaremos en otro momento.')
        exit()
    else:
        os.system('cls')
        print('Tu respuesta no es valida.')
        print('')
        pregunta = input('¿Quieres jugar al ahorcado? si/no:\t').lower()

## Ya se ha comprobado si quieres jugar o no, como quieres jugar hay que comprobar la que los caracteres de la frase estan en el abecedario
print('')
frase = input('Introduce una frase:\t').lower()

while True:
    i = 0
    for letra in frase:
        if letra == ' ' or letra in abecedario:
            i += 1

    if i == len(frase):
        print('')
        print('Pásale el ordenador a tu compañero para que intente adivinar tu frase.')
        print('Espera a que se borre la pantalla')
        break
    else:
        os.system('cls')
        print('En la frase introducida hay un valor que no pertenece al abecedario')
        print('')
        frase = input('Introduce una frase:\t').lower()

time.sleep(2.5)
os.system('cls')
## ya hemos comprobado las dos primeras condiciones que quieras jugar y que la frase introducida solo tenga valor del abecedario o sea esoacio
## vamos a jugar

intentos = 0
frase_oculta = []
letras_vistas = []
letras_borradas = []

for i in frase:
    letras_vistas.append(i)

for letra in frase:
    if letra in abecedario:
        frase_oculta.append(' _')
    else:
        frase_oculta.append(' ')

print(f'Llevas {intentos} intentos.')
print(ahorcado.get(intentos), ' ',''.join(frase_oculta) )

print('')



while True:

    if ''.join(frase_oculta) == frase:
        ganaste()
        exit()
    else:
        if intentos == 7:
            os.system('cls')
            caso = f'La frase que tenías que adivinar es: {frase} '
            imprimir(caso,intentos, frase_oculta)
            break
        else:
            print('')
            print('')
            var = input('Introduce una letra:\t').lower()
            os.system('cls')
            if len(var) > 1:
                if var == frase:
                    ganaste()
                    exit()
                else:
                    caso = 'Has introducido más de un caracter.'
                    imprimir(caso, intentos, frase_oculta)


            else:
                if var in abecedario:
                    if var in letras_vistas :
                        for j in range(len(frase)):
                            if letras_vistas[j] == var:
                                frase_oculta[j] = var

                        letras_borradas.append(var)
                        abecedario.remove(var)
                        caso = ' '
                        imprimir(caso, intentos, frase_oculta)

                    else:
                        intentos += 1

                        letras_borradas.append(var)
                        abecedario.remove(var)

                        caso = f'La letra {var} no esta en la frase'
                        imprimir(caso, intentos, frase_oculta)

                else:
                    if var in letras_borradas:
                        caso = f'Ya has intoducido la letra {var}'
                        imprimir(caso, intentos, frase_oculta)

                    elif var == ' ':
                        caso = 'No has introducido ningún valor.'
                        imprimir(caso, intentos, frase_oculta)

                    elif var.isdigit() == True:
                        caso = 'Has intoducido un valor numérico.'
                        imprimir(caso, intentos, frase_oculta)

                    else:
                        caso ='Has intoducido un caracter no válido.'
                        imprimir(caso, intentos, frase_oculta)
