from Person import Person

if __name__ == '__main__':
    maxim = Person('Максим', '24', 'м')
    olga = Person('Ольга', '24', 'ж')
    viktor = Person('Виктор', '24', 'м')
    print(maxim, olga, viktor, sep='\n')
    del viktor
    input()