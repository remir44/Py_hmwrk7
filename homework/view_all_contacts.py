import json
import controller
db_path = 'db.json'


def view_all_contacts():
    with open(db_path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            print(data[i])
    controller.user_choice()
