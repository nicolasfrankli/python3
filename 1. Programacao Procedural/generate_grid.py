from random import randint

def get_int(text, minimum=None, default=None):
    while True:
        try:
            get = input(text)
            if not get and default is not None:
                return default
            elif not get and default is None:
                return None
            number = int(get)
            if minimum is not None and number < minimum:
                print(f"Must be >= {minimum}")
            else:
                return number
        except ValueError as err:
            print(err)

def main():
    rows = get_int('Number of rows:', 1,)
    columns = get_int('Number of columns:', 1,)
    minimum = get_int('Minimum (or Enter for 0):', None, 0)
    maximum_default = 1000
    if maximum_default <= minimum: maximum_default = 2 * minimum
    maximum = get_int(f'Maximum (or enter for {maximum_default}):', None, maximum_default)

    for count in range(rows):
        line = ''
        for c in range(columns):
            output = randint(minimum, maximum)
            line += f'{output} '
        print(line)

main()