# app.py
from flask import Flask, render_template
import json,platform,config
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

def load_data(lang):
    file_path = 'data.json'
    if lang == 'en':
        file_path = 'data_en.json'
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        print(f"✅ Дані успішно завантажено зі '{file_path}' у змінну.")
        # print(f"Тип змінної: {type(data)}")
        # print(f"Ключі у змінній: {python_variable.keys()}")
        return data
    except FileNotFoundError:
        print(f"❌ Помилка: Файл '{file_path}' не знайдено.")
    except json.JSONDecodeError:
        print(f"❌ Помилка: Неправильний формат JSON у файлі '{file_path}'.")
    except Exception as e:
        print(f"❌ Виникла несподівана помилка: {e}")

RESUME_DATA = load_data('ua')

@app.route('/')
@app.route('/<string:lang>')
def index(lang='ua'):
    RESUME_DATA = load_data(lang)
    return render_template('index.html', resume=RESUME_DATA, current_lang=lang)

########### MAIN ##############################################
if __name__ == "__main__":
    if platform.system() == 'Windows':
        http_server = WSGIServer((config.local_ip,config.server_port), app)
        print(f"Running HTTP-SERVER on port - http://" + config.local_ip + ':' + str(config.server_port))
    else:
        http_server = WSGIServer(('', int(config.server_port)), app)
        print(f"Running HTTP-SERVER on port :" + str(config.server_port))
    http_server.serve_forever()
