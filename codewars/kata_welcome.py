__author__ = 'Tamby Kaghdo'

#My solution to Welcome! Kata from codewars.com
def greet(language):
    greetings = {'english': 'Welcome', 'czech': 'Vitejte', 'danish': 'Velkomst', 'dutch': 'Welkom', 'estonian': 'Tere tulemast', 'finnish': 'Tervetuloa', 'flemish': 'Welgekomen', 'french': 'Bienvenue', 'german': 'Willkommen', 'irish': 'Failte', 'italian': 'Benvenuto', 'latvian': 'Gaidits', 'lithuanian': 'Laukiamas', 'polish': 'Witamy', 'spanish': 'Bienvenido', 'swedish': 'Valkommen', 'welsh': 'Croeso'}
    response = greetings['english']
    for key, value in greetings.items():
        if key == language:
            response = value
    return response

def main():
    print(greet('english'))
    print(greet('dutch'))
    print(greet('IP_ADDRESS_INVALID'))
    print(greet(''))
    print(greet(2))

if __name__ == '__main__':
    main()
