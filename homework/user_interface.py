def start():
    greetings = 'Добро пожаловать в телефонную книгу.\nВы можете создать новый контакт,\
 найти контакт, изменить или удалить, а также показать все контакты.'
    print(f'{greetings}')


def menu():
    print('\nВыберите соответствующую цифру в меню: \n')
    new_book = '0. Создать новую книгу или очистить существующую'
    new_contact = '1. Добавить новый контакт'
    change_number = '2. Изменить номер телефона'
    change_surname = '3. Изменить фамилию'
    delete_contact = '4. Удалить контакт'
    view_all = '5. Показать все контакты'
    export_file = '6. Экспортировать контакты в файл'
    exit_book = '7. Выход'
    print(f'{new_book}\n{new_contact}\n{change_number}\n{change_surname}\n{delete_contact}\n'
          f'{view_all}\n{export_file}\n{exit_book}')
    return digit_check()


def digit_check():
    try:
        input_number = int(input('Введите число: \n'))
        return input_number
    except ValueError:
        print('Это должно быть число\n')
        return digit_check()
