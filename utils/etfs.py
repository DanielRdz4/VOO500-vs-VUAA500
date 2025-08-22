
def build_etf(usr_data):
    """Creates the specific dictionary for VOO500 and VUAA500"""

    #Dividend's Reinvestment Coeficient
    #            [VOO  , VUAA]
    reinv_coef = [0.606, 0.848]

    etfs = [[],[]]
    for i in range(2):
        etfs[i].append(reinv_coef[i])
        
        for value in usr_data:
            etfs[i].append(value)

    return etfs

