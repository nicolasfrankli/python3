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
    if len(argv) == 2: #Verifica se o número foi fornecido na linha de comando
        while True:             
            try :
                number = argv[1]
                break
            except None:
                continue
            except ValueError as err:
                print(err)
                continue
            except IndexError:
                print("usage: bigdigits.py <number>")
            except EOFError:
                break

        str_number = str(number)
        for c in range(7): #Cada algarismo da lista de grandes dígitos tem 7 itens ou 7 linhas
            output = ''
            for count in range(len(str_number)):
                output += bigdigits[int(str_number[count])][c]  +  '   ' #Cria uma string com as linhas em ordem de cada grande dígito
            print(output)
    else:
        print("No command line arguments")
main()