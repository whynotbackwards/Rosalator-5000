import time
from printer import welcomer, intro, age_calcer, choicer, robo_print, request_date, request_time
from printer import farewell, empty_input, invalider, invalids

from imports import dt, birthtime
from src.secrets.secret_roses import rose_randomizer


def main():
    """Runs main program."""
    welcomer()

    intro()

    curr_dt = dt.now()
    age_calcer(curr_dt)

    choice = ''
    rose_pic_i = -1
    invalid_i = 0

    while choice != '4':
        choice = choicer()
        robo_print('')
        robo_print('')

        if choice == '1':
            invalid_i = 0
            curr_dt_new = dt.now()
            age_calcer(curr_dt_new)
        elif choice == '2':
            invalid_i = 0
            input_date = request_date()
            if input_date != '':
                input_time = request_time(input_date)
                if input_time == '':
                    input_time = f'{birthtime} AM'
                new_dt = dt.strptime(input_date + ' ' + input_time, '%m/%d/%Y %I:%M:%S %p')
                age_calcer(new_dt, custom=True)
        elif choice == '3':
            invalid_i = 0
            rose_pic, rose_pic_i = rose_randomizer(rose_pic_i)
            robo_print(rose_pic)
            robo_print('\n')
            time.sleep(2)
        elif choice == '4':
            invalid_i = 0
            farewell()
        elif choice == '':
            empty_input()
        else:
            invalider(invalid_i)
            invalid_i += 1
            if invalid_i == len(invalids):
                choice = '4'
                farewell()
