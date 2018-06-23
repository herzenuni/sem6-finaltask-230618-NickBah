from tkinter import Entry, Frame, Label, Button, Radiobutton, IntVar
from process import getName

class main(Frame):

    def check_number(self,a):
        if (a.isdigit() == True):
            if (int(a) >= 0 and int(a) <= 9):
                return True
        return False

    def getNameButtonClicked(self, event):
        text = self.main_input.get()
        mode = self.mode.get()
        if (self.check_number(text) == True):
            number = int(text)
            if (mode == 0):
                #print(getName(number))
                self.output_label.configure(text = getName(number))
            elif (mode == 1):
                #print(getName(bin(number)))
                self.output_label.configure(text=getName(bin(number)))
            elif (mode == 2):
                #print(getName(oct(number)))
                self.output_label.configure(text=getName(oct(number)))
            else:
                #print(getName(hex(number)))
                self.output_label.configure(text=getName(hex(number)))
        else:
            #print('Неверный ввод')
            self.output_label.configure(text='Неверный ввод')




    def __init__(self, master):
        self.master = master
        self.master.title('Задание 1')
        self.master.geometry('1245x510+70+70')
        self.master.minsize(width=1245, height=510)
        self.master.maxsize(width=1245, height=510)

        # Главное поле ввода
        self.main_input = Entry(self.master, width=20, bd=3, font='times 15')
        self.main_input.place(x=500, y=50)

        self.main_input_label = Label(self.master, text='Введите число от 0 до 9')
        self.main_input_label.place(x=500, y=25)

        # Кнопка "Вывести имя"
        self.get_name_button = Button(self.master, width=20, bd=3, font='times 15', text="Вывести имя")
        self.get_name_button.place(x=100, y=50)
        self.get_name_button.bind('<Button-1>', self.getNameButtonClicked)

        self.output_label = Label(self.master, text='Здесь будет отображен результат',fg='#FF6A00')
        self.output_label.place(x=500, y=100)

        # 0 - Обычный режим
        # 1 - bin
        # 2 - oct
        # 3 - hex
        self.mode = IntVar()

        # Радиокнопки
        self.radiobutton_1 = Radiobutton(text="Обычный режим", value=0, variable=self.mode)
        self.radiobutton_1.place(x=100, y=150)

        self.radiobutton_2 = Radiobutton(text="bin", value=1, variable=self.mode)
        self.radiobutton_2.place(x=100, y=190)

        self.radiobutton_3 = Radiobutton(text="oct", value=2, variable=self.mode)
        self.radiobutton_3.place(x=100, y=230)

        self.radiobutton_4 = Radiobutton(text="hex", value=3, variable=self.mode)
        self.radiobutton_4.place(x=100, y=270)