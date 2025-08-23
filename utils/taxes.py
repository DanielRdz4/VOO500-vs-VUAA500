
isr_table = [
#   [inf limit],   [sup limit],   [fixed amount], [% above fixed amount]
    [0.01,         578.52,        0.00,           1.92],
    [578.53,       4_910.18,      11.11,          6.40],
    [4_910.19,     8_629.20,      288.33,         10.88],
    [8_629.21,     10_031.07,     692.96,         16.00],
    [10_031.08,    12_009.94,     917.26,         17.92],
    [12_009.95,    24_222.31,     1_271.87,       21.36],
    [24_222.32,    38_177.69,     3_880.44,       23.52],
    [38_177.70,    72_887.50,     7_162.74,       30.00],
    [72_887.51,    97_183.33,     17_575.69,      32.00],
    [97_183.34,    291_550.00,    25_350.35,      34.00],
    [291_550.01,   float("inf"),  91_435.02,      35.00]
]

def get_isr(monthly_income):
    """Calculates the income's correspondent tax rate"""

    table_len = len(isr_table)
    
    for fila in range(table_len):

        sup_lim = isr_table[fila][1]
        inf_lim = isr_table[fila][0]
        fixed_amount = isr_table[fila][2]
        above = isr_table[fila][3]

        if monthly_income > sup_lim:
            continue
        else:
            print(f"{sup_lim}, {inf_lim}, {fixed_amount}, {above}")
            taxes = fixed_amount + (monthly_income - inf_lim) * (above / 100)
            tax_rate = taxes / monthly_income
            return tax_rate
        
