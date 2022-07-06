from imports import time, sys, version, dt
from imports import name, first_name, birthday, birthtime, wgt, ht
from date_calcer import date_calcer


def robo_print(obj, sleep=0.03, newline=True):
    """Prints out string inputs character by character, and faster if the input is a list."""
    for item in obj:
        if type(obj) == str:
            print(item, end='', flush=True)
            sys.stdout.flush()
            if item != ' ':
                time.sleep(sleep)
                sys.stdout.flush()
        elif type(obj) == list:
            robo_print(item, sleep=0.01)
    if newline:
        print(flush=True)
    sys.stdout.flush()


def welcomer():
    """Prints welcome text."""
    sep = '################################################################'
    welcome = "  Welcome to the Rosalator 5000!"
    version_print = f"  Version {version}"
    robo_print('\n')
    robo_print(sep, sleep=0.01)
    robo_print(welcome)
    robo_print(version_print)
    robo_print(sep, sleep=0.01)
    robo_print('\n')
    time.sleep(1)


def intro():
    """Prints introduction text."""
    curr_time = dt.now()
    curr_hr = curr_time.hour

    if curr_hr < 12:
        time_of_day = 'morning'
    elif curr_hr < 17:
        time_of_day = 'afternoon'
    else:
        time_of_day = 'evening'

    birthdate = dt.strptime(birthday + ' ' + birthtime, '%Y-%m-%d %H:%M:%S')
    bd_str = dt.strftime(birthdate, '%A, %B %d, %Y')
    bt_str = dt.strftime(birthdate, '%H:%M %p')

    first_line = f"Good {time_of_day}! {name} was born on {bd_str} at {bt_str}."
    second_line = f"She was {wgt}, and {ht}. "
    third_line_1 = '... '
    third_line_2 = "She's much bigger now."

    robo_print(first_line)
    time.sleep(0.5)
    robo_print(second_line, newline=False)
    time.sleep(0.5)
    robo_print(third_line_1, sleep=0.1, newline=False)
    time.sleep(1)
    robo_print(third_line_2)
    time.sleep(1)
    robo_print('')
    robo_print('')
    time.sleep(0.5)


def pluralizer(age):
    """Returns an 's' for the end of the word to pluralize it if time value isn't 1."""
    return 's' if age != 1 else ''


def or_sep(r):
    """Returns 'OR' with number of R's based on input value."""
    return f"\n        O{'R' * r}\n"


def age_calcer(new_dt, custom=False):
    """Prints formatted age calculation results."""
    new_day = dt.strftime(new_dt, '%A, %B %d, %Y')
    new_time = dt.strftime(new_dt, '%I:%M:%S %p')

    if new_dt > dt.now():
        time_machine = 'future'
    else:
        time_machine = 'past'

    yrs, mos, mos_tot, days_mo, days_tot, hrs, mins, secs, weeks, days_wks = date_calcer(new_dt)

    if custom:
        if time_machine == 'future':
            first_line = f"Welcome to the future. The day is {new_day}, and it is {new_time}. "
        else:
            first_line = f"Way back in the distant past, the day is {new_day}, and it is {new_time}. "
    else:
        first_line = f"Today is {new_day}, and it is {new_time}. "

    second_line = f"This means {first_name} is...\n"

    age_full = f"    - {str(yrs)} year{pluralizer(yrs)}, {str(mos)} month{pluralizer(mos)}, {str(days_mo)} " \
               f"day{pluralizer(days_mo)}, {str(hrs)} hour{pluralizer(hrs)}, {str(mins)} minute{pluralizer(mins)}, " \
               f"and {str(secs)} second{pluralizer(secs)} old"

    age_months = f"    - {str(mos_tot)} month{pluralizer(mos_tot)}, {str(days_mo)} day{pluralizer(days_mo)}, " \
                 f"{str(hrs)} hour{pluralizer(hrs)}, {str(mins)} minute{pluralizer(mins)}, and {str(secs)} " \
                 f"second{pluralizer(secs)} old"

    age_days = f"    - {str(days_tot)} day{pluralizer(days_tot)}, {str(hrs)} hour{pluralizer(hrs)}, {str(mins)} " \
               f"minute{pluralizer(mins)}, and {str(secs)} second{pluralizer(secs)} old"

    age_weeks = f"    - {str(weeks)} week{pluralizer(weeks)}, {str(days_wks)} day{pluralizer(days_wks)}, {str(hrs)} " \
                f"hour{pluralizer(hrs)}, {str(mins)} minute{pluralizer(mins)}, and {str(secs)} " \
                f"second{pluralizer(secs)} old"

    robo_print(first_line, newline=False)
    robo_print(second_line)
    robo_print(age_full)
    robo_print(or_sep(1), sleep=0.1)
    robo_print(age_months)
    robo_print(or_sep(4), sleep=0.1)
    robo_print(age_days)
    robo_print(or_sep(8), sleep=0.1)
    robo_print(age_weeks)
    robo_print('\n')
    time.sleep(1)

    robo_print('Hit Enter to continue...', newline=False)
    input()
    robo_print('\n')


