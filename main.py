import customtkinter as ctk
import time


class App:

    def __init__(self, master: ctk.CTk):
        self.master = master
        self.master.geometry('350x300')
        self.master.resizable(False, False)
        self.master.title('Секундомер')
        self.time_gone = 0  # Начиная с нуля

        # Цифра, которая должна показывать сотые:
        self.label = ctk.CTkLabel(self.master, text=str(self.time_gone), font=('Arial bold', 50))
        self.label.place(relx=0.5, rely=0.4, anchor='center')  # 0 to 1
        # Кнопка старта:
        self.button = ctk.CTkButton(self.master, text='Старт', command=self.start_count, corner_radius=40)
        self.button.place(relx=0.5, rely=0.6, anchor='center')

    def start_count(self):
        start_time = time.time() * 100
        while True:
            try:
                current_time = time.time() * 100
                elapsed_time = current_time - start_time
                self.time_gone = round(elapsed_time)
                print(self.time_gone)
                self.label.configure(text=str(self.time_gone))
                time.sleep(0.01)  # ждем 1 сотую секунды

            except Exception as exc:
                print(f'Ошибка: {exc}')


if __name__ == '__main__':
    app = ctk.CTk()
    gui = App(master=app)
    app.mainloop()
