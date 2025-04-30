from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

# Начална страница
@app.route('/')
def home():
    return render_template('index.html')

# Страница за логин
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Пример за фиксиран логин (можеш да го замениш с база данни)
        if username == "admin" and password == "admin":  # Пример за проверка
            return redirect('/dashboard')  # Пренасочва към dashboard след успешен логин
        else:
            return "Invalid username or password", 403  # Грешка при логин
    return render_template('login.html')  # Зарежда login.html при GET заявка

# Страница за Dashboard (след логин)
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)  # Включи debug, за да виждаш допълнителни грешки