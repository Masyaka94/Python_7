def add_new():
    name = input('Имя: ')
    phone = input('Номер телефона: ')
    return (name, phone)


def find_phone():
    return input('Введите имя: ')


def nemu():
    return input('1 - Создать новый контакт\n'
                 '2 - Поиск контактов\n'
                 '3 - Экспорт контактов в формат txt\n'
                 '4 - Импорт контактов\n'
                 '5 - Удаление контакта\n'
                 '0 - Выход\n')

def delete_contact():
    return input('Введите имя: ')

def view_res(res):
    print(f"{res}\n")
