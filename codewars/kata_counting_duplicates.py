__author__ = 'Tamby Kaghdo'

def duplicate_count(text):
    text = text.lower()
    duplicate_counter = 0
    for i in text:
        if text.count(i) > 1:
            text = text.replace(i, "")
            duplicate_counter += 1
    return duplicate_counter

def main():
    print(duplicate_count("abcde"))
    print(duplicate_count("abcdea"))
    print(duplicate_count("indivisibility"))

if __name__ == '__main__':
    main()
