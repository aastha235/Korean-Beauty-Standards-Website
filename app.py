from flask import Flask, render_template, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        if 'num1' not in data or 'num2' not in data:
            raise ValueError('Both numbers must be provided')
        
        num1 = int(data['num1'])
        num2 = int(data['num2'])
        result = num1 + num2
        return jsonify({'result': result})
    except ValueError as e:
        return jsonify({'error': str(e)})
    except Exception as e:
        return jsonify({'error': str(e)})
        
if __name__ == '__main__':
    app.run(debug=True)
