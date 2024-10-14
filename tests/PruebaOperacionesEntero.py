import unittest
from src.OperacionesEntero import OperacionesEntero

class MyTestCase(unittest.TestCase):

    def setUp(self):
        operaciones = OperacionesEntero()
    def tearDown(self):
        operaciones = None

    def test_suma_numerosFlotantes_retornaSuma(self):
        #Arrange
        operaciones = OperacionesEntero()
        sumando1 = 10.5
        sumando2 = 20.5
        resultadoEsperado = 31

        #Do
        resultadoActual = operaciones.suma(sumando1,sumando2)

        #Assert
        self.assertEqual(resultadoEsperado, resultadoActual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
