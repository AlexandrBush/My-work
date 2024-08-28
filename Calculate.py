import tkinter as tk


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Калькулятор АБ")
        self.geometry("260x380")
        self.configure(bg="#f0f0f0")

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.create_widgets()

    def create_widgets(self):
        # Display
        display = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=5, insertwidth=2, width=10,
                           justify='right', bg="#ffffff")
        display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('+/-', 5, 1)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, font=("Arial", 12), width=5, height=2, bg="#e0e0e0", command=lambda
                t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, text):
        current = self.result_var.get()

        if text == 'C':
            self.result_var.set("0")
        elif text == '=':
            try:
                result = eval(current)
                formatted_result = round(result, 2)
                self.result_var.set(formatted_result)
            except Exception as e:
                self.result_var.set("Error")
        elif text == '+/-':
            if current.startswith('-'):
                self.result_var.set(current[1:])
            else:
                self.result_var.set('-' + current)
        else:
            if current == "0" and text.isdigit() and text != "0":
                self.result_var.set(text)
            else:
                self.result_var.set(current + text)


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()

"""
1. import tkinter as tk
Эта строка импортирует библиотеку Tkinter, которая используется для создания графических пользовательских 
интерфейсов (GUI) в Python.


2. Здесь создается класс Calculator, который наследуется от tk.Tk. В методе __init__ инициализируется главное окно 
приложения:
super().__init__() вызывает конструктор родительского класса tk.Tk.
self.title("Калькулятор АБ") устанавливает заголовок окна.
self.geometry("260x380") устанавливает размер окна.
self.configure(bg="#f0f0f0") устанавливает цвет фона окна в светло-серый.


3. Создается переменная result_var типа tk.StringVar, которая будет использоваться для хранения и отображения 
результата в поле ввода. Изначально она устанавливается в "0"


4. Вызывается метод create_widgets, который создает и размещает все виджеты (кнопки и поле ввода) на окне.


5. Метод create_widgets создает поле ввода (tk.Entry), которое отображает текущий результат. Оно настроено на 
использование переменной result_var для отображения текста. Поле ввода размещается в сетке с помощью метода grid.


6. Создается список buttons, который содержит кортежи с текстом кнопки и ее координатами в сетке.


7. Цикл for создает кнопки (tk.Button) для каждого элемента в списке buttons. Каждая кнопка настроена на 
вызов метода on_button_click с передачей текста кнопки при нажатии. Кнопки размещаются в сетке с помощью метода grid.


8. Метод on_button_click обрабатывает нажатия кнопок:
Если нажата кнопка 'C', очищает поле ввода, устанавливая значение в "0".
Если нажата кнопка '=', вычисляет результат выражения с помощью функции eval. Если возникает ошибка, устанавливает 
значение в "Error".
В противном случае, если текущее значение равно "0" и нажата цифра, отличная от нуля, заменяет "0" на эту цифру. 
В остальных случаях добавляет текст кнопки к текущему значению.


9. if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
Этот блок кода проверяет, запущен ли скрипт напрямую (а не импортирован как модуль). Если да, то создается экземпляр 
класса Calculator, и вызывается метод mainloop, который запускает главный цикл обработки событий Tkinter, чтобы окно 
оставалось открытым и реагировало на действия пользователя.

"""
