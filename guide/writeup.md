## Python code
Создаем с помощью чего угодно API калькулятор:
```python
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
	# Обязательно добавляем host с нулями, чтобы мы могли обращаться к серверу
    calc.run(host="0.0.0.0",debug=True)
```
## Dockerfile
Создаем файл для сборки Docker контейнера
```python
# import python library
FROM python:3.8-slim

# install FLask library
RUN pip install Flask

# Create work directory
WORKDIR /app

# Copy python's file to work directory
COPY api_calc.py .

# Use 5000 port
EXPOSE 5000

# Start program
CMD ["python", "api_calc.py"]
```
## Build container
Все делаем в консоли и под рутом.
1. Устанавливаем docker.
2. Проверяем, запущен ли Docker.
	`# systemctl status docker`
	Должно быть `active (running)`.
3. Переходим в директорию, в которой находятся `api_calc.py` и `Dockerfile`.
4. Создаем образ Docker.
	`# docker build -f Dockerfile -t api_calc .`
	Пробегут несолько строчек. Если будут красные предупреждения - не печалимся, все хорошо, просто версия pip немножка старенькая. 
	![[Pasted image 20231005142745.png]]
	
5. Проверяем созданный образ.
	`# docker images`
	![[Screenshot_20231005_142116.png|500]]
6. Запускаем docker контейнер
	![[Pasted image 20231005142439.png|500]]
	Контейнер с программой запущен, теперь пробуем обратиться к программе.
	![[Pasted image 20231005142639.png]]
	Вывод сигнализирует об успешной контейниризации программы.