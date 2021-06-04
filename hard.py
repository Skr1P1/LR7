#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Самостоятельно изучить возможности модуля xml стандартной библиотеки Python. Выполнить
# задание 2 данной лабораторной работы, в котором вместо сохранения и чтения данных из
# файла формата JSON реализовано сохранение и чтение данных в файл формата XML.

if __name__ == '__main__':
    tree = ET.parse(r'F:\S_P\Учёба\ОКП Маша\7\test.xml')
    tree
    root = tree.getroot()
    for child in root.findall('country'):
        rank = child.find('rank').text
        name = child.get('name')
        print(name, rank)

    a = ET.Element('')
    tree = ET.ElementTree(a)
    tree.write(r'F:\S_P\Учёба\ОКП Маша\7\test.xml')

    a = ET.Element('a')
    b = ET.SubElement(a, 'b')
    c = ET.SubElement(a, 'c')
    d = ET.SubElement(a, 'd')
    tree = ET.ElementTree(a)
    tree.write(r'F:\S_P\Учёба\ОКП Маша\7\test.xml')