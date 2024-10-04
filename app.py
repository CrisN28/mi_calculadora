from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    # Inicialmente, no hay resultado
    return render_template('index.html', result=None, show_message=False)


@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']
    result = None

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 / num2 if num2 != 0 else 'Error: División por cero'

    # Mostrar el mensaje "SIUUUUUU" solo después de la operación
    return render_template('index.html', result=result, show_message=True)


if __name__ == '__main__':
    app.run(debug=True)
