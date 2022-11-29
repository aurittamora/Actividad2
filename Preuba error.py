
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
def imprimir(x, intentos, frase_oculta):
    print(f'Llevas {intentos} intentos.')
    print(ahorcado.get(intentos), ' ', ''.join(frase_oculta))
    print('')
    print(x)
    print('')


intentos = 7
frase_oculta = ['a','u','r','a']
caso = 'Has intoducido un caracter no válido.'
imprimir(caso,intentos, frase_oculta)