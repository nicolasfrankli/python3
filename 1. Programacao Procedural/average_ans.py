def main():
    numbers = list()
    sum = 0
    lowest = None
    highest = None
    while True:
        try:
            line = input("enter a number or Enter to finish:")
            if not line:
                break
            number = int(line)
            sum += number
            numbers.append(number)
            if lowest is None or lowest > number:
                lowest = number
            if highest is None or highest < number:
                highest = number
        except ValueError as err:
            print(err)
            continue
    
    print(f'numbers: {numbers}\ncount = {len(numbers)} sum = {sum} lowest = {lowest}   highest = {highest}  mean = {(sum/len(numbers)):.2f}')
 
main()