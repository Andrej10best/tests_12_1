import unittest
from unittest import TestCase
from code import Runner


class RunnerTest(TestCase):

    def test_walk(self):
        self.people_1 = Runner('Max')
        for _ in range(10):
            self.people_1.walk()
        self.assertEqual(self.people_1.distance, 50)

    def test_run(self):
        self.people_2 = Runner('Den')
        for _ in range(10):
            self.people_2.run()
        self.assertEqual(self.people_2.distance, 100)

    def test_challenge(self):
        self.people_3 = Runner('Rick')
        self.people_4 = Runner('Morty')
        for _ in range(10):
            self.people_3.run()
        for _ in range(10):
            self.people_4.walk()
        self.assertNotEqual(self.people_3.distance, self.people_4.distance)


if __name__ == '__main__':
    unittest.main()
