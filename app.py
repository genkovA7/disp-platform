from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Добре дошъл в D.I.S.P.!"

if __name__ == '__main__':
    app.run(debug=True)