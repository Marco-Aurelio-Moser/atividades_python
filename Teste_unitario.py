import unittest

from exerciciosbasicospython import *

class TesteCompleto(unittest.TestCase):
    #def testar_se_numero_eh_par(self):
     #   numero_a_ser_testado = 14
     #   self.assertTrue(numero_a_ser_testado % 2 == 0)

   # def testar_se_numero_eh_impar(self):
       # numero_a_ser_testado = 11
       # self.assertTrue(numero_a_ser_testado % 2 == 1)

    #def testar_conta(self):
       # resultado_conta = 10 + 5 
       # self.assertEqual(resultado_conta, 15)

   # def testar_classificar_faixa_etaria(self):
       # self.assertEqual(classificar_faixa_etaria(10), 'Criança')
       # self.assertEqual(classificar_faixa_etaria(15), 'Adolescente')
       # self.assertEqual(classificar_faixa_etaria(25), 'Adulto')
       # self.assertEqual(classificar_faixa_etaria(-5), 'Idade inválida')
       # self.assertEqual(classificar_faixa_etaria(150), 'Idade inválida')

#def testar_comparar_dois_numeros(self):
  #      self.assertEqual(comparar_dois_numeros(10, 5), '10 é maior que 5')
 #       self.assertEqual(comparar_dois_numeros(5, 10), '5 é menor que 10')
  #      self.assertEqual(comparar_dois_numeros(7, 7), '7 é igual a 7')

    def testar_verificar_vogal_ou_consoante(self):
        self.assertEqual(verificar_vogal_ou_consoante('a'), 'A letra digitada é uma vogal.')
        self.assertEqual(verificar_vogal_ou_consoante('b'), 'A letra digitada é uma consoante.')
        self.assertEqual(verificar_vogal_ou_consoante('E'), 'A letra digitada é uma vogal.')
        self.assertEqual(verificar_vogal_ou_consoante('Z'), 'A letra digitada é uma consoante.')

if __name__ == "__main__":
    unittest.main()
