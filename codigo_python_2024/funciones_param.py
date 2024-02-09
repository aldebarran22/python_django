"""
Definición de parámetros en la entrada de una función
"""
def funcion(ob1, ob2, op1=1, op2=2, *args, **kwargs):
    print('obligatorios: ', ob1, ob2)
    print('opcionales: ', op1, op2)
    print('args: ', args)
    print('kwargs: ', kwargs)
    print()

if __name__ == '__main__':
    funcion(10,20)
    funcion(1,2,3,4)
    funcion(10,20, op2=200)
    funcion(1,2,3,4,5,6,7,8, x=-1, y=-2)

    

