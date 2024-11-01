import unittest
from unittest import TextTestRunner

# Импортируем тестовые классы
from tests_12_3 import RunnerTest, TournamentTest

# Создаем TestSuite
suite = unittest.TestSuite()

# Добавляем тесты в TestSuite
suite.addTest(unittest.makeSuite(RunnerTest))
suite.addTest(unittest.makeSuite(TournamentTest))

# Создаем объект TextTestRunner с verbosity=2
runner = TextTestRunner(verbosity=2)

# Запускаем TestSuite
runner.run(suite)