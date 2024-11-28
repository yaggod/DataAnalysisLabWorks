def get_value_of_percent_string(string):
    return float(string[:-1])/100

def get_value_of_money_string(string):
    return float(string[:-2].replace(",", "."))

def get_sum_of_money_strings(*args):
    result = 0
    for arg in args:
        if(arg):
            result += get_value_of_money_string(arg)
    return result

def get_money_string_from_value(value):
    return "{:.2f}".format(value).replace(".", ",") + "р."
