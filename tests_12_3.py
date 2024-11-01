import unittest

# Декоратор для пропуска тестов, если is_frozen = True
def skip_frozen(func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_frozen
    def test_run(self):
        self.assertEqual(1 + 1, 2)

    @skip_frozen
    def test_walk(self):
        self.assertEqual(2 + 2, 4)

    @skip_frozen
    def test_challenge(self):
        self.assertEqual(3 + 3, 6)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_frozen
    def test_first_tournament(self):
        self.assertEqual(4 + 4, 8)

    @skip_frozen
    def test_second_tournament(self):
        self.assertEqual(5 + 5, 10)

    @skip_frozen
    def test_third_tournament(self):
        self.assertEqual(6 + 6, 12)

if __name__ == '__main__':
    unittest.main()