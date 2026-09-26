def read_text():
    while True:
        try:
            text = input("Enter text: ")
        except Exception as e:
            print("Enter text again using only ASCII characters")
            continue
        else:
            if text == "":
                print("Please enter a text")
                continue
            if not text.isascii():
                print("Use only ASCII characters")
                continue

        return text

def scramble_text(text):
    text = text.split()
    reversed_words = []
    for word in text:
        letters = [ch for ch in word if ch.isalpha()]
        new_word = ""
        for ch in word:
            if ch.isalpha():
                new_word += letters.pop()
            else:
                new_word += ch
        reversed_words.append(new_word)
    return " ".join(reversed_words)

def main():
    str = read_text()
    print("Original text: ", str)
    print("New text: ", scramble_text(str))

if __name__ == '__main__':
    main()
