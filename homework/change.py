import json
import controller
db_path = 'db.json'


def change_phone_number():
    name = input('Введите имя или фамилию контакта, чей номер будем менять:  ')

    with open(db_path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if name == data[i]['Name'] or name == data[i]['Surname']:
                data[i]['Phone number'] = input('Новый телефон: ')
    with open(db_path, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)
    print('\nНомер успешно изменён!\n')
    controller.user_choice()


def change_surname():
    name = input('Введите имя или фамилию контакта, фамилию которого будем менять:  ')

    with open(db_path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if name == data[i]['Name'] or name == data[i]['Surname']:
                data[i]['Surname'] = input('Новая фамилия: ')
    with open(db_path, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)
    print('\nФамилия успешно изменена!\n')
    controller.user_choice()


def delete_contact():
    name = input('Введите имя или фамилию контакта, которого надо удалить:  ')

    with open(db_path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(data.index(data[-1])+1):
            if name == data[i]['Name'] or name == data[i]['Surname']:
                del data[i]
    with open(db_path, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)
    print('\nКонтакт успешно удалён!\n')
    controller.user_choice()
