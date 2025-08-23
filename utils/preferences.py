#This module stores and manages the user's preferences

import json
from pathlib import Path
import os

FILENAME = "preferences.json"
cwd = Path(__file__).resolve()
BASE_DIR = cwd.parent.parent
DATA_DIR = BASE_DIR / "data" 
DATA_FILE = DATA_DIR / FILENAME

def seek_preferences():
    """Seeks user's preferences file"""

    DATA_DIR.mkdir(parents=True,exist_ok=True)

    if DATA_FILE.exists():

        print("\nPreferencias actuales: \n")
        with open(DATA_FILE,"r") as f:
            user_preferences = json.load(f)
            for k, v in user_preferences.items():
                print(f"{k} = {v}")
            print("\n")

        update = input("Desea actualizar las preferencias (Y/N): ").upper().rstrip()

        if update == "Y":
            os.remove(DATA_FILE)
            user_preferences = get_preferences()
        else:
            with open(DATA_FILE, "r") as f:
                user_preferences = json.load(f)

    else:
        user_preferences = get_preferences()
        with open(DATA_FILE,"w") as f:
            json.dump(user_preferences, f, indent = 4)
    
    return user_preferences
            
            

def get_float(mensaje):
    """Stores float securely"""

    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("El valor tiene que ser mayor a 0")
                continue
            return valor
        except ValueError:
            print("Valor inválido, vuelva a intentarlo")

def get_int(mensaje):
    """Stores float securely"""

    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print("El valor tiene que ser mayor a 0")
                continue
            return valor
        except ValueError:
            print("Valor inválido, vuelva a intentarlo")



def get_preferences():
    """Stores user preferences securely in a dictionary"""

    preferences = {
        "inflation_USA" : get_float("Inflación anual a considerar para USA (%): "),
        "inflation_MX" : get_float("Inflación anual a considerar para México (%): "),
        "anual_nominal_return" : get_float("Rendimiento anual esperado (%): "),
        "anual_dividend_yield" : get_float("Rendimiento por dividendos (%): "),
        "investment_years" : get_int("Años totales de inverisón (sin decimales): "),
        "initial_investment": get_float("Inversión inicial (MXN$): "),
        "gross_monthly_income": get_float("Ingreso bruto mensual (MXN$): "),
        "monthly_payment" : get_float("Aportación mensual (MXN$): "),
        "brokerage" : get_float("Costo por transacción en casa de bolsa (%): "),
    }

    return preferences

