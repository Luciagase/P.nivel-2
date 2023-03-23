import math

class Punto: #crear clase punto
    def __init__(self, x=0, y=0):#Añade un método constructor para crear puntos fácilmente
        self.x=x
        self.y=y

    def __str__(self):#Sobreescribe el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)
        return "({},{})".format(self.x, self.y)
    
    def cuadrante(self):#método llamado cuadrante que indique a qué cuadrantepertenece el punto
        if self.x==0 and self.y!=0:
            print("El punto se sitúa sobre el eje Y")
        elif self.x!=0 and self.y==0:
            print("El punto se sitúa sobre el eje X")
        elif self.x==0 and self.y==0:
            print("El punto está sobre el origen")
        elif self.x>0 and self.y>0:
            print("El punto se sitúa en el primer cuadrante")
        elif self.x>0 and self.y<0:
            print("El punto se sitúa en el cuarto cuadrante")
        elif self.x<0 and self.y>0:
            print("El punto se sitúa en el segundo cuadrante")
        elif self.x<0 and self.y<0:
            print("El punto se sitúa en el tercer cuadrante")

        
