def is_palindrome(word):
    back_word = word[::-1]
    print(back_word)
    if (word == back_word):
        print("SI es palíndromo")
    else:
        print("No es palíndromo")

word = input("Ingrese palabra: ")
is_palindrome(word)