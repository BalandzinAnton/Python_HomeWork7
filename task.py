# Составить расписание через консольного бота
import sys
weekdays = {1: 'Monday.txt', 2: 'Tuesday.txt', 3: 'Wednesday.txt',
            4: 'Thursday.txt', 5: 'Friday.txt', 6: 'Saturday', 7: 'Sunday'}
def add_schedule(my_weekdays):
    do_next = ''
    while do_next != ' ':
        schedule_change = int(input('Enter 1 to read, 2 - to add, 3 - to change \n'))
        if schedule_change == 1:
            day = int(input('Enter day of week (from 1 to 7) \n'))
            with open(my_weekdays[day], 'r', encoding='utf-8') as my_f:
                print(my_f.readlines())
                do_next = input('Введите ENTER (или др.) для продолжения записей '
                                'или ПРОБЕЛ для ВЫХОДА ')
        elif schedule_change == 2:
            day = int(input('Enter day of week (from 1 to 7) \n'))
            event = input('What event do U like to add? \n')
            time = input('What time to add this event \n')

            with open(my_weekdays[day], 'a', encoding='utf-8') as my_f:
                my_f.writelines(f'{time} - {event} \n')
                #my_f.write(event)
                do_next = input('Введите ENTER (или др.) для продолжения записей '
                                'или ПРОБЕЛ для ВЫХОДА ')
        elif schedule_change == 3:
            day = int(input('Enter day of week (from 1 to 7) \n'))
            event = input('What event do U like to add? \n')
            with open(my_weekdays[day], 'w', encoding='utf-8') as my_f:
                my_f.write(event)
            do_next = input('Введите ENTER (или др.) для продолжения записей '
                                'или ПРОБЕЛ для ВЫХОДА ')
        elif schedule_change > 3 or schedule_change < 1:
            return print('Выбранная опция отсутствует')

add_schedule(weekdays)

