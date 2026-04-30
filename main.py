import tkinter as tk
import random
import json

# Изначальные данные
tasks = [
    {"task": "Прочитать статью", "type": "учёба"},
    {"task": "Сделать зарядку", "type": "спорт"},
    {"task": "Проверить почту", "type": "работа"}
]

history = []

# Загрузка истории из файла
def load_history():
    try:
        with open("history.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Сохранение истории
def save_history():
    with open("history.json", "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=4)

# Глобальные переменные
current_task_label = None
history_box = None

# Функция генерации случайной задачи
def generate_task():
    task = random.choice(tasks)
    history.append(task)
    update_history()
    current_task_var.set(f"Задача: {task['task']} ({task['type']})")
    save_history()

def update_history():
    global history_box
    history_box.delete(0, tk.END)
    for t in history:
        history_box.insert(tk.END, f"{t['task']} - {t['type']}")

# Функция фильтрации
def filter_tasks():
    selected_type = filter_var.get()
    if selected_type == "Все":
        filtered_tasks = tasks
    else:
        filtered_tasks = [t for t in tasks if t['type'] == selected_type]
    # Обновляем список
    # Можно сделать интерфейс с Combobox, для простоты — перезапишем список задач
    # (для полной реализации можно расширить)
    return filtered_tasks

# Основное окно
root = tk.Tk()
root.title("Random Task Generator")

current_task_var = tk.StringVar()
current_task_label = tk.Label(root, textvariable=current_task_var, font=("Arial", 14))
current_task_label.pack(pady=10)

generate_btn = tk.Button(root, text="Сгенерировать задачу", command=generate_task)
generate_btn.pack(pady=5)

# Фильтр по типу
filter_var = tk.StringVar(value="Все")
types = ["Все", "учёба", "спорт", "работа"]
for t in types:
    tk.Radiobutton(root, text=t, variable=filter_var, value=t, command=lambda: None).pack(side=tk.LEFT)

# История
history_box = tk.Listbox(root, width=50)
history_box.pack(pady=10)

# Загружаем историю при запуске
history = load_history()
update_history()

root.mainloop()