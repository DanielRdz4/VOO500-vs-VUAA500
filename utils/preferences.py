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
            return valor
        except ValueError:
            print("Valor inválido, vuelva a intentarlo")

def get_int(mensaje):
    """Stores float securely"""

    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Valor inválido, vuelva a intentarlo")



def get_preferences():
    """Stores user preferences securely in a dictionary"""

    preferences = {
        "inflacion_a_USA" : get_float("Inflación anual a considerar para USA (%): "),
        "inflacion_a_MX" : get_float("Inflación anuala a considerar para México (%): "),
        "rendimiento_anual" : get_float("Rendimiento anual esperado (%): "),
        "rendimiento_dividendos" : get_float("Rendimiento por dividendos (%): "),
        "años_inversion" : get_int("Años totales de inverisón (sin decimales): "),
        "inversion_inicial": get_float("Inversión inicial (MXN$): "),
        "aportacion_mensual" : get_float("Aportación mensual (MXN$): "),
        "tasa_isr" : get_float("Tasa de isr aplicable por ingreso (%): ")
    }

    return preferences

