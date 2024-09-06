import tkinter as tk
from tkinter import messagebox
import random
import time


class Minesweeper:
    def __init__(self, root):
        self.root = root
        self.root.title("Сапер")
        self.root.geometry("750x920")

        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack(pady=20)

        self.create_menu()
        self.add_signature(self.menu_frame)

        self.game_frame = None
        self.attempts = 0
        self.flags = 0
        self.buttons = []
        self.mines = []
        self.game_started = False
        self.rows = 10
        self.cols = 10
        self.mine_count = 10
        self.first_move = True
        self.start_time = None
        self.timer_id = None
        self.message_label = None
        self.restarts = 0  # Добавляем переменную для хранения количества рестартов

    def create_menu(self):
        tk.Label(self.menu_frame, text="Добро пожаловать в игру", font=("Helvetica", 25)).pack(pady=20)
        tk.Label(self.menu_frame, text="САПЕР", font=("Helvetica", 25)).pack(pady=40)

        tk.Button(self.menu_frame, text="Старт", font=("Helvetica", 25), command=self.select_game_params).pack(pady=20)
        tk.Button(self.menu_frame, text="Инфо", font=("Helvetica", 25), command=self.show_info).pack(pady=20)
        tk.Button(self.menu_frame, text="Выход", font=("Helvetica", 25), command=self.root.quit).pack(pady=20)

    def add_signature(self, frame):
        tk.Label(frame, text="Created by Alex Bush", font=("Helvetica", 8)).pack(side=tk.TOP, anchor=tk.NE)

    def select_game_params(self):
        self.menu_frame.pack_forget()
        self.param_frame = tk.Frame(self.root)
        self.param_frame.pack(pady=20)

        self.create_param_widgets()
        self.add_signature(self.param_frame)

    def create_param_widgets(self):
        tk.Label(self.param_frame, text="Количество строк:", font=("Helvetica", 14)).pack(pady=10)
        self.rows_scale = tk.Scale(self.param_frame, from_=10, to=30, orient=tk.HORIZONTAL, font=("Helvetica", 14),
                                   length=400)
        self.rows_scale.set(self.rows)
        self.rows_scale.pack(pady=5)

        tk.Label(self.param_frame, text="Количество столбцов:", font=("Helvetica", 14)).pack(pady=10)
        self.cols_scale = tk.Scale(self.param_frame, from_=10, to=30, orient=tk.HORIZONTAL, font=("Helvetica", 14),
                                   length=400)
        self.cols_scale.set(self.cols)
        self.cols_scale.pack(pady=5)

        tk.Label(self.param_frame, text="Выберите уровень сложности:", font=("Helvetica", 14)).pack(pady=10)
        self.difficulty_var = tk.StringVar(value="средний")
        self.create_difficulty_buttons()

        tk.Button(self.param_frame, text="Начать игру", font=("Helvetica", 14), command=self.start_game).pack(pady=19)
        tk.Button(self.param_frame, text="Назад", font=("Helvetica", 14), command=self.return_to_menu).pack(pady=10)

    def create_difficulty_buttons(self):
        difficulties = [("Легкий", "легкий"), ("Средний", "средний"), ("Сложный", "сложный"),
                        ("Нереальный", "нереальный")]
        for text, level in difficulties:
            btn = tk.Button(self.param_frame, text=text, font=("Helvetica", 10),
                            command=lambda l=level: self.set_difficulty(l))
            btn.pack(pady=5)
            if level == self.difficulty_var.get():
                btn.config(bg="blue", fg="white")

    def set_difficulty(self, difficulty):
        self.difficulty_var.set(difficulty)
        self.update_difficulty_buttons()

    def update_difficulty_buttons(self):
        for widget in self.param_frame.winfo_children():
            if isinstance(widget, tk.Button) and widget.cget("text") in ["Легкий", "Средний", "Сложный", "Нереальный"]:
                if widget.cget("text").lower() == self.difficulty_var.get():
                    widget.config(bg="blue", fg="white")
                else:
                    widget.config(bg="SystemButtonFace", fg="black")

    def start_game(self):
        self.rows = self.rows_scale.get()
        self.cols = self.cols_scale.get()
        self.mine_count = self.calculate_mine_count()

        self.param_frame.pack_forget()
        self.reset_game()
        self.create_game_frame()
        self.create_board()
        self.game_started = True
        self.first_move = True

    def calculate_mine_count(self):
        difficulty = self.difficulty_var.get()
        ratios = {"легкий": 0.10, "средний": 0.15, "сложный": 0.20, "нереальный": 0.30}
        return int(ratios[difficulty] * self.rows * self.cols)

    def reset_game(self):
        if self.game_frame:
            self.game_frame.destroy()
        self.buttons = []
        self.mines = []
        self.attempts = 0
        self.flags = 0
        self.start_time = None
        self.timer_id = None

    def create_game_frame(self):
        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack(pady=20)

        self.attempts_label = tk.Label(self.game_frame, text=f"Попытки: {self.attempts}")
        self.attempts_label.grid(row=0, column=0, columnspan=self.cols)

        self.flags_label = tk.Label(self.game_frame, text=f"Флажки: {self.flags}/{self.mine_count}")
        self.flags_label.grid(row=1, column=0, columnspan=self.cols)

        self.timer_label = tk.Label(self.game_frame, text="Время: 0 сек", font=("Helvetica", 8))
        self.timer_label.grid(row=1, column=self.cols // 2, columnspan=self.cols // 2, sticky="e")

        self.restarts_label = tk.Label(self.game_frame, text=f"Рестарты: {self.restarts}")  # Добавляем метку для рестартов
        self.restarts_label.grid(row=0, column=self.cols // 2, columnspan=self.cols // 2, sticky="e")

        tk.Button(self.game_frame, text="Главное меню", font=("Helvetica", 14), command=self.return_to_menu).grid(
            row=self.rows + 2, column=0, columnspan=self.cols, pady=10)

    def create_board(self):
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                button = tk.Button(self.game_frame, width=2, height=1, bg="green",
                                   command=lambda i=i, j=j: self.click_button(i, j))
                button.grid(row=i + 2, column=j)
                button.bind("<Button-3>", lambda event, i=i, j=j: self.flag_mine(i, j))
                button.config(fg="black")  # Убедитесь, что изначальный цвет текста установлен в черный
                row.append(button)
            self.buttons.append(row)

    def place_mines(self, avoid_row, avoid_col):
        while len(self.mines) < self.mine_count:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if (row, col) not in self.mines and (row, col) != (avoid_row, avoid_col):
                self.mines.append((row, col))

    def click_button(self, row, col):
        if self.message_label and self.message_label.winfo_exists():
            return

        if not self.game_started or self.buttons[row][col]["state"] == tk.DISABLED:
            return

        if self.first_move:
            self.place_mines(row, col)
            self.first_move = False
            self.start_time = time.time()
            self.update_timer()
            self.reveal_around(row, col)

        if (row, col) in self.mines:
            self.reveal_all_mines()
            self.show_message("Вы проиграли!")
            self.stop_timer()
        else:
            self.reveal_cell(row, col)
            self.check_win()

    def reveal_around(self, row, col):
        for i in range(max(0, row - 1), min(row + 2, self.rows)):
            for j in range(max(0, col - 1), min(col + 2, self.cols)):
                if self.buttons[i][j]["state"] == tk.NORMAL and (i, j) not in self.mines:
                    self.reveal_cell(i, j)

    def reveal_cell(self, row, col):
        self.attempts += 1
        self.attempts_label.config(text=f"Попытки: {self.attempts}")
        mines_around = self.count_mines_around(row, col)
        if mines_around == 0:
            self.buttons[row][col].config(text="", state=tk.DISABLED, bg="white")
            self.reveal_empty_cells(row, col)
        else:
            color = self.get_color_for_mines_around(mines_around)
            self.buttons[row][col].config(text=str(mines_around), state=tk.DISABLED, fg=color, bg="white")
            self.root.update_idletasks()  # Добавьте эту строку
            self.root.update()

    def get_color_for_mines_around(self, mines_around):
        if mines_around == 1:
            return "yellow"
        elif mines_around == 2:
            return "green"
        elif mines_around == 3:
            return "orange"
        elif mines_around == 4:
            return "red"
        elif mines_around == 5:
            return "maroon"
        elif mines_around == 6:
            return "purple"
        elif mines_around == 7:
            return "blue"
        elif mines_around == 8:
            return "black"
        else:
            return "black"

    def flag_mine(self, row, col):
        if self.buttons[row][col]["state"] == tk.NORMAL:
            if self.flags <= self.mine_count:
                self.buttons[row][col].config(text="F", bg="yellow", state=tk.DISABLED)
                self.flags += 1
                self.flags_label.config(text=f"Флажки: {self.flags}/{self.mine_count}")
        elif self.buttons[row][col]["text"] == "F":
            self.buttons[row][col].config(text="", bg="green", state=tk.NORMAL)  # Восстанавливаем серый цвет
            self.flags -= 1
            self.flags_label.config(text=f"Флажки: {self.flags}/{self.mine_count}")

    def count_mines_around(self, row, col):
        count = 0
        for i in range(max(0, row - 1), min(row + 2, self.rows)):
            for j in range(max(0, col - 1), min(col + 2, self.cols)):
                if (i, j) in self.mines:
                    count += 1
        return count

    def reveal_empty_cells(self, row, col):
        queue = [(row, col)]
        while queue:
            r, c = queue.pop(0)
            for i in range(max(0, r - 1), min(r + 2, self.rows)):
                for j in range(max(0, c - 1), min(c + 2, self.cols)):
                    if self.buttons[i][j]["state"] == tk.NORMAL:
                        mines_around = self.count_mines_around(i, j)
                        if mines_around == 0:
                            self.buttons[i][j].config(text="", state=tk.DISABLED, bg="white")
                            queue.append((i, j))
                        else:
                            color = self.get_color_for_mines_around(mines_around)
                            self.buttons[i][j].config(text=str(mines_around), state=tk.DISABLED, fg=color, bg="white")

    def reveal_all_mines(self):
        def reveal_mine(row, col):
            if self.buttons[row][col]["state"] == tk.NORMAL or self.buttons[row][col]["text"] == "F":
                if self.buttons[row][col]["text"] == "F":
                    self.buttons[row][col].config(text="F", bg="blue")
                else:
                    self.buttons[row][col].config(text="X", bg="red")
                self.root.after(1, lambda: reveal_next_mine())

        def reveal_next_mine():
            if mine_queue:
                row, col = mine_queue.pop(0)
                reveal_mine(row, col)

        mine_queue = self.mines.copy()
        reveal_next_mine()

    def restart_level(self):
        self.restarts += 1  # Увеличиваем счетчик рестартов
        self.restarts_label.config(text=f"Рестарты: {self.restarts}")  # Обновляем метку рестартов
        self.game_started = False
        self.reset_game()
        self.create_game_frame()
        self.create_board()
        self.game_started = True
        self.first_move = True
        if self.message_label and self.message_label.winfo_exists():
            self.message_label.destroy()
            self.message_label = None

    def check_win(self):
        # Проверяем, что все клетки, не содержащие мины, открыты
        for row in range(self.rows):
            for col in range(self.cols):
                if (row, col) not in self.mines and self.buttons[row][col]["state"] == tk.NORMAL:
                    return  # Если найдена хотя бы одна неоткрытая клетка, не содержащая мину, игра продолжается

        # Если все клетки, не содержащие мины, открыты, объявляем победу
        self.show_message("Поздравляем, победа!")
        self.stop_timer()
        self.reveal_all_mines()

    def return_to_menu(self):
        if self.game_frame:
            self.game_frame.destroy()
        if self.param_frame:
            self.param_frame.destroy()
        self.menu_frame.pack(pady=20)
        self.stop_timer()

    def show_info(self):
        info = (
            "Как играть в Сапер:\n\n"
            "1. Нажмите кнопку 'Старт' для начала новой игры.\n"
            "2. Выберите размер поля и количество мин.\n"
            "3. Нажмите на кнопки, чтобы открыть ячейки.\n"
            "4. Используйте правую кнопку мыши, чтобы поставить флажок на предполагаемую мину.\n"
            "5. Если вы откроете мину, игра закончится.\n"
            "6. Цель игры - открыть все ячейки, кроме тех, где находятся мины.\n"
            "Удачи!"
        )
        messagebox.showinfo("Инфо", info)

    def update_timer(self):
        if self.game_started and self.start_time:
            elapsed_time = int(time.time() - self.start_time)
            self.timer_label.config(text=f"Время: {elapsed_time} сек")
            self.timer_id = self.root.after(1000, self.update_timer)

    def stop_timer(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

    def show_message(self, message):
        if self.message_label and self.message_label.winfo_exists():
            self.message_label.config(text=message)
        else:
            self.message_label = tk.Label(self.game_frame, text=message, font=("Helvetica", 25), bg="white")
            self.message_label.grid(row=self.rows // 2 + 2, column=0, columnspan=self.cols, pady=20)

        if message == "Вы проиграли!":
            self.root.after(2000, self.restart_level)
        elif message == "Поздравляем, победа!":
            self.root.after(2000, self.increase_difficulty)

    def increase_difficulty(self):
        self.rows = min(int(self.rows * 1.1), 30)
        self.cols = min(int(self.cols * 1.1), 30)
        if self.rows == 30 and self.cols == 30:
            self.return_to_menu()
        else:
            self.mine_count = self.calculate_mine_count()
            self.restart_level()


if __name__ == "__main__":
    root = tk.Tk()
    game = Minesweeper(root)
    root.mainloop()