# app.py
from flask import Flask, render_template
import json
app = Flask(__name__)

# Дані резюме (можна уявити, що це приходить з бази даних або JSON)




def load_data(lang):
    file_path = 'data.json'
    if lang == 'en':
        file_path = 'data_en.json'
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Змінна 'data' тепер міститиме вміст JSON як словник або список Python
            data = json.load(file)

        print(f"✅ Дані успішно завантажено зі '{file_path}' у змінну.")
        print(f"Тип змінної: {type(data)}")
        # Приклад доступу до даних (якщо це словник)
        # print(f"Ключі у змінній: {python_variable.keys()}")
        return data
    except FileNotFoundError:
        print(f"❌ Помилка: Файл '{file_path}' не знайдено.")
    except json.JSONDecodeError:
        print(f"❌ Помилка: Неправильний формат JSON у файлі '{file_path}'.")
    except Exception as e:
        print(f"❌ Виникла несподівана помилка: {e}")

RESUME_DATA = load_data('ukr')

@app.route('/')
@app.route('/<lang>')
def index(lang='ua'):
    RESUME_DATA = load_data(lang)
    print(lang)
    return render_template('index.html', resume=RESUME_DATA, current_lang=lang)

if __name__ == '__main__':
    # Встановіть debug=True для автоматичного перезавантаження під час змін
    app.run(debug=True)