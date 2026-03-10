from flask import Flask, render_template

app = Flask(__name__)

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

# Конфигуратор
@app.route('/configurator')
def configurator():
    return render_template('configurator.html')

# Страница сборок
@app.route('/sborki')
def sborki():
    return render_template('sborki.html')

# Страница контактов
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)