import unittest
from supermarket import (
    inventory,
    prices,
    total_count,
    find_category,
    apply_discount
)


class TestInventory(unittest.TestCase):
    """Tests for inventory structure"""

    def test_inventory_has_5_categories(self):
        """Inventory must have exactly 5 categories"""
        self.assertEqual(len(inventory), 5)

    def test_each_category_has_4_items(self):
        """Every category must have at least 4 items"""
        for category, items in inventory.items():
            self.assertGreaterEqual(
                len(items), 4,
                f"{category} has fewer than 4 items"
            )

    def test_total_count_is_positive(self):
        """Total inventory count must be greater than 0"""
        self.assertGreater(total_count(), 0)

    def test_no_negative_quantities(self):
        """No item should have negative quantity"""
        for category, items in inventory.items():
            for item, qty in items.items():
                self.assertGreaterEqual(qty, 0, f"{item} has negative qty")


class TestCategoryLookup(unittest.TestCase):
    """Tests for find_category function"""

    def test_find_apple_in_fruits(self):
        """Apple should be in Fruits category"""
        self.assertEqual(find_category("Apple"), "Fruits")

    def test_find_milk_in_dairy(self):
        """Milk should be in Dairy category"""
        self.assertEqual(find_category("Milk"), "Dairy")

    def test_unknown_item_returns_none(self):
        """Unknown items should return None"""
        self.assertIsNone(find_category("Pizza"))


class TestDiscount(unittest.TestCase):
    """Tests for the NEW discount feature"""

    def test_no_discount_for_regular_customer(self):
        """Regular customers pay full price"""
        self.assertEqual(apply_discount(100), 100)

    def test_senior_gets_10_percent_off(self):
        """Senior citizens get 10% discount"""
        self.assertEqual(apply_discount(100, is_senior=True), 90.0)

    def test_discount_on_decimal_amount(self):
        """Discount should round to 2 decimals"""
        self.assertEqual(apply_discount(99.99, is_senior=True), 89.99)

    def test_negative_amount_raises_error(self):
        """Negative amounts should raise ValueError"""
        with self.assertRaises(ValueError):
            apply_discount(-10)


if __name__ == "__main__":
    unittest.main()