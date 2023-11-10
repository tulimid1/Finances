import unittest
import os
from Investor import Investor


class Investor_Test(unittest.TestCase):
    example_investor = Investor()
    
    def test_portfolio_amount_case_2(self):
        dan = Investor(
            current_age=45,
            investment_per_month=200,
            percent_rate_of_return=8,
            n_years_investing=20,
        )
        dan.calculate_portfolio_amount()
        self.assertEqual(dan.portfolio_amount[-1], 118589)

    def test_portfolio_amount_case_1(self):
        sally = Investor(
            current_age=35,
            investment_per_month=200,
            percent_rate_of_return=8,
            n_years_investing=10,
        )
        sally.calculate_portfolio_amount()
        self.assertEqual(sally.portfolio_amount[-1], 181469)

    def test_investor_has_calculate_portfolio_amount(self):
        self.assertTrue("calculate_portfolio_amount" in dir(self.example_investor))

    def test_investor_has_portfolio_amount(self):
        self.assertTrue("portfolio_amount" in dir(self.example_investor))

    def test_percent_rate_of_return_too_high(self):
        with self.assertRaises(ValueError):
            Investor(percent_rate_of_return=-101)

    def test_percent_rate_of_return_too_low(self):
        with self.assertRaises(ValueError):
            Investor(percent_rate_of_return=-1)

    def test_percent_rate_of_return_error_not_float(self):
        with self.assertRaises(TypeError):
            Investor(percent_rate_of_return="not float")

    def test_investor_has_percent_rate_of_return(self):
        self.assertTrue("percent_rate_of_return" in dir(self.example_investor))

    def test_calculate_years_to_retirement_case_1(self):
        me = Investor(age=35)
        self.assertEqual(me.calculate_years_to_retirement(), 30)

    def test_investor_has_calculate_years_to_retirement(self):
        self.assertTrue("calculate_years_to_retirement" in dir(self.example_investor))

    def test_retirement_age_65(self):
        self.assertEqual(self.example_investor.RETIREMENT_AGE, 65)

    def test_investor_has_retirement_age(self):
        self.assertTrue("RETIREMENT_AGE" in dir(self.example_investor))

    def test_n_years_investing_error_not_positive(self):
        with self.assertRaises(ValueError):
            Investor(n_years_investing=-1)

    def test_n_years_investing_error_not_int(self):
        with self.assertRaises(TypeError):
            Investor(n_years_investing="not an int")

    def test_investor_has_n_year_investing(self):
        self.assertTrue("n_years_investing" in dir(self.example_investor))

    def test_investment_per_month_error_not_positive(self):
        with self.assertRaises(ValueError):
            Investor(investment_per_month=-1)

    def test_investment_per_month_error_not_int(self):
        with self.assertRaises(TypeError):
            Investor(investment_per_month="not an int")

    def test_investor_has_investment_per_month(self):
        self.assertTrue("investment_per_month" in dir(self.example_investor))

    def test_current_age_error_not_positive(self):
        with self.assertRaises(ValueError):
            Investor(current_age=-1)

    def test_current_age_error_not_int(self):
        with self.assertRaises(TypeError):
            Investor(current_age="not an int")

    def test_investor_has_current_age(self):
        self.assertTrue("current_age" in dir(self.example_investor))

    def test_last_name_set_property(self):
        last_name = "Tulimieri"
        me = Investor(last_name=last_name)
        self.assertEqual(me.last_name, last_name)

    def test_error_last_name_not_str(self):
        with self.assertRaises(TypeError):
            Investor(last_name=1)

    def test_investor_has_last_name(self):
        self.assertTrue("last_name" in dir(self.example_investor))

    def test_first_name_set_property(self):
        first_name = "Duncan"
        me = Investor(first_name=first_name)
        self.assertEqual(me.first_name, first_name)

    def test_error_first_name_not_str(self):
        with self.assertRaises(TypeError):
            Investor(first_name=1)

    def test_investor_has_first_name(self):
        self.assertTrue("first_name" in dir(self.example_investor))

    def test_investor_is_class(self):
        self.assertTrue(os.path.isfile("Investor.py"))


if "__main__" == __name__:
    unittest.main()
