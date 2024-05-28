import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''

totalpass = input('Количество Паролей для генерации  ')
lenpass = input('Длина одного пароля   ')
digits_pass = input('Включать ли цифры?   ')
if digits_pass == 'да' or digits_pass == 'Да' or digits_pass == 'Yes' or digits_pass == 'yes':
    chars = chars+digits
uppercase_letters_pass = input('Включать ли прописные буквы?   ')
if uppercase_letters_pass == 'да' or uppercase_letters_pass == 'Да' or uppercase_letters_pass == 'Yes' or uppercase_letters_pass == 'yes':
    chars = chars+lowercase_letters
lowercase_letters_pass = input('Включать ли строчные буквы?   ')
if lowercase_letters_pass == 'да' or lowercase_letters_pass == 'Да' or lowercase_letters_pass == 'Yes' or lowercase_letters_pass == 'yes':
    chars = chars+uppercase_letters
punctuation_pass = input('Включать ли символы?   ')
if punctuation_pass == 'да' or punctuation_pass == 'Да' or punctuation_pass == 'Yes' or punctuation_pass == 'yes':
    chars = chars+punctuation
difsimbols_pass = input('Исключать ли неоднозначные символы il1Lo0O   ')
if difsimbols_pass == 'да' or difsimbols_pass == 'Да' or difsimbols_pass == 'Yes' or difsimbols_pass == 'yes':
    dif = 'il1Lo0O'
    for i in range(len(dif)):
        chars = chars.replace('dif(i)', '')

user_password = ''

def generate_password(lenpass,chars):
    global user_password
    for _ in range(int(lenpass)+1):
        r = random.randrange(len(chars))
        user_password = user_password+chars[r]
    return user_password

for _ in range(1, int(totalpass)+1):
    print(generate_password(lenpass,chars))
    user_password = ''
