import customtkinter as ctk
import threading
import time
import stopwatch


class App:

    def __init__(self, master: ctk.CTk):
        self.master = master
        self.master.geometry('350x300')
        self.master.resizable(False, False)
        self.master.title('Stopwatch')
        self.time_gone = 0  # Starting from zero
        self.tumbler = False  # Is paused when the program starts

        # The digit that shows us hundredths of seconds:
        self.label = ctk.CTkLabel(self.master, text=str(self.time_gone), font=('Arial bold', 50))
        self.label.place(relx=0.5, rely=0.4, anchor='center')  # 0 to 1
        # The start button:
        self.button = ctk.CTkButton(self.master, text='Start', command=self.tumbler_switch, corner_radius=40)
        self.button.place(relx=0.5, rely=0.6, anchor='center')

    def start_count(self):
        """The function for creating a new thread. Not used at the time"""
        t = threading.Thread(target=self.count_time)
        t.start()

    def tumbler_switch(self):
        """The function to make the time tumbler True or False. (To make time running or frozen)"""
        t = threading.Thread(target=self.count_time)
        if self.tumbler:
            self.tumbler = False
            print('Tumbler down')  # This makes the timer refreshed that I didn't mean, but I'm working on it
        else:
            self.tumbler = True
            print('Tumbler up')
            t.start()

    def count_time(self):
        start_time = time.time() * 100
        while self.tumbler:
            try:
                current_time = time.time() * 100
                elapsed_time = current_time - start_time
                self.time_gone = round(elapsed_time)
                # Refreshing the interface at the main window
                self.master.after(10, self.update_label)
                time.sleep(0.01)  # waiting a 100'th of second
            except Exception as exc:
                print(f'Ошибка: {exc}')

    def update_label(self):
        # refreshing the lable that's showing time
        self.label.configure(text=str(self.time_gone))


if __name__ == '__main__':
    app = ctk.CTk()
    gui = App(master=app)
    app.mainloop()
