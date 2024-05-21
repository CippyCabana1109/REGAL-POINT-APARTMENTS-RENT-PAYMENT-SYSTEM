import unittest
from rent_splitting import RentSplitting

class TestRentSplitting(unittest.TestCase):
    def test_split_rent(self):
        # Test splitting rent among 4 tenants for a total rent of $2000
        rent_splitting = RentSplitting(4)
        rent_per_tenant = rent_splitting.split_rent(2000)
        self.assertEqual(rent_per_tenant, 500.0)

if __name__ == '__main__':
    unittest.main()
