#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    def comm_add():
        city = input("город назначения ")
        nfly = ''
        while not nfly.isdigit():
            nfly = input("номер рейса ")
        numfly = int(nfly)
        typea = input("тип самолета ")

        flylistdic = {
            'city': city,
            'numfly': numfly,
            'typea': typea,
        }

        flylist.append(flylistdic)
        if len(flylist) > 1:
            flylist.sort(key=lambda item: item.get('city', ''))


    def comm_list():
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                "№",
                "Город ",
                "Номер рейса",
                "Тип ВС"
            )
        )
        print(line)
        for idx, flylistdic in enumerate(flylist, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                    idx,
                    flylistdic.get('city', ''),
                    flylistdic.get('numfly', '0'),
                    flylistdic.get('typea', '')
                )
            )
        print(line)


    def comm_plane():
        destplane = input("тип самолёта ")

        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                "№",
                "Город ",
                "Номер рейса",
                "Тип ВС"
            )
        )
        print(line)
        yesfly = -1
        for idx, flylistdic in enumerate(flylist, 1):
            if flylistdic.get('typea', '') == destplane:
                yesfly = 1
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                        idx,
                        flylistdic.get('city', ''),
                        flylistdic.get('numfly', '0'),
                        flylistdic.get('typea', '')
                    )
                )
        print(line)
        if yesfly == -1:
            print('тип ', destplane, 'не выполняет рейсов ')


    def comm_help():
        print("Список команд:\n")
        print("add - добавить рейс;")
        print("list - вывести весь список рейсов;")
        print("plane - вывести типы самолётов;")
        print("help - отобразить справку;")
        print("exit - завершить работу с программой.")


    flylist = []
    while True:
        command = input(">>> ").lower()
        if command == 'exit':
            break

        elif command == 'add':
            comm_add()

        elif command == 'list':
            comm_list()

        elif command == 'plane':
            comm_plane()

        elif command == 'help':
            comm_help()
            
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
