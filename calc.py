import re
from flask import Flask, request, render_template, flash

app = Flask(__name__)
app.secret_key = b'_5#L"F4Q8z\n\xec]/'

number_regex = re.compile(r'^\d+$')
ru_letters_regex = re.compile(r'[а-яёА-ЯЁ]')
en_letters_regex = re.compile(r'[a-zA-Z]')

@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        number = request.form['number']
        if bool(number_regex.search(number)):
            if int(number) % 2 == 0:
               flash('Число четное')
            else:
               flash('Число нечетное')
        elif number == '':
            flash('Поле не должно быть пустым')
        elif bool(ru_letters_regex.search(number)) or bool(en_letters_regex.search(number)):
            flash('Введите число')
        else:
            flash('Введите целое число')
    return render_template('main.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)