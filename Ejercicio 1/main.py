import gramatica as grammar

while(True):
    print('Ingrese una operación')
    entrada = input()
    response = grammar.parse(entrada)
    print('Salida:')
    print(response.c3d)
    print('Etiquetas verdaderas: ')
    print(response.true_label)
    print('Etiquetas falsas: ')
    print(response.false_label)

    print('¿Terminar ejecución? (y|n)')
    if (input() == 'y' or input() == 'Y'): break