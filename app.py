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
        if username == "admin" and password == "admin":  
            return redirect('/dashboard')  # Пренасочва към dashboard след успешен логин
        else:
            return "Invalid username or password", 403  # Грешка при логин
    return render_template('login.html')  # Зарежда login.html при GET заявка

# Страница за Dashboard (след логин)
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# За качване на скоркарта
@app.route('/upload-scorecard')
def upload_scorecard():
    return render_template('upload_scorecard.html')  # Ще създадем тази страница

# За преглед на стари скоркарти
@app.route('/view-scorecards')
def view_scorecards():
    return render_template('view_scorecards.html')  # Ще създадем тази страница

# За избор на седмица и преглед
@app.route('/review-week', methods=['GET'])
def review_week():
    selected_week = request.args.get('week')
    # Обработи избора на седмица и покажи съответната информация
    return render_template('review_week.html', week=selected_week)

# За топ 5 най-слабо представящи се
@app.route('/top-5')
def top_5():
    return render_template('top_5.html')  # Ще добавим съдържание за топ 5

if __name__ == '__main__':
    # Настройване на Flask да слуша на 0.0.0.0 и да използва правилния порт
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))