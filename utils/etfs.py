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
            etfs[i][k]=[v]

    return etfs

class Etf:
    """Creates instance of one specific etf"""

    def __init__(self, **kwargs):
        """Creates all of the necesary arguments for the class"""

        for k, v in kwargs.items():
            setattr(self, k, v)
        print(self.__dict__)

    def calculate_investment(self):
        """Calculates the total investment value after set number of years"""


#ETF Class attributes
    #'reinvertion_coeficient', 'm_real_return', 'tm_div_yield', 'years'
    # 'inicial_investment', 'monthly_payment', 'taxes_rate', 'brokerage'



