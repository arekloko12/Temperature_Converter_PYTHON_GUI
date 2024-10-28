from tkinter import Tk, Button, Label, Radiobutton, Entry, StringVar


class App:
    def __init__(self, master):
        master.geometry("300x500")
        master.title("Converter")
        master.config(bg="lightgray")
        master.resizable(False, False)

        self.entry_value = StringVar()
        self.option1 = StringVar()
        self.option2 = StringVar()

        self.number = Entry(master, textvariable = self.entry_value, font="Arial, 20", width=16, justify="right")
        self.number.place(x = 25, y = 30)

        Label(master, text="Starting unit:", font="Arial, 15").place(x=40, y=100)

        self.convert1 = Radiobutton(master, font="Arial, 10", variable=self.option1, value=1, text="Celcius")
        self.convert2 = Radiobutton(master, font="Arial, 10", variable=self.option1, value=2, text="Fahrenheit")
        self.convert3 = Radiobutton(master, font="Arial, 10", variable=self.option1, value=3, text="Kelvin")

        self.convert1.place(x = 25,y = 150)
        self.convert2.place(x = 25, y = 180)
        self.convert3.place(x = 25, y = 210)

        Label(master, text="Ending unit:", font="Arial, 15").place(x=40, y=250)

        self.convert4 = Radiobutton(master, font="Arial, 10", variable=self.option2, value=4, text="Celcius")
        self.convert5 = Radiobutton(master, font="Arial, 10", variable=self.option2, value=5, text="Fahrenheit")
        self.convert6 = Radiobutton(master, font="Arial, 10", variable=self.option2, value=6, text="Kelvin")

        self.convert4.place(x=25, y=300)
        self.convert5.place(x=25, y=330)
        self.convert6.place(x=25, y=360)

        self.option1.set("1")
        self.option2.set("4")

        self.submit_btn = Button(master, font="Arial, 20", text="Calculate",
                                 command=lambda: self.result(self.option1.get(), self.option2.get()))
        self.submit_btn.place(x=80, y=410)

    def result(self, value1, value2):
        try:
            match int(value1), int(value2):
                case 1, 4:
                    pass
                case 1, 5:
                    self.celc_fahren(self.entry_value.get())
                case 1, 6:
                    self.celc_kelw(self.entry_value.get())
                case 2, 4:
                    self.fahren_celc(self.entry_value.get())
                case 2, 5:
                    pass
                case 2, 6:
                    self.fahren_kelw(self.entry_value.get())
                case 3, 4:
                    self.kelw_celc(self.entry_value.get())
                case 3, 5:
                    self.kelw_fahren(self.entry_value.get())
                case 3, 6:
                    pass
                case _:
                    pass
        except:
            self.entry_value.set("Error!")

    def celc_fahren(self, value):
        try:
            fahrenheit: float = round((float(value) * 1.8) + 32, 3)
            self.entry_value.set(str(fahrenheit))
        except:
            self.entry_value.set("Error!")

    def fahren_celc(self, value):
        try:
            celcius: float = round((float(value) - 32) / 1.8, 3)
            self.entry_value.set(str(celcius))
        except:
            self.entry_value.set("Error!")

    def celc_kelw(self, value):
        try:
            kelvin: float = round(float(value) + 273.15, 3)
            self.entry_value.set(str(kelvin))
        except:
            self.entry_value.set("Error!")

    def kelw_celc(self, value):
        try:
            celcius: float = round(float(value) - 273.15, 3)
            self.entry_value.set(str(celcius))
        except:
            self.entry_value.set("Error!")


    def fahren_kelw(self, value):
        try:
            kelvin: float = round((float(value) + 459.67) * 5 / 9, 3)
            self.entry_value.set(str(kelvin))
        except:
            self.entry_value.set("Error!")


    def kelw_fahren(self, value):
        try:
            fahrenheit: float = round((float(value) * 1.8) - 459.67, 3)
            self.entry_value.set(str(fahrenheit))
        except:
            self.entry_value.set("Error!")



root = Tk()
app = App(root)
root.mainloop()