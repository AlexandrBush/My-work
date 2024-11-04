import logging
import unittest
from runner import Runner, Tournament

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='UTF-8',
    format='%(asctime)s | %(levelname)s | %(message)s'
)

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner("John", -1)  # Передаем отрицательное значение в speed
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            runner = Runner(123)  # Передаем что-то кроме строки в name
            runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner")

    def test_run_valid(self):
        try:
            runner = Runner("Alice", 10)  # Передаем корректные данные
            runner.run()
            self.assertEqual(runner.distance, 20)
            logging.info('"test_run_valid" выполнен успешно')
        except Exception as e:
            logging.error(f"Ошибка в 'test_run_valid': {e}")

    def test_walk_valid(self):
        try:
            runner = Runner("Bob", 5)  # Передаем корректные данные
            runner.walk()
            self.assertEqual(runner.distance, 5)
            logging.info('"test_walk_valid" выполнен успешно')
        except Exception as e:
            logging.error(f"Ошибка в 'test_walk_valid': {e}")

class TournamentTest(unittest.TestCase):
    def test_tournament_start(self):
        try:
            runner1 = Runner("Alice", 10)
            runner2 = Runner("Bob", 5)
            tournament = Tournament(50, runner1, runner2)
            finishers = tournament.start()
            self.assertEqual(len(finishers), 2)
            self.assertEqual(finishers[1].name, "Alice")
            self.assertEqual(finishers[2].name, "Bob")
            logging.info('"test_tournament_start" выполнен успешно')
        except Exception as e:
            logging.error(f"Ошибка в 'test_tournament_start': {e}")

    def test_tournament_start_no_finishers(self):
        try:
            runner1 = Runner("Alice", 1)
            runner2 = Runner("Bob", 1)
            tournament = Tournament(100, runner1, runner2)
            finishers = tournament.start()
            self.assertEqual(len(finishers), 0)
            logging.info('"test_tournament_start_no_finishers" выполнен успешно')
        except Exception as e:
            logging.error(f"Ошибка в 'test_tournament_start_no_finishers': {e}")

if __name__ == "__main__":
    unittest.main()