import json
import controller
db_path = 'db.json'


def export_txt():
    with open(db_path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            with open('exported_contacts.txt', 'a') as export:
                export.write('\n' + "".join(data[i]['Name']) + ' ' + "".join(data[i]['Surname']) + ' '
                             + "".join(data[i]['Phone number']) + ' ' + "".join(data[i]['Comment']))

    print('\nКонтакты успешно экспортированы в файл!\n')
    controller.user_choice()
