#Jose Franco
#11/28/2024
#Assignment 7.2 - Test Cases

import unittest
from city_functions import city_country

#Tests fot the city_country function
class TestCityCountry(unittest.TestCase):

#Test that the function returns the correct string.
    def test_city_country(self):
        result = city_country("Caracas", "Venezuela")
        self.assertEqual(result, "Caracas, Venezuela")

# Run the tests
if __name__ == "__main__":
    unittest.main()
