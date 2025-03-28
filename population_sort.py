import sys
import tkinter as tk
from tkinter import filedialog

def read_data(filename):
    """Зчитує дані з файлу та повертає список країн."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = [line.strip().split(', ') for line in file]
            return [(x[0], float(x[1]), int(x[2])) for x in data if len(x) == 3]
    except Exception as e:
        print(f"Помилка: {e}")
        return []

def sort_data(data, index):
    """Сортує дані за вибраним параметром."""
    return sorted(data, key=lambda x: x[index], reverse=True)

def main():
    root = tk.Tk()
    root.withdraw()  # Ховаємо головне вікно
    filename = filedialog.askopenfilename(title="Оберіть файл", filetypes=[("Text files", "*.txt")])
    
    if not filename:
        print("Файл не вибрано.")
        return
    
    data = read_data(filename)
    if not data:
        print("Файл порожній або містить помилки.")
        return
    
    print("\nЗа площею:")
    for c, a, p in sort_data(data, 1):
        print(f"{c}: {a} км², {p} осіб")
    
    print("\nЗа населенням:")
    for c, a, p in sort_data(data, 2):
        print(f"{c}: {a} км², {p} осіб")

if __name__ == "__main__":
    main()

