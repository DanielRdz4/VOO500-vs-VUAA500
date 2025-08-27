#Dependencies
from utils import preferences as pref
from utils import etfs
from utils import investment


#Main script
usr_pref = pref.seek_preferences()
usr_data = investment.calculate_data(usr_pref)
etfs_diccs = etfs.build_etf(usr_data)
etfs_list = [etfs.Etf(**data) for data in etfs_diccs]

for etf in etfs_list:
    print(f"\n{etfs.Etf.calculate_investment(etf)}")
    

##Pseudocode
    #Get user data
    #Store user preferences
    #Calculate every other necesarry variable
    #Clculate final investment value for both ETF's
    #Compare totals in graph
