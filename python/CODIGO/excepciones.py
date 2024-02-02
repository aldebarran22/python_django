"""
Captura de excepciones en Python
"""

def test1():
    L = [1,2,3]
    try:
        print(L)
        #print(10 / 0) Aborta el script porque no captura ZeroDivisionError
        print(L[10])
        print(L)
    except IndexError as e:
        print("ERROR",e)

def test2():
    # Capturar varios tipos de excepción
    L = [1,2,3]
    try:
        print(L)
        print(10 / 0) 
        print(L[10])
        print(L)
    except IndexError as e:
        print("ERROR",e)

    except ZeroDivisionError as e:
        print('ERROR', e)

def test3():
    # Capturar varios tipos de excepción y agruparlas
    L = [1,2,3]
    try:
        print(L)
        print(L[10])
        print(10 / 0)         
        print(L)
    except (IndexError,ZeroDivisionError) as e:
        # Para imprimir el nombre de la clase utilizamos la prop. __class__
        print("ERROR",e.__class__.__name__, e)


def test4():
    # Capturar agrupando con la super clase: Exception
    L = [1,2,3]
    try:
        print(L)
        print(L[10])
        print(10 / 0)         
        print(L)
    except Exception as e:
        print("ERROR",e.__class__.__name__, e)

def test5():
    # Abrir un fichero, leerlo y liberar recursos (cerrar el fichero)
    # Si el fichero NO existe no lo intenta cerrar
    # Si el fichero existe lo cierra en finally.
    f=None
    try:
        f = open('ficheros/fichero1.csv')
        txt = f.read()
        return txt               
    except Exception as e:
        print('Error: ', e)
    finally:
        if f!=None: f.close()

def test6(n):
    # Lanzar una excepción:
    if not (10 <= n <= 20):
        raise ValueError(f'{n} no se encuentra entre 10 y 20')
    else:
        print('Valor correcto: ', n)

if __name__ == '__main__':
    try:
        print(__name__)
        test6(-12)
    except Exception as e:
        print('ERROR: ' , e)