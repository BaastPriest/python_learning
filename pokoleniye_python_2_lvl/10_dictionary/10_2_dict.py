import re


def sum_min_max_keys():
    my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee', 7.1: 'ff', 0.12: 'qq', 1.91: 'aa',
               10.12: [1, 2, 3], 99.0: {9, 0, 1}}
    print(sum([min(my_dict), max(my_dict)]))
    """sum(min(my_dict), max(my_dict)) will be TypeError: 'float' object is not iterable"""


users_for_10_2 = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
                  {'name': 'Helga', 'phone': '555-1618'},
                  {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
                  {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
                  {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
                  {'name': 'John', 'phone': '233-421-32', 'email': ''},
                  {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
                  {'name': 'Alina', 'phone': '+7948-799-2434'},
                  {'name': 'Robert', 'phone': '420-2011', 'email': ''},
                  {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
                  {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
                  {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
                  {'name': 'Roman', 'phone': '+7459-145-8059'},
                  {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
                  {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
                  {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]


def names_users_phone_ends_with_8(users):
    users_for_sort = []
    for i in users:
        if i["phone"][-1] == "8":
            users_for_sort.append(i['name'])
    print(*sorted(users_for_sort))
    """result = [user['name'] for user in users if user['phone'].endswith('8')]
    print(*sorted(result))"""


def name_users_without_email(users):
    # result = [user['name'] for user in users if user['email'] in users and user['email'] == ""]
    users_no_email = []
    for i in users:
        if 'email' in i.keys() and i['email'] == "":
            users_no_email.append(i['name'])
        elif 'email' not in i.keys():
            users_no_email.append(i['name'])
    print(*sorted(users_no_email))
    """1) print(*sorted([k['name'] for k in users if 'email' not in k or k['email'] == '']))
       2) if 'email' not in n or n['email'] == '':  """


def string_representation(number):
    num_str_dict = {"0": "zero",
                    "1": "one",
                    "2": "two",
                    "3": "three",
                    "4": "four",
                    "5": "five",
                    "6": "six",
                    "7": "seven",
                    "8": "eight",
                    "9": "nine"}
    my_num = str(number)
    for c in my_num:
        print(num_str_dict[c], end=' ')
    """print(*[digits[key] for key in input()])"""


def displays_info_about_course_by_course_number(number, info):
    print(f'{number}: {info[number]["audience_number"]}, {info[number]["teacher"]}, {info[number]["time"]} ')
    """
    audience, teacher, time = my_dict[course_number]
    print(f'{course_number}: {audience}, {teacher}, {time}')
    """


course_info = {'CS101': {'audience_number': '3004', 'teacher': 'Tim', 'time': '8:00'},
               'CS102': {'audience_number': '4501', 'teacher': 'Maria', 'time': '9:00'},
               'CS103': {'audience_number': '6755', 'teacher': 'Robert', 'time': '10:00'},
               'NT110': {'audience_number': '1244', 'teacher': 'Rosa', 'time': '11:00'},
               'CM241': {'audience_number': '1411', 'teacher': 'Li', 'time': '13:00'}}


def pushbutton_phones_text_messages(text_msg, pushbtn_table):
    """
    a program that displays the keystrokes required to type a message
    :return:
    """
    allowed_chars = "".join(pushbutton_phone_table.values())
    pattern = f"[^{re.escape(allowed_chars)}]"
    filtered_text = re.sub(pattern, '', text_msg.upper())
    for target_letter in filtered_text:
        for key, value in pushbtn_table.items():
            if target_letter in value:
                index = value.index(target_letter) + 1
                print(str(key) * index, end="")


pushbutton_phone_table = {1: ".,?!:", 2: "ABC", 3: "DEF", 4: "GHI", 5: "JKL", 6: "MNO", 7: "PQRS", 8: "TUV", 9: "WXYZ",
                          0: " "}


def output_msg_encoded_morse_code_1(text, morse_code_table):
    allowed_chars = "".join(morse_code_table.keys())
    pattern = f"[^{re.escape(allowed_chars)}]"
    filtered_text = re.sub(pattern,'', text.upper())
    for letter in filtered_text:
        print(morse_code_table[letter],end=" ")


morse_code = {'A': '.-', 'J': '.---', 'S': '...', '1': '.----',
              'B': '-...', 'K': '-.-', 'T': '-', '2': '..---',
              'C': '-.-.', 'L': '.-..', 'U': '..-', '3': '...--',
              'D': '-..', 'M': '--', 'V': '...-', '4': '....-',
              'E': '.', 'N': '-.', 'W': '.--', '5': '.....',
              'F': '..-.', 'O': '---', 'X': '-..-', '6': '-....',
              'G': '--.', 'P': '.--.', 'Y': '-.--', '7': '--...',
              'H': '....', 'Q': '--.-', 'Z': '--..', '8': '---..',
              'I': '..', 'R': '.-.', '0': '-----', '9': '----.'}


def output_msg_encoded_morse_code_2(text):
    letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
    morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
             '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
             '...--', '....-', '.....', '-....', '--...', '---..', '----.']
    morse_dict = dict(zip(letters, morse))
    for c in text.upper():
        if c in morse_dict.keys():
            print(morse_dict[c], end=" ")


output_msg_encoded_morse_code_2("interstellar")