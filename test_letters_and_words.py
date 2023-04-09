import unittest
from count_letters_and_words import Count

class TestCountLetters(unittest.TestCase):

    def test_simple(self):
        countLtr = Count()
        result = countLtr.count_letters('a')
        self.assertEqual(result, {'a': 1})

    def test_complex(self):
        countLtr = Count()
        result = countLtr.count_letters('hola')
        self.assertEqual(
            result,
            {
                'h': 1,
                'o': 1,
                'l': 1,
                'a': 1,
            }
        )

    def test_super_complex_I(self):
        countLtr = Count()
        result = countLtr.count_letters('hola chau')
        self.assertEqual(
            result,
            {
                'h': 2,
                'o': 1,
                'l': 1,
                'a': 2,
                ' ': 1,
                'c': 1,
                'u': 1
            }
        )

    def test_super_complex_II(self):
        countLtr = Count()
        result = countLtr.count_letters('Aguante River Plate')
        self.assertEqual(
            result,
            {
                'a': 3,
                'g': 1,
                'u': 1,
                'n': 1,
                't': 2,
                'e': 3,
                'r': 2,
                'i': 1,
                'v': 1,
                ' ': 2,
                'p': 1,
                'l': 1
            }
        )

    def test_super_complex_III(self):
        countLtr = Count()
        result = countLtr.count_letters('La programación es el futuro')
        self.assertEqual(
            result,
            {
                'l': 2,
                'a': 3,
                'p': 1,
                'r': 3,
                'o': 2,
                'g': 1,
                'm': 1,
                'c': 1,
                'i': 1,
                'ó': 1,
                'n': 1,
                ' ': 4,
                'e': 2,
                's': 1,
                'f': 1,
                'u': 2,
                't': 1,
                
            }
        )

    def test_super_complex_IV(self):
        countLtr = Count()
        result = countLtr.count_letters('Hoy juega River')
        self.assertEqual(
            result,
            {
                'h': 1,
                'o': 1,
                'y': 1,
                'j': 1,
                'u': 1,
                'e': 2,
                'g': 1,
                'a': 1,
                'r': 2,
                'i': 1,
                'v': 1,
                ' ': 2
            }
        )

    def test_super_complex_V(self):
        countLtr = Count()
        result = countLtr.count_letters('Chippin in')
        self.assertEqual(
            result,
            {
                'c': 1,
                'h': 1,
                'i': 3,
                'p': 2,
                'n': 2,
                ' ': 1
            }
        )
    def test_super_complex_VI(self):
        countLtr = Count()
        result = countLtr.count_letters('Never fade away')
        self.assertEqual(
            result,
            {
                'n': 1,
                'e': 3,
                'v': 1,
                'r': 1,
                ' ': 2,
                'f': 1,
                'a': 3,
                'd': 1,
                'w': 1,
                'y': 1

            }
        )

    def test_super_complex_VII(self):
        countLtr = Count()
        result = countLtr.count_letters('A like supreme')
        self.assertEqual(
            result,
            {
                'a': 1,
                ' ': 2,
                'l': 1,
                'i': 1,
                'k': 1,
                'e': 3,
                's': 1,
                'u': 1,
                'p': 1,
                'r': 1,
                'm': 1

            }
        )

    def test_super_complex_VII(self):
        countLtr = Count()
        result = countLtr.count_letters('I really want to stay at your house')
        self.assertEqual(
            result,
            {
                'i': 1,
                ' ': 7,
                'r': 2,
                'e': 2,
                'a': 4,
                'l': 2,
                'y': 3,
                'w': 1,
                'n': 1,
                't': 4,
                'o': 3,
                's': 2,
                'h': 1,
                'u': 2

            }
        )


class TestCountWords(unittest.TestCase):

    def test_simple(self):
        countWrd = Count()
        result = countWrd.count_words('hola')
        self.assertEqual(result, {'hola': 1})

    def testCountWords_I(self):
        countWrd = Count()
        result = countWrd.count_words('hola mundo')
        self.assertEqual(result, {'hola': 1, 'mundo': 1})

    def testCountWords_II(self):
        countWrd = Count()
        result = countWrd.count_words('Chippin in')
        self.assertEqual(result, {'Chippin': 1, 'in': 1})

    def testCountWords_III(self):
        countWrd = Count()
        result = countWrd.count_words('ser o no ser')
        self.assertEqual(result, {'ser': 2, 'o': 1, 'no': 1})
    
    def testCountWords_IV(self):
        countWrd = Count()
        result = countWrd.count_words('Vanpiro esiten')
        self.assertEqual(result, {'Vanpiro': 1, 'esiten': 1})

    def testCountWords_V(self):
        countWrd = Count()
        result = countWrd.count_words('I really want to stay at your house')
        self.assertEqual(result, {'I': 1, 'really': 1, 'want': 1, 'to': 1, 'stay': 1, 'at': 1, 'your': 1, 'house': 1})

    def testCountWords_VI(self):
        countWrd = Count()
        result = countWrd.count_words('El dinero es dinero, el dinero es dinero, aprende algo dinero')
        self.assertEqual(result, {'El': 1, 'dinero': 3, 'es': 2, 'el': 1, 'dinero,': 2, 'aprende': 1, 'algo': 1 })

    def testCountWords_VII(self):
        countWrd = Count()
        result = countWrd.count_words('Las cátedras virtuales están caídas justo ahora (True)')
        self.assertEqual(result, {
            'Las': 1, 'cátedras': 1, 'virtuales': 1, 'están': 1, 'caídas': 1, 'justo': 1, 'ahora': 1, '(True)': 1
            })
    
    def testCountWords_VIII(self):
        countWrd = Count()
        result = countWrd.count_words('SiNoHayEspaciosTomaAbsolutamenteTodoJunto')
        self.assertEqual(result, {
            'SiNoHayEspaciosTomaAbsolutamenteTodoJunto':1
            })

if __name__ == '__main__':
    unittest.main()