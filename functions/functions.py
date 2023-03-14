def validInteger(number):
    while True:
        try :
            get_number = int(input())
            break
        except ValueError as err:
            print(err)
            continue
        except EOFError:
            break
    return get_number
