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



if __name__ == "__main__":
   ans =  extract_price("GH₵ 1,450, Negotiable")
   print(ans)