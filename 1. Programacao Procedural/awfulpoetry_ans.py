# Programa para gerar textos de teste
from random import choice, randint
from sys import argv

def main():
        if len(argv) == 2: #Verifica se o número foi fornecido na linha de comando
            while True:             
                try :
                    number = int(argv[1])
                    break
                except None:
                    continue
                except ValueError as err:
                    print(err)
                    continue
                except IndexError:
                    print(f'usage: awfulpoetry_ans.py <number>')
                except EOFError:
                    break
            if 10 < number or number < 1:
                    print('Must be >1 and <10') 
            else:
                articles = ['the', 'a', 'an']
                subjects = ['cat', 'dog', 'man', 'woman']
                verbs = ['sing', 'run', 'jumps']
                adverbs = ['slowly', 'quickly', 'silently', 'well', 'wrong'] 
                terms = [articles, subjects, verbs, adverbs]
                for count in range(number):
                    estructure = randint(1,2) #Define se a estrutura da frase vai ser artigo, sujeito, verbo e advérbio ou artigo, sujeito e verbo
                    line = ''
                    for c in range(2+estructure): 
                        line += f'{choice(terms[c])} '
                    print(line)
        else:
            print("No command line arguments")
main() 