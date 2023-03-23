def order_list(list):
    ordered_list = []
    for count in range(len(list)):
        ordered_list += ' ' #cria uma lista do tamanho da lista de argumento
    lowest = None
    highest = None
    for count in range(len(list)):
        auxiliary_variable = None
        number = list[count]
        if count > 0: # 9 8 7
            if ordered_list[count-1] > number:
                auxiliary_variable = ordered_list[count-1]
                ordered_list[count-1] = number
                ordered_list[count] =  auxiliary_variable
            else: 
                ordered_list[count] = number                    
        else:
            ordered_list[0] = number
    
    for count in range(len(ordered_list)):
        auxiliary_variable = None
        number = ordered_list[count]
        if count > 0: # 9 8 7
            if ordered_list[count-1] > number:
                auxiliary_variable = ordered_list[count-1]
                ordered_list[count-1] = number
                ordered_list[count] =  auxiliary_variable
            else: 
                ordered_list[count] = number                    
        else:
            ordered_list[0] = number
    return ordered_list


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
    ordered_list = order_list(numbers)
    if (len(ordered_list) % 2 == 0):
        mean = (ordered_list[len(ordered_list)//2 - 1] + ordered_list[len(ordered_list)//2]) / 2
    else:
        mean = ordered_list[len(ordered_list)//2]
    print(f'numbers: {numbers}\ncount = {len(numbers)} sum = {sum} lowest = {lowest}   highest = {highest}  mean = {mean:.2f}')
 
main()