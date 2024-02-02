"""
Pruebas con POO
"""

class Persona():
    """
    Implementación de la clase Persona
    """
    contador=0

    def __init__(self, nombre="",edad=0, altura=0.0):
        self.nombre=nombre
        self.edad=edad
        self.altura=altura
        Persona.contador += 1

    def cumple(self):
        self.edad += 1

    def hablar(self, otro=None):
        if not otro:
            print(self.nombre,'habla solo')
        else:
            print(self.nombre,'y',otro.nombre,'están hablando')

    def __lt__(self, otro):
        return self.edad < otro.edad
    
    def __eq2__(self, otro):
        return self.nombre == otro.nombre and \
        self.edad == otro.edad and self.altura == otro.altura

    def __eq__(self, otro):
        if type(self) != type(otro):
            return False
        else:
            L1 = list(self.__dict__.values())
            L2 = list(otro.__dict__.values())
            return L1 == L2

    def __eq3__(self, otro):
        if type(self) != type(otro):
            return False
        else:
            self_dict = vars(self) # self.__dict__
            otro_dict = vars(otro)
            for k in self_dict:
                if self_dict[k] != otro_dict[k]:
                   return False
            return True

    def __str__(self):
        return " ".join([str(i) for i in self.__dict__.values()])
        #return self.nombre + " " + str(self.edad) + " " + str(self.altura)
    
    def __repr__(self):
        return str(self)
    
    def __del__(self):
        print('Se elimina: ', self.nombre)
        Persona.contador -= 1

class Guia(Persona):

    def __init__(self, nombre="", edad=0, altura=0, ambito='', idiomas=[]):
        #super().__init__(nombre, edad, altura)
        Persona.__init__(self, nombre, edad, altura)

        self.ambito = ambito
        self.idiomas = idiomas

    def __str__(self):
        return Persona.__str__(self)+ " "+self.ambito + " " + \
        ",".join(self.idiomas)
    
    def __eq__(self, otro):
        self.idiomas.sort()
        otro.idiomas.sort()
        return super().__eq__(otro) and self.ambito == otro.ambito \
        and self.idiomas == otro.idiomas
    
    def hablar(self, otro=None):
        if not otro:
            print(self.nombre,'habla solo')
        else:
            c1 = set(self.idiomas)
            c2 = set(otro.idiomas)
            comun = c1 & c2
            if len(comun) == 0:
                print('no hay idioma en común')
            else:
                print('Pueden hablar en : ', comun)


def testGuia():
    g1 = Guia('Pedro',34, 1.77, 'N', ['inglés','Francés'])
    g2 = Guia('Sara',44, 1.79, 'I', ['Italiano','Alemán'])
    g3 = Guia('Sara',44, 1.49, 'I', ['Alemán','Italiano','Inglés'])
    print(g1)
    g1.cumple()
    print(g1)
    g1.hablar(g2)
    p1 = Guia('Jose',14, 1.99)
    L = [g1,p1,g2]
    # Ordenación por defecto: operador < con la edad
    L.sort(reverse=True)
    print(L)
    # Ordenar ASC por la altura:
    L.sort(key=lambda obj : obj.altura)
    print(L)
    # Ordenar DESC por el nombre:
    L.sort(key=lambda obj : obj.nombre, reverse=True)
    print(L)
    print('g1==g2', g1==g2)
    print('g2==g3', g2==g3)

def testPersona():
    print("Num personas: ", Persona.contador)
    p1 = Persona("Eva",45, 1.8)
    p2 = Persona("Eva",45, 1.8)
    p3 = Persona("Jose",25, 1.7)

    print('p1', p1)
    print('p2', p2)

    if p1 == p2:
        print('iguales')
    else:
        print('distintos')

    print("Num personas: ", Persona.contador)
    L = [p1, p2, Persona("Jorge", 33, 1.8)]
    print("Num personas: ", Persona.contador)
    del(p3)
    print("Num personas: ", Persona.contador)

    print(L)
    for p in L:
        print(p)
    p1.hablar()
    p2.hablar(p1)

    print(p1)
    p1.cumple()
    print(p1)
    p2.cumple()
    print(p2)
    print(p2.apellido)
    print(p1.apellido)
    p1.apellido="Gomez"
    print(p2.apellido)
    print(p1.apellido)
    print(Persona.apellido)
    p1.telefono = 600450540
    print(p2.__dict__)
    print(p1.__dict__)


    """
    print(str(p1))
    print(p1.__str__())
    print(p1.nombre)
    """

testGuia()