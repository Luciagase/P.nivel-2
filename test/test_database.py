import database as db
import unittest

class TestDatabase(unittest.TestCase):

    def test_crear_puntos(self):#Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.
        puntoA = db.Punto(2, 3)
        self.assertEqual(puntoA.x, 2)
        self.assertEqual(puntoA.y, 3)
        puntoB = db.Punto(5, 5)
        self.assertEqual(puntoB.x, 5)
        self.assertEqual(puntoB.y, 5)
        puntoC = db.Punto(-3, -1)
        self.assertEqual(puntoC.x, -3)
        self.assertEqual(puntoC.y, -1)
        puntoD = db.Punto(0, 0)
        self.assertEqual(puntoD.x, 0)
        self.assertEqual(puntoD.y, 0)
    
    def test_cuadrantes(self):#Consulta a que cuadrante pertenecen el punto A, C y D.
        puntoA = db.Punto(2, 3)
        self.assertEqual(puntoA.cuadrante(), "El punto se sitúa en el primer cuadrante")
        puntoC = db.Punto(-3, -1)
        self.assertEqual(puntoC.cuadrante(), "El punto se sitúa en el tercer cuadrante")
        puntoD = db.Punto(0, 0)
        self.assertEqual(puntoD.cuadrante(), "El punto se está sobre el origen")
    
    def test_vector(self):
        puntoA = db.Punto(2, 3)
        puntoB = db.Punto(5, 5)
        self.assertEqual(puntoA.vector(puntoB), "El vestor es: (3, 2)")

    def test_distancia(self):
        puntoA = db.Punto(2, 3)
        puntoB = db.Punto(5, 5)
        self.assertEqual(puntoA.distancia(puntoB), 3.605551275463989)

    def test_rectangulo(self):
        puntoA = db.Punto(2, 3)
        puntoB = db.Punto(5, 5)
        rectangulo = db.Rectangulo(puntoA, puntoB)
        self.assertEqual(rectangulo.base(), 3)
        self.assertEqual(rectangulo.altura(), 2)
        self.assertEqual(rectangulo.area(), 6)


