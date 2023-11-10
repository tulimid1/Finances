class Investor(object):
    RETIREMENT_AGE = 65
    portfolio_amount = []

    def __init__(
        self,
        current_age=26,
        investment_per_month=500,
        percent_rate_of_return=8,
        n_years_investing=0,
        last_name="",
        first_name="",
    ):
        self.CURRENT_AGE = current_age
        self.INVESTMENT_PER_MONTH = investment_per_month
        self.PERCENT_RATE_OF_RETURN = percent_rate_of_return
        self.N_YEARS_INVESTING = n_years_investing
        self.LAST_NAME = last_name
        self.FIRST_NAME = first_name

    def calculate_years_to_retirement(self):
        return self.RETIREMENT_AGE - self.CURRENT_AGE

    def calculate_portfolio_amount(self):
        n_months_per_year = 12
        monthly_rate_of_return = self.PERCENT_RATE_OF_RETURN / 100 / n_months_per_year
        for i_year in range(self.calculate_years_to_retirement()):
            for j_month in range(n_months_per_year):
                is_going_to_invest = i_year <= self.N_YEARS_INVESTING
                if is_going_to_invest:
                    investment_amount = self.INVESTMENT_PER_MONTH
                else:
                    investment_amount = 0

                is_first_year_first_month = i_year == 0 and j_month == 0
                if is_first_year_first_month:
                    if is_going_to_invest:
                        j_portfolio_amount = investment_amount
                    else:
                        j_portfolio_amount = 0
                else:
                    j_portfolio_amount += j_portfolio_amount * monthly_rate_of_return
                    j_portfolio_amount += investment_amount

            self.portfolio_amount.append(j_portfolio_amount)

    @property
    def FIRST_NAME(self):
        return self._FIRST_NAME

    @FIRST_NAME.setter
    def FIRST_NAME(self, name=""):
        if type(name) is not str:
            raise TypeError("first_name must be a string.\n")
        self._FIRST_NAME = name

    @property
    def LAST_NAME(self):
        return self._LAST_NAME

    @LAST_NAME.setter
    def LAST_NAME(self, name=""):
        if type(name) is not str:
            raise TypeError("last_name must be a string.\n")
        self._LAST_NAME = name

    @property
    def N_YEARS_INVESTING(self):
        return self._N_YEARS_INVESTING

    @N_YEARS_INVESTING.setter
    def N_YEARS_INVESTING(self, n_years=0):
        is_time_traveling = n_years < 0
        if is_time_traveling:
            raise ValueError("n_years_investing must be greater than 0.\n")
        self._N_YEARS_INVESTING = n_years

    @property
    def PERCENT_RATE_OF_RETURN(self):
        return self._PERCENT_RATE_OF_RETURN

    @PERCENT_RATE_OF_RETURN.setter
    def PERCENT_RATE_OF_RETURN(self, percent=8):
        rate_too_low = percent < 0
        if rate_too_low:
            raise ValueError("percent_rate_of_return must be greater than 0.\n")
        self._PERCENT_RATE_OF_RETURN = percent

    @property
    def INVESTMENT_PER_MONTH(self):
        return self._INVESTMENT_PER_MONTH

    @INVESTMENT_PER_MONTH.setter
    def INVESTMENT_PER_MONTH(self, investment_amount=0):
        is_taking_from_investment = investment_amount < 0
        if is_taking_from_investment:
            raise ValueError("investment_per_month must be positive.\n")
        self._INVESTMENT_PER_MONTH = investment_amount

    @property
    def CURRENT_AGE(self):
        return self._CURRENT_AGE

    @CURRENT_AGE.setter
    def CURRENT_AGE(self, age=26):
        has_not_been_born = age < 1
        if has_not_been_born:
            raise ValueError("current_age must be >= 1.\n")
        self._CURRENT_AGE = age
