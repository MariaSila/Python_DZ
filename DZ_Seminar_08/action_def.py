contacts = 'List_contact.txt'

def save_file(data):    
    with open(contacts, 'w', encoding='utf-8') as f:
        for i in data:
            f.write(i + '\n')


def read_file():
    with open(contacts, 'r', encoding='utf-8') as f:
        file = f.readlines()
    data = []
    for i in range(len(file)):
        data.append(file[i].replace('\n',''))
    return data


def show_contact(data):
    print('\nСписок контактов:')
    for i in range(len(data)):
        print(f"{i+1}. {data[i]}")


 
def add_contact(data):
    print('Введите Имя, Фамилию, номер телефона: ')
    data.append(input())
    return data


def find_contact(data):
    notfind = True
    print('Введите строку поиска: ')
    c = input()
    lst = []
    for i in range(len(data)):
        if c in data[i]:
            lst.append(f'{i+1}. {data[i]}')
            notfind = False
    print(f"\nРезультат поиска по запросу <{c}>:")
    for i in lst:
        print(i)
    if notfind:
       print(f'Контакт не найден')


def delet_contact(data):
    print('Для удаления введите порядковый номер контакта')
    number = int(input())
    notfind = True
    if number <= len(data):
        d = data[number - 1]
        del data[number - 1]
        print(f'\nУдален контакт: {d}\n')
        notfind = False
    elif notfind:
       print(f'\nКонтакт под номером {number} не найден.\nКоличество контактов в списке: {len(data)}\n')
    return data


def change_contact(data):
    print('Введите порядковый номер контакта')
    number = int(input())
    notfind = True
    if number <= len(data):
        print(f"Старое значение: {data[number-1]}")
        print('Введите новое значение: ')
        data[number-1] = input()
        notfind = False
    elif notfind:
       print(f'\nКонтакт под номером {number} не найден.\nКоличество контактов в списке: {len(data)}\n')
    return data