import re

def extract_price(price_string):
    # Use regular expressions to extract the numeric string
    match = re.search(r'\d+(,\d+)*', price_string)
    if match:
        numeric_string = match.group()
    else:
        raise ValueError('Invalid price string')

    # Convert the numeric string to an integer
    price = int(numeric_string.replace(',', ''))

    # Check if the price is negotiable
    is_negotiable = 'Negotiable' in price_string

    return price

def extract_currency(price_string):
     currency = re.findall(r'[A-Z]+', price_string)[0]
     return currency

def get_numerical_value_from_string(string_text):
    numerical_value = re.findall(r'(\d+(?:\.\d+)?)', string_text)[0]
    return numerical_value



if __name__ == "__main__":
    ans =  extract_currency("GH₵ 1,450, Negotiable")
    num =  get_numerical_value_from_string("3.8 out of 34")
    print(num)