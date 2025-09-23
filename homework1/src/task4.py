#Returns price after discount percentage applied (rounded to 2 decimals)
def calculate_discount(price,discount):
    return round(price*(1-(discount/100)),2)