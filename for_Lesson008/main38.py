import csv
def main():
    
    phonebook = []
    with open('phonebook.txt', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            phonebook.append(row)

    while True:
        print("####[PHONE BOOK]####")
        print("1. Показать все контакты")
        print("2. Найти контакт по имени")
        print("3. Найти контакт по фамилии")
        print("4. Изменить контакт")
        print("5. Удалить контакт")
        print("6. Добавить контакт")
        print("7. Экспортировать в файл")
        print("8. Выйти")
        
        choice = input("Введите номер действия, которое вы хотите выполнить: ")
        
        if choice == "1":
            show_all(phonebook)
        elif choice == "2":
            name = input("Введите имя: ")
            find_by_name(phonebook, name)
        elif choice == "3":
            surname = input("Введите фамилию: ")
            find_by_surname(phonebook, surname)
        elif choice == "4":
            name = input("Введите имя: ")
            update_entry(phonebook, name)
        elif choice == "5":
            name = input("Введите имя: ")
            delete_entry(phonebook, name)
        elif choice == "6":
            add_entry(phonebook)
        elif choice == "7":
            export_to_file(phonebook)
        elif choice == "8":
            print("До свидания!")
            break
        else:
            print("Пожалуйста, выберите корректное действие")

def show_all(phonebook):
    print("Контакты:")
    for row in phonebook:
        print(row)

def find_by_name(phonebook, name):
    for row in phonebook:
        if row['Имя'] == name:
            print(row)

def find_by_surname(phonebook, surname):
    for row in phonebook:
        if row['Фамилия'] == surname:
            print(row)

def update_entry(phonebook, name):
    for row in phonebook:
        if row['Имя'] == name:
            new_number = input("Введите новый номер телефона: ")
            row['Номер телефона'] = new_number
            print("Контакты обновлены")

def delete_entry(phonebook, name):
    for row in phonebook:
        if row['Имя'] == name:
            phonebook.remove(row)
            print("Контакт удален...")

def add_entry(phonebook):
    new_entry = {}
    new_entry['Фамилия'] = input("Введите фамилию: ")
    new_entry['Имя'] = input("Введите имя: ")
    new_entry['Отчество'] = input("Введите отчество: ")
    new_entry['Номер телефона'] = input("Введите номер телефона: ")
    phonebook.append(new_entry)
    print("Контакт добавлен")

def export_to_file(phonebook):
    with open('phonebook.txt', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['Фамилия', 'Имя', 'Отчество', 'Номер телефона'])
        writer.writeheader()
        for row in phonebook:
            writer.writerow(row)
            print("Контакты экспортированы в файл")
        
if __name__ == '__main__':
    main()
