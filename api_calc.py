from flask import Flask, request, jsonify

calc = Flask(__name__)

@calc.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    if 'a' in data and 'b' in data:
        a = data['a']
        b = data['b']
        result = a + b
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Missing parameters'}), 400

@calc.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()   
    if 'a' in data and 'b' in data:
        a = data['a']
        b = data['b']
        result = a - b
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Missing parameters'}), 400

@calc.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    if 'a' in data and 'b' in data:
        a = data['a']
        b = data['b']
        result = a * b
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Missing parameters'}), 400

@calc.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    if 'a' in data and 'b' in data:
        a = data['a']
        b = data['b']
        if b != 0:
            result = a / b
            return jsonify({'result': result})
        else:
            return jsonify({'error': 'Division by zero'}), 400
    else:
        return jsonify({'error': 'Missing parameters'}), 400

if __name__ == '__main__':
    calc.run(host="0.0.0.0",debug=True)
