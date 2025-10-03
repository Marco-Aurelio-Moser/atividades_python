import unittest

from exerciciosbasicos import *

class TesteCompleto(unittest.TestCase):
    def testar_se_numero_eh_par(self):
        numero_a_ser_testado = 14
        self.assertTrue(numero_a_ser_testado % 2 == 0)

    def testar_se_numero_eh_impar(self):
        numero_a_ser_testado = 11
        self.assertTrue(numero_a_ser_testado % 2 == 1)

    def testar_conta(self):
        resultado_conta = 10 + 5 
        self.assertEqual(resultado_conta, 15)

if __name__ == "__main__":
    unittest.main()