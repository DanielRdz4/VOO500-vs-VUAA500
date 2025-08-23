#Dependecies
from utils import taxes

def calculate_data(usr_pref):
    """Transforms user preferences data for later calculation"""

    anual_return =usr_pref["anual_nominal_return"]
    dividend_yield = usr_pref["anual_dividend_yield"]
    inflation_USA = usr_pref["inflation_USA"]
    broker = usr_pref["brokerage"]

    capital_gains = (anual_return) / 100 - (dividend_yield / 100)
    real_return = ( (1 + capital_gains) / (1 + inflation_USA / 100) ) - 1
    brokerage = broker / 100

    # m_* --> monthly_*
    m_real_return = real_return / 12

    # tm_* --> trimonthly_*
    tm_div_yield = dividend_yield / 4  #Dividends distributed trimonthly

    #Data needed for calculations
    usr_data={
        "m_real_return" : m_real_return,
        "tm_div_yield" : tm_div_yield,
        "years" : usr_pref["investment_years"],
        "inicial_investment" : usr_pref["initial_investment"],
        "monthly_payment" : usr_pref["monthly_payment"],
        "taxes_rate" : taxes.get_isr(usr_pref["gross_monthly_income"]),
        "brokerage" : brokerage
    } 


    return usr_data


