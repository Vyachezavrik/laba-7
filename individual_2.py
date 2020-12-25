#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Использовать словарь, содержащий следующие ключи:
#название пункта назначения рейса;
#номер рейса;
#тип самолета.
#Написать программу, выполняющую следующие действия:
#ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
#записи должны быть упорядочены по возрастанию номера рейса;
#вывод на экран номеров рейсов и типов самолетов, вылетающих в пункт назначения, название которого совпало с названием,введенным с клавиатуры;
#если таких рейсов нет, выдать на дисплей соответствующее сообщение.

import json
import sys

if __name__ == '__main__':
    # Список работников.
    flights = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ")

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о самолётах.
            num = int(input("Номер рейса? "))
            typ = (input("Тип самолёта? "))
            place = input("Пункт назначения рейса? ")

            # Создать словарь.
            flight = {
                'num': num,
                'typ': typ,
                'place': place,
            }

            # Добавить словарь в список.Ф
            flights.append(flight)
            # Отсортировать список в случае необходимости.
            if len(flights) > 1:
                flights.sort(key=lambda item: item.get('num', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 25
            )
            print(line)
            print('| {:^4} | {:^30} | {:^20} | {:^25} |'.format(
                "№",
                "Номер рейса? ",
                "Тип самолёта? ",
                "Пункт назначения рейса? "))
            print(line)

            # Вывести данные о всех рейсах.
            for idx, flight in enumerate(flights, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:<25} |'.format(
                        idx,
                        flight.get('num', 0),
                        flight.get('typ', ''),
                        flight.get('place', '')
                    )
                )
            print(line)

        elif command.startswith('select '):
            # Разбить команду на части для выделения пункта назначения.
            plane = command.split(' ', maxsplit=1)
            # Инициализировать счетчик.
            count = 0
            # Проверить сведения рейсов из списка.
            for flight in flights:
                if plane[1] == flight.get('place'):
                    count += 1
                    print('{:>4}: Номер самолёта - {}, Тип самолёта - {}'.format(count, flight.get('num', ''), flight.get('typ', '')))
                # Если счетчик равен 0, то работники не найдены.
            if count == 0:
                print("Таких пунктов назначения не найдено.")
        elif command.startswith('load '):
            # Разбить команду на части для выделения пункта назначения.
            plane = command.split(' ', maxsplit=1)

            #Посчитать данные из файла JSON
            with open(plane[1], 'r') as f:
                flights = json.load(f)

        elif command.startswith('save '):
            # Разбить команду на части для выделения имени файла.
            plane = command.split(' ', maxsplit=1)
            # Сохранить данные в файл JSON.
            with open(plane[1], 'w') as f:
                json.dump(flights, f)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить рейс;")
            print("list - вывести список рейсов;")
            print("select <Пункт назначения рейса> - запросить нужный рейс;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