def choicer():
    """Asks the user to input what program option they want."""
    question = "What would you like to do next?"
    choice_1 = f"[1] Re-check {first_name}'s current age"
    choice_2 = f"[2] Check {first_name}'s age at a different date"
    choice_3 = "[3] ?????"
    choice_4 = "[4] Exit the program"

    input_prompt = "Enter in the number of your choice and hit enter:  "

    robo_print(question)
    robo_print('')
    time.sleep(0.5)
    robo_print(choice_1)
    robo_print(choice_2)
    robo_print(choice_3)
    robo_print(choice_4)
    robo_print('')
    robo_print(input_prompt, newline=False)

    choice = input()

    return choice


def request_date():
    """Asks user to input custom date."""
    request = f"Enter a date (M/D/YYYY or M/D/YY) to calculate {first_name}'s age, or leave blank to go back:  "

    while True:
        robo_print(request, newline=False)
        input_date = input()
        robo_print('')

        if input_date == '':
            return input_date
        else:
            try:
                dt.strptime(input_date, '%m/%d/%Y')
                if dt.strptime(input_date, '%m/%d/%Y') < dt.strptime(birthday, '%Y-%m-%d'):
                    robo_print("You can't check her age before she was born... Please try again.\n")
                    continue
                return input_date
            except ValueError:
                try:
                    dt.strptime(input_date, '%m/%d/%y')
                    if dt.strptime(input_date, '%m/%d/%y') < dt.strptime(birthday, '%Y-%m-%d'):
                        robo_print("You can't check her age before she was born... Please try again.\n")
                        continue
                    return dt.strftime(dt.strptime(input_date, '%m/%d/%y'), '%m/%d/%Y')
                except ValueError:
                    robo_print("Incorrect date format. Please try again.\n")


def request_time(input_date):
    """Asks user to input custom time (if wanted)."""
    request = f"Enter a time (HH:MM(:SS) AM/PM) to calculate {first_name}'s age, or leave blank for days only:  "

    while True:
        robo_print(request, newline=False)
        input_time = input()
        robo_print('')

        if input_time == '':
            return input_time
        else:
            try:
                if input_time.count(':') == 2:
                    dt.strptime(input_time, '%I:%M:%S %p')
                else:
                    dt.strptime(input_time, '%I:%M %p')
                    input_time = input_time[:-3] + ':00' + input_time[-3:].upper()
                if dt.strptime(input_date, '%m/%d/%Y') == dt.strptime(birthday, '%Y-%m-%d'):
                    if dt.strptime(input_time, '%I:%M:%S %p') < dt.strptime(birthtime, '%H:%M:%S'):
                        robo_print("You can't check her age before she was born... Please try again.\n")
                        continue
                return input_time
            except ValueError:
                robo_print("Incorrect time format. Please try again.\n")


def farewell():
    """Program exit sequence."""
    thank_you = "Thank you for using the Rosalator 5000! Have a nice day."
    self_destruct = "This program will self-destruct."

    robo_print(thank_you)
    time.sleep(1)
    robo_print(self_destruct)

    time.sleep(1)
    robo_print('')

    for x in range(5, -1, -1):
        robo_print(('... ' + str(x) if x != 5 else str(x)) + ' ', newline=False)
        time.sleep(1)


def empty_input():
    """Prints message when user does not enter an option."""
    seriously = "Are you serious? You didn't enter anything! Please try again.\n"
    time.sleep(0.5)
    robo_print(seriously)
    time.sleep(0.5)


invalids = ["Sorry, that's not one of the choices. Please try again.",
            "No seriously, you just have to enter a number: 1, 2, 3, or 4. Please try again.",
            "Stop it... This isn't funny. Please try again.",
            "OK, now you're just messing with me. Please try again.",
            "Come on! 1, 2, 3, or 4. How hard is that?! Please try again.",
            "I'm not playing anymore. But seriously, please try again.",
            "At this point, I'll choose for you. How about 2? That's a nice one. Please try again.",
            "I give up. Please try again. Please.",
            "Still not budging, eh? I'm warning you... Please try again.",
            "Last chance. I dare you to enter in something that isn't 1 through 4. Please try again.",
            "That's it! I'll choose for you. How about we end the program! I win!"]


def invalider(i):
    """Prints message when user enters an invalid choice."""
    robo_print(invalids[i])
    robo_print('')
    time.sleep(0.5)
