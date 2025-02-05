from leve import normalized_dist, closest_str
import unittest


class TestLeve(unittest.TestCase):
    def test_correct_shortest(self):
        self.assertEqual(
            closest_str("add", ["daddy", "muil", "maddi", "shady"]),
            "daddy",
            "It should be daddy",
        )

    def test_normalized_score(self):
        self.assertGreaterEqual(
            normalized_dist("add", "daddy"),
            0,
            "It should be greater than or equal to 0",
        )
        self.assertLessEqual(
            normalized_dist("add", "daddy"), 1, "It should be lesser than or equal to 0"
        )


if __name__ == "__main__":
    unittest.main()
