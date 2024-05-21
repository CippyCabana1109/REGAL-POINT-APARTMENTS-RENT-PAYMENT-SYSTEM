import unittest
from property_management import PropertyManagement

class TestPropertyManagement(unittest.TestCase):
    def setUp(self):
        self.property_manager = PropertyManagement("Regal Point Apartments")

    def test_add_unit(self):
        # Test adding a new unit
        self.property_manager.add_unit("101", "2-bedroom apartment")
        self.assertIn("101", self.property_manager.available_units)

    def test_remove_unit(self):
        # Test removing an existing unit
        self.property_manager.add_unit("102", "1-bedroom apartment")
        self.property_manager.remove_unit("102")
        self.assertNotIn("102", self.property_manager.available_units)

if __name__ == '__main__':
    unittest.main()
