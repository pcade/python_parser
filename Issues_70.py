#!/bin/python3
# Encoding = UTF-8
#--------------------------------------------------------------------
# Автор:  Григорий Пахомов
# Версия: 0.1
# Дата:   27.05.2023
#====================================================================

#====================================================================
# Импорт модулей и определение глабальных констант и переменных
#====================================================================
import sys
import os
import json
import xml.etree.ElementTree as ET
from xml.dom.minidom import parse

#====================================================================
# Глобальные переменные
#====================================================================
path_1 = '/opt/upiter/plot/task/bin/etc/config'
path_2 = '/opt/upiter/plot/task/doka/_config'

file_1 = 'json'
file_2 = 'broker.xml'
file_3 = 'doka.ini'
file_4 = 'doka.log.json'
file_5 = str(os.popen(f"ls {path_1}| grep {file_1}").read().rstrip()).split('\n')

IS_CEF_LOG = "IS_CEF_LOG"
IS_DBG_LOG = "IS_DBG_LOG"
IS_SQL_LOG = "IS_SQL_LOG"

#====================================================================
# Функция проверки наличия дирректории
#====================================================================
def dir_path() -> bool:
    a = 0
    if os.path.isdir(path_1) == False:
        print(f'{path_1} отсутствует')
        a += 1 
    if os.path.isdir(path_2) == False:
        print(f'{path_2} отсутствует')
        a += 1
    if a > 0:
        return(False)
    return(True)

#====================================================================
# Функция проверки наличия файлов
#====================================================================
def is_file() -> bool:
    a = 0
    if os.path.isfile(path_1 + '/' + file_5[0]) == False:
        print(f'Файлы {file_1} в дирректории {path_1} отсутствуют')
        a += 1
    if os.path.isfile(path_1 + '/' + file_2) == False:
        print(f'Файл {file_2} в дирректории {path_1} отсутствуют')
        a += 1
    if os.path.isfile(path_2 + '/' + file_3) == False:
        print(f'Файл {file_3} в дирректории {path_2} отсутствуют')
        a += 1
    if os.path.isfile(path_2 + '/' + file_3) == False:
        print(f'Файл {file_4} в дирректории {path_2} отсутствуют')
        a += 1
    if a > 0:
        return(False)
    return(True)

#====================================================================
# Функция проверки уровня логирования
#====================================================================
def first_function() -> bool:
    if parser_json_function() == False:
        print('parser_json_function() - что-то не так')
        pass
    if parser_xml_fuction() == False:
        print('parser_xml_fuction() - что-то не так')
        pass
    if parser_doka() == False:
        print('parser_doka() - что-то не так')
        pass

# Функция парсинг json
def parser_json_function() -> bool:
    x = 0
    while len(file_5) > x:  
        with open(path_1 + '/' + file_5[x], 'r') as handle:
            json_load = json.load(handle)
            if 'log' not in json_load:
                print(f"Файл {file_5[x]} - не содержит level")
                x += 1
            else:
                print(f"Файл {file_5[x]} level = {json_load['log']['file']['level']}")
        x += 1
    return(True)

# Функция парсинг xml
def parser_xml_fuction() -> bool:
    tree = ET.parse(path_1 + '/' + file_2)
    root = tree.getroot()
    for group in root.findall('broker'):
      title = group.find('log')
      titlephrase = title.find('level').text
      return(True and print(f'{file_2} значение параметра <level> - {titlephrase}'))

# Фунция парсинг ini
def parser_doka() -> bool:

    a = 0
    b = 0
    c = 0

    with open(path_2 + '/' + file_3, 'r') as doka:
        lst = doka.readlines()

    for i in lst:
        if IS_CEF_LOG in i:
            a += 1
            print(i.rstrip())
        if IS_DBG_LOG in i:
            b += 1
            print(i.rstrip())
        if IS_SQL_LOG in i:
            c += 1
            print(i.rstrip())

    if a < 1:
        print(f'{IS_CEF_LOG} не достуен')
        pass
    if b < 1:
        print(f'{IS_DBG_LOG} не достуен')
        pass
    if c < 1:
        print(f'{IS_SQL_LOG} не достуен')
        pass
    return(True)

# Функция парсинг log.json
def parser_doka_json_function() -> bool:
    with open(path_2 + '/' + file_4, 'r') as handle:
        json_load = json.load(handle)
        if 'level' not in json_load:
            print(f"Файл {file_4} - не содержит level")
        else:
            print(f"Файл {file_4} level = {json_load['level']}")
    return(True)

#====================================================================
# Функция Установка максимального уровня логирования
#====================================================================
def second_function() -> bool:
    if mask_json_function(6) == False:
        print('mask_json_function(6) - что-то не так')
        pass
    if mask_xml_function(4) == False:
        print('mask_xml_function(4) - что-то не так')
        pass
    if worker_doka('y') == False:
        print('worker_doka() - что-то не так')
        pass
    if mask_doka_json_function(6) == False:
        print('mask_doka_json_function(6) - что-то не так')
        pass
    return(True)

