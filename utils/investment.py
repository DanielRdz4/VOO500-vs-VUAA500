#Dependecies
import pandas as pd

def calculate_data(usr_pref):
    """Transforms user preferences data for later calculation"""

    usr_data = []
    for values in usr_pref.values():
        usr_data.append(values)
        
    capital_gains = (usr_data[2] / 100) - (usr_data[3] / 100)
    real_return = ( (1 + capital_gains) / (1 + usr_data[0] / 100) ) - 1


    # m_* --> monthly_*
    m_real_return = real_return / 12
    usr_data.append(m_real_return)
    # tm_* --> trimonthly_*
    tm_div_yield = usr_data[3] / 4  #Dividends distributed trimonthly, 4 trimesters in a year
    usr_data.append(tm_div_yield)

    return usr_data


