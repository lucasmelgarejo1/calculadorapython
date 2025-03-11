from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        data = request.get_json()
        operacion = data.get('operacion')
        num1 = float(data.get('num1'))
        num2 = float(data.get('num2', 0))

        resultado = None
        if operacion == 'suma':
            resultado = num1 + num2
        elif operacion == 'resta':
            resultado = num1 - num2
        elif operacion == 'multiplicacion':
            resultado = num1 * num2
        elif operacion == 'division':
            resultado = num1 / num2 if num2 != 0 else 'Error: División por 0'
        elif operacion == 'potencia':
            resultado = math.pow(num1, num2)
        elif operacion == 'raiz':
            resultado = math.sqrt(num1) if num1 >= 0 else 'Error: Raíz de número negativo'
        elif operacion == 'logaritmo':
            resultado = math.log(num1) if num1 > 0 else 'Error: Logaritmo de número no positivo'
        
        return jsonify({'resultado': resultado})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
