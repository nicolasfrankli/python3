#Digite o número na linha de comando após o nome do arquivo
from sys import argv

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
            number = argv[1]
            break
        except ValueError as err:
            print(err)
            continue
        except IndexError:
            print("usage: bigdigits.py <number>")
        except EOFError:
            break

    str_number = str(number)
    for c in range(7):
        output = ''
        for count in range(len(str_number)):
            output += bigdigits[int(str_number[count])][c]  +  '   '
        print(output)

main()