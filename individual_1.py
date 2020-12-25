#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Написать программу, которая считывает английский текст из файла и выводит на экран
#слова, начинающиеся с гласных букв.

if __name__ == '__main__':
    with open('text_individual_1.txt', 'r') as f:
        text = f.read().lower()

    words = text.split(' ')
    a = ["e", "y", "u", "i", "o", "a"]
    print(words)
    b = [word for word in words if word[0] in a]
    print(b)