from random import randint
import os

wordlist = ['mountain', 'country', 'dog', 'cat', 'hedgehog', 'motorbike', 'zelda', 'game', 'beer', 'alcohol', 'adventure', 'book', 'television', 'clothes', 'couch', 'music']

word = wordlist[randint(0, len(wordlist))-1]
art = ["""\n\n\n\n\n\n\n""",
        """\n\n\n\n\n\n
        _______""",
        """\n
           |
           |
           |
           |
           | 
        -------""",
        """
           ______
           |/
           |
           |
           |
           |
        -------""",
        """
           ______
           |/   |
           |
           |
           |
           |
        -------""",
        """
           ______
           |/   |
           |    O
           |    
           |    
           |
        -------""",
       """
          ______
          |/   |
          |    O
          |    |
          |
          |
       -------""",
      """
          ______
          |/   |
          |    O
          |   -|-
          |
          |
       -------""",
     """
          ______
          |/   |
          |    O
          |   -|-
          |   / \\
          |
       -------"""]

go = 0
created_string = ''

for i in range(0, len(word)):
    created_string += "_"

used_letters = []
used_words = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(art[go])
    print(created_string)
    print('used letters: ', end="")
    print(*used_letters)
    print('used words: ', end="")
    print(*used_words)
    guess = input(">>")
    if len(guess) == 1:
        if guess in word:
            new_string = ''
            for i in range(0,len(word)):
                if word[i] == guess:
                    new_string += guess
                else:
                    new_string += created_string[i]
            created_string = new_string
            if(created_string == word):
                print("you win!!\nThe word was: " + word)
                break
        else:
            go += 1
            used_letters.append(guess)
            if go == len(art) -1:
                print("Game over...\nThe word was: " + word)
                print(art[go])
                break

    elif len(guess) > 1:
        if(guess == word):
            print("you win!!\nThe word was: " + word)
            break
        else:
            go += 1
            used_words.append(guess)
            if go == len(art)-1:
                print("Game over...\nThe word was: " + word)
                print(art[go])
                break

