# para rodar o teste 'python -m unittest <file.py>'

# Resumo:
# pode-se implementar os testes usando doctest como foi feito em dd_game
# pode-se criar um script que implemente os testes assim como em test_dices.py e test_moves.py.
# por fim, pode-se instalar a biblioteca coverage (pip install coverage)
# >>> coverage run <filename.py>
# >>> coverage report    -> para ver o relatorio de cobertura do teste
# >>> coverage report -m       -> para ver as linhas que não estão testadas
# >>> coverage html          -> gera report em html, em uma pasta no workspace 'htmlcov'(abrir arquivos html)


import unittest
import dice

class DieTests(unittest.TestCase):
    def setUp(self):
        self.d6 = dice.Die(6)
        self.d8 = dice.Die(8)

    def test_creation(self):
        self.assertEqual(self.d6.sides, 6)
        self.assertIn(self.d6.sides, range(1,7))

    def test_add(self):
        self.assertIsInstance(self.d6+self.d8, int)

class RollTests(unittest.TestCase):
    def setUp(self):
        self.hand1 = dice.Roll('1d2')
        self.hand3 = dice.Roll('3d6')

    def test_lowe(self):
        self.assertGreaterEqual(int(self.hand3), 3)

    def test_upper(self):
        self.assertLessEqual(int(self.hand3), 18)

    def test_membership(self):
        test_die = dice.Die(2)
        test_die.value = self.hand1.results[0].value
        self.assertIn(test_die, self.hand1.results)
    
    def test_bad_description(self):
        # se der ValueError, está ok, pois '2b6' é um valor invalido
        with self.assertRaises(ValueError):
            dice.Roll('2b6')
    
    # def test_small_die(self):
    #     # Como não apresenta ValueError, acontece erro de teste, pois '1d2' é um valor valido
    #     with self.assertRaises(ValueError):
    #         dice.Roll('1d2')

    def test_bad_sides(self):
        with self.assertRaises(ValueError):
            dice.Die(1)


if __name__ == "__main__":
    unittest.main()
