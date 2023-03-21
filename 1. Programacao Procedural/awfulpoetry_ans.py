# Programa para gerar textos de teste
from random import choice, randint

def main():
    articles = ['the', 'a', 'an']
    subjects = ['cat', 'dog', 'man', 'woman']
    verbs = ['sing', 'run', 'jumps']
    adverbs = ['slowly', 'quickly', 'silently', 'well', 'wrong'] 
    terms = [articles, subjects, verbs, adverbs]
    for count in range(5):
        estructure = randint(1,2) #Define se a estrutura da frase vai ser artigo, sujeito, verbo e advérbio ou artigo, sujeito e verbo
        line = ''
        for c in range(2+estructure): 
            line += f'{choice(terms[c])} '
        print(line)

main()