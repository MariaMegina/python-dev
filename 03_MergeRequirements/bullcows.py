import sys
import random
import urllib.request
import cowsay

def bullscows(guess, secret):
    bulls = 0
    cows = 0
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return (bulls, cows)

def gameplay(ask, inform, words):
    attempts = 0
    secret = random.choice(words)
    while True:
        guess = ask("Введите слово: ", words)
        bulls, cows = bullscows(guess, secret)
        inform("Быки: {}, Коровы: {}", bulls, cows)
        attempts += 1
        if guess == secret:
            return attempts


def inform(format_string, bulls, cows):
    print(cowsay.cowsay(format_string.format(bulls, cows), cow = random.choice([*cowsay.list_cows()])))


def ask(prompt, valid = None):
    print(cowsay.cowsay(prompt, cow = random.choice([*cowsay.list_cows()])))
    guess = input()
    if valid != None:
        while guess not in valid:
            print(cowsay.cowsay(prompt, cow = random.choice([*cowsay.list_cows()])))
            guess = input()
    return guess

if __name__ == "__main__":

    if sys.argv[1].startswith("https://"):
        dictionary = urllib.request.urlopen(sys.argv[1]).read().decode("utf-8").splitlines()

    else:
        try:
            with open(sys.argv[1], "r") as file:
                dictionary = [word.strip() for word in file]
        except Exception:
            print("dictionary is not corret")
            sys.exit(1)
    if len(sys.argv) == 2:
        length = 5
    elif len(sys.argv) == 3:
        length = int(sys.argv[2])
    else:
        print("arguments is not correct")
        sys.exit(1)

    dictionary = [word for word in dictionary if len(word) == length]
#    print(dictionary)
    print("Попыток: ",gameplay(ask, inform, dictionary))
