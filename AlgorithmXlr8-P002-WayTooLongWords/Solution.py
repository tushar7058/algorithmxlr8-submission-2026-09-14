def solve(word):
    if len(word) <= 10:
        return word

    return word[0] + str(len(word) - 2) + word[-1]


def main():
    n = int(input())

    for _ in range(n):
        word = input().strip()
        print(solve(word))


if __name__ == "__main__":
    main()

# def solve(word):
#     if len(word) <= 10:
#         return word

#     return word[0] + str(len(word) - 2) + word[-1]

"""
    1. first we will check the lenght of word
    2. if it crossed more than 10 we will keep first letter and last letter 
    3. we will return inbetween word count
    4. return the new shorter version of that word.

    eg .
    n = 4 word localization internationalization pneumonoultramicroscopicsilicovolcanoconiosis
Output :word, l10n, i18n, p43s
    
"""
    # if len(word) <= 10:
    #     return word
    # return word[0]+str(len(word-2)+word[-1])

   
