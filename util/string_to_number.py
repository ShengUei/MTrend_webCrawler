
def str_to_int(str_int):
    if type(str_int) == str:
        return int(str_int.replace(',', ''))
    return str_int

def str_to_float(str_float):
    if type(str_float) == str:
        return float(str_float.replace(',', ''))
    return str_float
