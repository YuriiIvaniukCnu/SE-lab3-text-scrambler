def readText():
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

def main():
    str = readText()
    print(str)

if __name__ == '__main__':
    main()
