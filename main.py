import customtkinter as ctk

class App:

    def __init__(self, master: ctk.CTk):
        self.master = master
        self.master.geometry('350x300')
        self.master.resizable(False, False)
        self.master.title('Секундомер')

if __name__ == '__main__':
    app = ctk.CTk()
    gui = App(master=app)
    app.mainloop()