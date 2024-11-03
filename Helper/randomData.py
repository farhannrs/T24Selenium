import datetime
import random


def create_cnic():
    x = random.randint(11111111, 99999999)
    y = f'42201{x}'
    return y


def create_mobile_number():
    x = random.randint(1111111, 9999999)
    y = f'0300{x}'
    return y


def create_ntn():
    x = random.randint(111111, 999999)
    y = f'{x}-0'
    return y


def create_limit_id(limit_ids):
    ids = []
    # iterating through IDs to get max value, and add 1 into it to get new limit ID
    for i in limit_ids:
        # splitting ID to get last value (which is used to get new ID)
        value = i.text.split("101647.0006200.")
        try:
            ids.append(value[1])
        except:
            pass
    return int(max(ids))+1

# def generate_random_date_in_format():
#   """
#   This function generates a random date within the format "DD MMM YYYY" (01 SEP 2025 in this case).
#   """
#   # Set the desired year and month
#   year = 2025
#   month = 9  # September
#
#   # Generate a random day between 1 and 2 (inclusive) to ensure both 1st and 2nd are possible
#   day = random.randint(1, 2)
#
#   # Create the date object
#   random_date = date(year, month, day)
#
#   # Format the date as "DD MMM YYYY"
#   formatted_date = random_date.strftime("%d %b %Y")
#
#   return formatted_date

def generate_random_date_in_format():
    start_year = 1951
    end_year = 2024
    while True:
        try:
            year = random.randint(start_year, end_year)
            month = random.randint(1, 12)
            day = random.randint(1, 31)

            # Handle invalid dates (e.g., February 29th in non-leap years)
            random_date = datetime.date(year, month, day)
            break
        except ValueError:
            pass  # Skip to the next iteration if an invalid date is generated

    formatted_date = random_date.strftime('%d %b %Y')

    return formatted_date