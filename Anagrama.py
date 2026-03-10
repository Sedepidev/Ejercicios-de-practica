# Ejercicio para determinar si dos palabras son anagramas
word_one = input("Pon la primera palabra para verificar: ")
word_two = input("Pon la segunda palabra para verificar: ")
def is_anagrama(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    
    return sorted(word_one.lower()) == sorted(word_two.lower())

def main():
    print(is_anagrama(word_one, word_two))

main()