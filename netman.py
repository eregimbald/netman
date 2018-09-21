#!/usr/bin/python3.6

import sys
import yaml

pictures = yaml.load(open('boom.yml'))

secret = 'hairpinning'
health = 15
status_list = ['no_problem','hmmm','probably_nothing','do_you_smell_that','cpu_99','march_2018']
answer = ''

print(pictures['router_health']['no_problem'])

while True:
    answer += input('Guess a letter: ')
    temp = ''
    for char in secret:
        if char in answer:
            print(char, end='')
        else:
            print('_', end='')
    print()
    health -= 1
    if health > 12:
        print(pictures['router_health'][status_list[0]])
    elif health > 9:
        print(pictures['router_health'][status_list[1]])
    elif health > 6:
        print(pictures['router_health'][status_list[2]])
    elif health > 3:
        print(pictures['router_health'][status_list[3]])
    elif health > 0:
        print(pictures['router_health'][status_list[4]])
    else:
        print(pictures['router_health'][status_list[5]])
        sys.exit()