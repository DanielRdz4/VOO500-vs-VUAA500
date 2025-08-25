from utils import investment
from utils import taxes

def build_etf(usr_data):
    """Creates the specific dictionary for VOO500 and VUAA500"""

    #Dividend's Reinvestment Coeficient
    reinv_coef = taxes.reinvertion_coeficient(usr_data)

    etfs = [{},{}]
    for i in range(2):
        etfs[i]["reinvertion_coeficient"] = reinv_coef[i]
        
        for k, v in usr_data.items():
            etfs[i][k]=[v]

    return etfs

class Etf:
    """Creates instance of one specific etf"""

    def __init__(self, **kwargs):
        """Creates all of the necesary arguments for the class"""

        for k, v in kwargs.items():
            setattr(self, k, v)



