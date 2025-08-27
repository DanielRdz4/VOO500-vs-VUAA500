from utils import investment
from utils import taxes

def build_etf(usr_data):
    """Creates the specific dictionary for VOO500 and VUAA500"""

    #Dividend's Reinvestment Coeficient
    reinv_coef = taxes.reinvertion_coeficient(usr_data)

    #Fund management cost
    #                 [VOO, VUAA]
    management_cost = [0 , 0.04]    #The 0.03% cost of the VOO is already taken into account in the 10% anual return,
                                    #VUAA is 0.04% more expensive

    etfs = [{},{}]
    for i in range(2):
        etfs[i]["reinvertion_coeficient"] = reinv_coef[i]
        etfs[i]["management_cost"] = management_cost[i]
        
        for k, v in usr_data.items():
            etfs[i][k] = v

    return etfs


class Etf:
    """Creates instance of one specific etf"""

    def __init__(self, **kwargs):
        """Creates all of the necesary arguments for the class"""

        for k, v in kwargs.items():
            setattr(self, k, v)

    def calculate_dividends(self, total):
        """Calculates the dividend due for a given trimester"""

        dividend = total * self.tm_div_yield
        reinv_dividend = dividend * self.reinvertion_coeficient
        
        return reinv_dividend
    
    def yearly_growth(self,total):
        """Calculates 1 year of growth"""

        m_real_return = self.m_real_return * (1 - (self.management_cost) / 12)

        for month in range(1,13):

            interest = total * m_real_return

            if month % 3 == 0:
                dividend = self.calculate_dividends(total)
            else:
                dividend = 0

            monthly_payment = self.monthly_payment * (1 - self.brokerage)
            
            total += monthly_payment + interest + dividend
        
        return total

    def calculate_investment(self):
        """Calculates the total investment value after set number of years"""

        total = self.initial_investment
        total_per_year = []

        for year in range(self.years):
            total = self.yearly_growth(total)
            self.monthly_payment *= (1 + self.inflation_MX)
            total_per_year.append(total)

        return total_per_year


#ETF Class attributes
    #'reinvertion_coeficient','management_cost' , 'm_real_return', 'tm_div_yield', 'years', 'months'
    # 'initial_investment', 'monthly_payment', 'taxes_rate', 'brokerage'



