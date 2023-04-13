# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.


def add_person():
    last_name = input('Введите фамилию: ')
    name = input('Введите имя: ') 
    surname = input('Введите отчество: ') 
    phone = input('Введите номер телефона: ') 
    data = open('C:\\Users\\Uber\\Desktop\\Sem8\\file\\phonebook.txt', 'a', encoding='UTF-8')
    data.writelines([last_name, ' ',  name, ' ', surname, ' ', phone, '\n'])
    data.close()
#add_person()

def print_data():
    with open('C:\\Users\\Uber\\Desktop\\Sem8\\file\\phonebook.txt', 'r', encoding='UTF-8') as data:
        print(data.read())
# print_data()

def search():
    search_name = input('Введите данные для поиска: ')
    with open('C:\\Users\\Uber\\Desktop\\Sem8\\file\\phonebook.txt', 'r', encoding='UTF-8') as data:
        for line in data:
            if search_name in line:
                print(line)
# search() 

def load_data():
    with open('C:\\Users\\Uber\\Desktop\\Sem8\\file\\phonebook.txt', 'r+', encoding='UTF-8') as data:
        text_data = data.read()
        path = input('Введите адрес файла: ')
        with open(path, 'r', encoding='UTF-8') as data_2:
            for line in data_2:
                if line not in text_data:
                    data.write(line)
# load_data()

def del_person():
    del_name = input('Введите контакт, который нужно удалить: ')
    with open('C:\\Users\\Uber\\Desktop\\Sem8\\file\\phonebook.txt', 'r', encoding='UTF-8') as data:
        d = data.readlines()
        for i_line in range(len(d)):
            if del_name in d[i_line]:
                del d[i_line]
    with open('C:\\Users\\Uber\\Desktop\\Sem8\\file\\phonebook.txt', 'w', encoding='UTF-8') as data:
        for line in d:
            data.write(line)
            
def change_person():
    change_name = input('Введите данные контакта, который хотите изменить: ')
    last_name = input('Введите новую фамилию: ') 
    name = input('Введите новое имя: ') 
    surname = input('Введите новое отчество: ') 
    phone = input('Введите новый номер телефона: ')
    
    with open('C:\\Users\\Uber\\Desktop\\Sem8\\file\\phonebook.txt', 'r', encoding='UTF-8') as data:
        d = data.readlines()
    for i_line in range(len(d)):
        if change_name in d[i_line]:
            d[i_line] = last_name + ' ' + name + ' ' + surname + ' ' + phone + ' '
    
    with open('C:\\Users\\Uber\\Desktop\\Sem8\\file\\phonebook.txt', 'w', encoding='UTF-8') as data:
        for line in d:
            data.write(line)

def ui():
    print('''
    1 - Добавить контакт
    2 - Поиск
    3 - Импорт данных
    4 - Вывод в консоль
    5 - Удалить контакт
    6 - Изменить контакт
    ''')
    user_input = input('Введите действие: ')
    if user_input == '1':
        add_person()
    elif user_input == '2':
        search()
    elif user_input == '3':
        load_data()
    elif user_input == '4':
        print_data()
    elif user_input == '5':
        del_person()
    elif user_input == '6':
        change_person()

def main():
    ui()
    
if __name__ == "__main__":
    main() 

