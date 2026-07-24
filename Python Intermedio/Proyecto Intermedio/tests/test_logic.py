import os
import shutil
import sys
import unittest


sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic import FinanceManager, NoCategoriesError, CategoryAlreadyExistsError  # noqa: E402
from persistence import Persistence  # noqa: E402


class TestFinanceManager(unittest.TestCase):
    def setUp(self):
        self.test_dir = os.path.join(os.path.dirname(__file__), "_data_test")
        self.persistence = Persistence(data_dir=self.test_dir)
        self.manager = FinanceManager(persistence=self.persistence)

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    # ---- Categories ----

    def test_add_category(self):
        self.manager.add_category("food")
        self.assertIn("Food", self.manager.categories)

    def test_empty_category_raises_error(self):
        with self.assertRaises(ValueError):
            self.manager.add_category("   ")

    def test_duplicate_category_raises_error(self):
        self.manager.add_category("Food")
        with self.assertRaises(CategoryAlreadyExistsError):
            self.manager.add_category("food")  # same normalized name

    # ---- Movements: business rules ----

    def test_expense_without_categories_raises_error(self):
        with self.assertRaises(NoCategoriesError):
            self.manager.add_expense("Lunch", 5000, "Food")

    def test_nonexistent_category_raises_error(self):
        self.manager.add_category("Food")
        with self.assertRaises(ValueError):
            self.manager.add_expense("Lunch", 5000, "Transport")

    def test_negative_amount_raises_error(self):
        self.manager.add_category("Food")
        with self.assertRaises(ValueError):
            self.manager.add_expense("Dinner", -100, "Food")

    def test_non_numeric_amount_raises_error(self):
        self.manager.add_category("Food")
        with self.assertRaises(ValueError):
            self.manager.add_expense("Dinner", "abc", "Food")

    def test_empty_title_raises_error(self):
        self.manager.add_category("Food")
        with self.assertRaises(ValueError):
            self.manager.add_expense("   ", 1000, "Food")

    def test_balance_with_income(self):
        self.manager.add_category("Salary")
        self.manager.add_income("Monthly pay", 500000, "Salary")
        self.assertEqual(self.manager.calculate_balance(), 500000)

    def test_balance_with_expense(self):
        self.manager.add_category("Transport")
        self.manager.add_expense("Bus", 1500, "Transport")
        self.assertEqual(self.manager.calculate_balance(), -1500)

    def test_mixed_balance(self):
        self.manager.add_category("Salary")
        self.manager.add_category("Food")
        self.manager.add_income("Pay", 100000, "Salary")
        self.manager.add_expense("Dinner", 30000, "Food")
        self.assertEqual(self.manager.calculate_balance(), 70000)

    def test_calculate_totals(self):
        self.manager.add_category("Salary")
        self.manager.add_category("Food")
        self.manager.add_income("Pay", 100000, "Salary")
        self.manager.add_expense("Dinner", 30000, "Food")
        income_total, expense_total = self.manager.calculate_totals()
        self.assertEqual(income_total, 100000)
        self.assertEqual(expense_total, 30000)

  
if __name__ == "__main__":
    unittest.main()