# Функция установка значения маски в json
def mask_json_function(mask) -> bool:
    x = 0
    while len(file_5) > x:
        with open(path_1 + '/' + file_5[x], 'r') as handle:
            json_load = json.load(handle)
            if 'log' not in json_load:
                print(f"Файл {file_5[x]} - не содержит level")
                x += 1
            else:
                json_load['log']['file']['level'] = str(mask)
                with open(path_1 + '/' + file_5[x], 'w') as handle:
                    json.dump(json_load, handle, ensure_ascii=False, indent=4)
                print(f"Файл {file_5[x]} level = {json_load['log']['file']['level']}")
        x += 1
    return(True)

# Функция установки значения маски в xml
def mask_xml_function(mask) -> bool:
    file_name = path_1 + '/' + file_2
    doc = parse(file_name)
    node = doc.getElementsByTagName('level')
    node[0].firstChild.nodeValue = str(mask)
    xml_file = open(file_name, "w")
    doc.writexml(xml_file, encoding="utf-8")
    xml_file.close()
    return(True and print(f"Файл {file_2} level = {mask}"))

# Функция установки значения в doka
def worker_doka(sign) -> bool:

    a = 0
    b = 0
    c = 0
    with open(path_2 + '/' + file_3, 'r') as doka:
        lst = doka.readlines()

    for i in lst:
        if IS_CEF_LOG in i:
            replace_doka(i, sign)
            a += 1
            print(i.rstrip())
        if IS_DBG_LOG in i:
            replace_doka(i, sign)
            b += 1
            print(i.rstrip())
        if IS_SQL_LOG in i:
            replace_doka(i, sign)
            c += 1
            print(i.rstrip())

    if a < 1:
        print(f'{IS_CEF_LOG} не достуен')
        if write_doka(IS_CEF_LOG, sign) == False:
            print(f'{IS_CEF_LOG} вы отказались записать')
        pass
    if b < 1:
        print(f'{IS_DBG_LOG} не достуен')
        if write_doka(IS_DBG_LOG, sign) == False:
            print(f'{IS_DBG_LOG} вы отказались записать')
        pass
    if c < 1:
        print(f'{IS_SQL_LOG} не достуен')
        if write_doka(IS_SQL_LOG, sign) == False:
            print(f'{IS_SQL_LOG} вы отказались записать')
        pass
    return(True)

def replace_doka(name, sign):
    fin = open(path_2 + '/' + file_3, 'rt')
    data = fin.read()
    data = data.replace(name, name[0:-2] + str(sign) + name[-1:])
    fin.close()
    fin = open(path_2 + '/' + file_3, 'wt')
    fin.write(data)
    fin.close()

def write_doka(name, sign) -> bool:
    if input('Желаете дозаписать? - y/n ?') == 'Y' or 'y':
        fin = open(path_2 + '/' + file_3, 'rt')
        data = fin.read()
        data = data.replace('[LOGS]\n', '[LOGS]\n' + name + '=' + str(sign) + '\n')
        fin.close()
        fin = open(path_2 + '/' + file_3, 'wt')
        fin.write(data)
        fin.close()
        return(True)
    return(False)

# Функция установки значения в doka.json
def mask_doka_json_function(mask) -> bool:
    with open(path_2 + '/' + file_4, 'r') as handle:
        json_load = json.load(handle)
        if 'level' not in json_load:
            print(f"Файл {file_4} - не содержит level")
        else:
            json_load['level'] = str(mask)
            with open(path_2 + '/' + file_4, 'w') as handle:
                json.dump(json_load, handle, ensure_ascii=False, indent=4)
            print(f"Файл {file_4} level = {json_load['level']}")
    return(True)

#====================================================================
# Функция Установка минимального уровня логирования
#====================================================================
def theard_function() -> bool:
    if mask_json_function(2) == False:
        print('mask_json_function(2) - что-то не так')
        pass
    if mask_xml_function(1) == False:
        print('mask_xml_function(1) - что-то не так')
        pass
    if worker_doka('n') == False:
        print('worker_doka() - что-то не так')
        pass
    if mask_doka_json_function(2) == False:
        print('mask_doka_json_function(2) - что-то не так')
        pass
    return(True)

#====================================================================
# Основная функция
#====================================================================
def main():
    if dir_path() == False:
        return(False)
    if is_file() == False:
        return(False)
    if len(sys.argv) == 2:
        if sys.argv[1] == '1':
            first_function()
            return(True)
        if sys.argv[1] == '2':
            second_function()
            return(True)
        if sys.argv[1] == '3':  
            theard_function()
            return(True)
    print('Для запуска подставь ключ от 1-3')
    return(False)

#====================================================================
# Главный модуль
#====================================================================
if __name__ == "__main__":
    main()