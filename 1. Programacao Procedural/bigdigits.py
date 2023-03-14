#Após a entrada de um número, o programa exibe-o com grandes dígitos
Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ",
        "   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]
bigdigits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

def main(): 
    while True:
        try :
            number = int(input())
            break
        except ValueError as err:
            print(err)
            continue
        except EOFError:
            break

    str_number = str(number)
    #23
    for c in range(7):
        output = ''
        for count in range(len(str_number)):
            output += bigdigits[int(str_number[count])][c]  +  '   '
        print(output)



main()