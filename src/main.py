#Dependencies
from utils import preferences as pref
from utils import etfs
from utils import investment


#Main script
usr_pref = pref.seek_preferences()
usr_data = investment.calculate_data(usr_pref)
etfs_data = etfs.build_etf(usr_data)
proyection = [etfs.Etf(**data) for data in etfs_data]







##Pseudocode
    #Get user data
    #Store user preferences
    #Calculate every other necesarry variable
    #Clculate final investment value for both ETF's
    #Compare totals in graph
