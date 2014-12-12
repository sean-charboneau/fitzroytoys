def hasSufficientCharacters(newspaperClipping, ransomLetter):
    counts = {}
    for c in ransomLetter:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

    for c in newspaperClipping:
        if c in counts:
            counts[c] -= 1
            if counts[c] == 0:
                ransomMade = True
                for key in counts:
                    if counts[key] > 0:
                        ransomMade = False
                if ransomMade:
                    return True

    return False

if __name__ == "__main__":
    print hasSufficientCharacters("hello there george", "roger")
    print hasSufficientCharacters("hello there george", "rogerz")
    print hasSufficientCharacters("hello there george", "gregor")
    print hasSufficientCharacters("hello there george", "gregory")
