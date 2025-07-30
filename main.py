from tkinter import *
from tkinter import filedialog as fd
import json
import csv
from os import path



def openFile():
    filename = fd.askopenfilename()
    if filename != '':
        with open(filename) as file:  # открываем и читаем файл-список хостов
            data = file.read()
        load_label = Label(root, text=f'Файл {filename} загружен.').pack()

        data = json.loads(data)  # загружаем прочитанную информацию в библиотеку json

        result = [('Host name', 'service1', 'service2', 'service3'), ]  # Создаем список результатов

        host_info = [0, 0, 0, 0]
        for key, value in data.items():
            services = value['services']
            host_info[0] = key
            for service in services:
                if 'service1' in service:
                    if service['service1'] == 'n/a':
                        host_info[1] = 'Служба не отвечает'
                    else:
                        host_info[1] = service['service1']
                elif 'service2' in service:
                    if service['service2'] == 'n/a':
                        host_info[2] = 'Служба не отвечает'
                    else:
                        host_info[2] = service['service2']
                elif 'service3' in service:
                    if service['service3'] == 'n/a':
                        host_info[3] = 'Служба не отвечает'
                    else:
                        host_info[3] = service['service3']
            result.append(host_info)  # Добавляем в результат список-инфо по конкретному хосту
            host_info = [0, 0, 0, 0]
        name_path, del_path = path.splitext(filename)
        result_file_name = name_path + '_parser' + '.csv'
        with open(result_file_name, 'w', newline='') as result_file:  # записываем результат в csv-файл
            writer = csv.writer(result_file)
            writer.writerows(result)
            result_label = Label(root, text='Результат готов, файл сохранен рядом с загружаемым файлом(К имени добавлен _parser).').pack()
    else:
        warning_label = Label(root, text='Вы не выбрали файл', fg='red', font='Helvetica 18 bold').pack(pady=(30, 30))

root = Tk()

root.title('Crawler parser')
root.geometry('800x400')
info_label = Label(root, text='Программа для форматирования json-файла мониторинга crawler в читабельный csv-файл.', font='Helvetica 11 bold').pack(pady=(30))
info_label2 = Label(root, text='Выберите json-файл', font='Helvetica 11 bold').pack(pady=(10))
button = Button(root, text="Открыть файл", command=openFile, font='Helvetica 9 bold', width=15, height=3)
button.pack(pady=(50, 25))


root.mainloop()

