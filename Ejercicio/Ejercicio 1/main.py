import gramatica as grammar

while(True):
    print('Ingrese una operación')
    entrada = input()
    response = grammar.parse(entrada)
    print('Salida:')
    print(response.c3d)

    print('¿Terminar ejecución? (y|n)')
    if (input() == 'y' or input() == 'Y'): break