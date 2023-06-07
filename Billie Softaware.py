
import tkinter as tk
import os
from tkinter import ttk, messagebox
from csv import DictReader,DictWriter
import inflect
import random
from gtts import gTTS
import subprocess


import time
def audio(number):
    pass







class Stock:
    def __init__(self):
        self.path_of_file = "D:\\New folder (2)\\tejas.csv"
        self.cosmetic_name = ['Soap', 'Face_Cream', 'Hair_Spray', 'Hair_Gel', 'Body_Lotion', 'Face_Wash']
        self.grocerry_name = ['Tea', 'Daal', 'Rice', "Food_Oil", 'Sugar', 'Wheat']
        self.cold_drink_name = ['Thums_Up', 'Limca', 'Frooti', 'Cock', 'Sprite', 'Maza']
        self.All_Product = []
        for i in self.cosmetic_name:
            self.All_Product.append(i)
        for i in self.grocerry_name:
            self.All_Product.append(i)
        for i in self.cold_drink_name:
            self.All_Product.append(i)
        self.All_Product.append("Time")
        self.All_Product.append('source')

        self.cosmetic = {}
        self.grocerry = {}
        self.cold_drink = {}

    def write_stock_comsetic(self, **kwargs):
        # m.write_stock_comsetic(Soap=[o, o,], Face_Cream=[o, o], Hair_Spray=[o, o,], Hair_Gel=[o,.o,],
        #                       Body_Lotion=[o, o,], Face_Wash=[o, o,])'''
        if len(kwargs) == 6:
            for i, j in kwargs.items():
                if len(j) == 2:
                    if i == self.cosmetic_name[0]:
                        self.cosmetic[i] = j

                    elif i == self.cosmetic_name[1]:
                        self.cosmetic[i] = j
                    elif i == self.cosmetic_name[2]:
                        self.cosmetic[i] = j
                    elif i == self.cosmetic_name[3]:
                        self.cosmetic[i] = j
                    elif i == self.cosmetic_name[4]:
                        self.cosmetic[i] = j
                    elif i == self.cosmetic_name[5]:
                        self.cosmetic[i] = j

    def write_stock_grocerry(self, **kwargs):
        '''m.write_stock_grocerry(Tea=[0,0],Daal=[0,0],Rice=[0,0],Food_Oil=[0,0],Sugar=[0,0],Wheat=[0,0])'''
        if len(kwargs) == 6:
            for i, j in kwargs.items():
                if len(j) == 2:
                    if i == self.grocerry_name[0]:
                        self.grocerry[i] = j

                    elif i == self.grocerry_name[1]:
                        self.grocerry[i] = j
                    elif i == self.grocerry_name[2]:
                        self.grocerry[i] = j
                    elif i == self.grocerry_name[3]:
                        self.grocerry[i] = j
                    elif i == self.grocerry_name[4]:
                        self.grocerry[i] = j
                    elif i == self.grocerry_name[5]:
                        self.grocerry[i] = j

    def write_stock_coldrinks(self, **kwargs):
        # m.write_stock_coldrinks(Thums_Up=[0,0], Frooti=[0,0], Cock=[0,0], Sprite=[0,0], Maza=[0,0],
        #                       Limca=[0,0])
        if len(kwargs) == 6:
            for i, j in kwargs.items():

                if len(j) == 2:
                    if i == self.cold_drink_name[0]:
                        self.cold_drink[i] = j

                    elif i == self.cold_drink_name[1]:
                        self.cold_drink[i] = j
                    elif i == self.cold_drink_name[2]:
                        self.cold_drink[i] = j
                    elif i == self.cold_drink_name[3]:
                        self.cold_drink[i] = j
                    elif i == self.cold_drink_name[4]:
                        self.cold_drink[i] = j
                    elif i == self.cold_drink_name[5]:
                        self.cold_drink[i] = j

    def sorce(self, define_source):
        self.sorce_ = define_source

    def Writer(self):
        self.Dictionary = {}
        times = [time.strftime("%D"), time.strftime("%T")]
        for i, j in self.cold_drink.items():
            self.Dictionary[i] = j
        for i, j in self.grocerry.items():
            self.Dictionary[i] = j
        for i, j in self.cosmetic.items():
            self.Dictionary[i] = j
        self.Dictionary['source'] = self.sorce_
        self.Dictionary["Time"] = times


        with open(self.path_of_file, "a",encoding="utf-8") as f1:
            f2 = DictWriter(f1, fieldnames=self.All_Product)
            if os.stat(self.path_of_file).st_size == 0:
                f2.writeheader()
            f2.writerow(self.Dictionary)
        f1.close()

    def Reader(self):
        dict = {}
        with open(self.path_of_file, "r",encoding="utf-8") as f1:
            f2 = DictReader(f1)
            for i in f2:
                dict = i


        f1.close()
        return dict


class creating(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1800x1000")
        bgcolor = "black"
        self.bgcolor=bgcolor
        self.object = Stock()

        # Products Name_________________________________________________________________________________________
        self.cosmetic = ['Soap', 'Face Cream', 'Hair Spray', 'Hair Gel', 'Body Lotion', 'Face Wash']
        self.grocerry = ['Tea', 'Daal', 'Rice', "Food Oil", 'Sugar', 'Wheat']
        self.coldrink = ['Thums Up', 'Limca', 'Frooti', 'Cock', 'Sprite', 'Maza']
        # Products Name End_________________________________________________________________________________________
        # _______________________________________________________Variables
        # cosmetic Variables
        self.soap = tk.IntVar()
        self.face_cream = tk.IntVar()
        self.hair_s = tk.IntVar()
        self.hair_g = tk.IntVar()
        self.lotion = tk.IntVar()
        self.face_wash = tk.IntVar()

        # Grosery Variables
        self.rice = tk.IntVar()
        self.food_oil = tk.IntVar()
        self.wheat = tk.IntVar()
        self.sugar = tk.IntVar()
        self.daal = tk.IntVar()
        self.tea = tk.IntVar()

        # colddrink Variables
        self.maza = tk.IntVar()
        self.cock = tk.IntVar()
        self.frooti = tk.IntVar()
        self.thumsup = tk.IntVar()
        self.limca = tk.IntVar()
        self.sprite = tk.IntVar()

        # ______________________________________________Set Price Variables
        # cosmetic Variables
        self.soap_price = tk.IntVar()
        self.face_cream_price = tk.IntVar()
        self.hair_s_price = tk.IntVar()
        self.hair_g_price = tk.IntVar()
        self.lotion_price = tk.IntVar()
        self.face_wash_price = tk.IntVar()

        # Grosery Variables
        self.rice_price = tk.IntVar()
        self.food_oil_price = tk.IntVar()
        self.wheat_price = tk.IntVar()
        self.sugar_price = tk.IntVar()
        self.daal_price = tk.IntVar()
        self.tea_price = tk.IntVar()

        # colddrink Variables
        self.maza_price = tk.IntVar()
        self.cock_price = tk.IntVar()
        self.frooti_price = tk.IntVar()
        self.thumsup_price = tk.IntVar()
        self.limca_price = tk.IntVar()
        self.sprite_price = tk.IntVar()

        # __________________________________________New Stock Variable
        # cosmetic Variables
        self.soap_new = tk.IntVar()
        self.face_cream_new = tk.IntVar()
        self.hair_s_new = tk.IntVar()
        self.hair_g_new = tk.IntVar()
        self.lotion_new = tk.IntVar()
        self.face_wash_new = tk.IntVar()

        # Grosery Variables
        self.rice_new = tk.IntVar()
        self.food_oil_new = tk.IntVar()
        self.wheat_new = tk.IntVar()
        self.sugar_new = tk.IntVar()
        self.daal_new = tk.IntVar()
        self.tea_new = tk.IntVar()

        # colddrink Variables
        self.maza_new = tk.IntVar()
        self.cock_new = tk.IntVar()
        self.frooti_new = tk.IntVar()
        self.thumsup_new = tk.IntVar()
        self.limca_new = tk.IntVar()
        self.sprite_new = tk.IntVar()

        title = tk.Label(self, text="Billing Software", bd=12, relief="groove", bg=bgcolor, fg="white",
                         font=("times new roman", 30, "bold"))
        title.pack(fill=tk.X)

        self.f1 = tk.LabelFrame(self, text="Cosmetic", font=("times new roman", "15", "bold"), bg=bgcolor, fg="gold",
                                bd=10, relief="groove")

        self.f2 = tk.LabelFrame(self, text="Grossery", font=("times new roman", "15", "bold"), bg=bgcolor, fg="gold",
                                bd=10, relief="groove")

        self.f3 = tk.LabelFrame(self, text="Cold Drink", font=("times new roman", "15", "bold"), bg=bgcolor, fg="gold",
                                bd=10, relief="groove")
        self.f4 = tk.LabelFrame(self, text="Set price of products", font=("times new roman", "15", "bold"), bg=bgcolor,
                                fg="gold",
                                bd=10, relief="groove")
        self.f5 = tk.LabelFrame(self, text="Avilble Stock", font=("times new roman", "15", "bold"), bg=bgcolor,
                                fg="gold",
                                bd=10, relief="groove")

        self.f7 = tk.LabelFrame(self, text="Buttons", font=("times new roman", "15", "bold"), bg=bgcolor, fg="gold",
                                bd=10, relief="groove")
        self.f1.place(x=0, y=70, width=330, height=500)
        self.f2.place(x=330, y=70, width=330, height=500)
        self.f3.place(x=660, y=70, width=330, height=500)
        self.f4.place(x=1020, y=70, width=390, height=500)
        self.f5.place(x=0, y=570, width=1200, relheight=1.0)
        self.Button1 = tk.Button(self.f7, text='Reset', width=20, height=5, command=self.reset, fg="black",
                                 highlightbackground="cyan", font=("times", 14, "bold"))
        self.Button1.grid(row=0, column=0, padx=15, pady=10)
        self.Button2 = tk.Button(self.f7, text='Sumbit', width=20, height=5, command=self.write_stock, fg="black",
                                 highlightbackground="cyan", font=("times", 14, "bold"))

        self.Button1.bind("<Motion>", lambda event: self.Button1.configure(text="Click to Reset Stock",
                                                                           highlightbackground="#00FF00", fg="red"))
        self.Button1.bind("<Leave>",
                          lambda event: self.Button1.configure(text="Reset", fg="black", highlightbackground="cyan"))
        self.Button2.bind("<Motion>", lambda event: self.Button2.configure(text="Click To Sumbit",
                                                                           highlightbackground="#00FF00", fg="red"))
        self.Button2.bind("<Leave>",
                          lambda event: self.Button2.configure(text="Sumbit", fg="black", highlightbackground="cyan"))

        self.Button2.grid(row=1, column=0, padx=15, pady=10)

        self.f7.place(x=1200, y=570, relwidth=1.0, relheight=1.0)
        self.font = ("times new roman", 18, "bold")
        self.t = tk.Label(self.f4, bg='white')
        self.t.pack(fill=tk.X)
        self.read_stock()
        self.cosmetic_fun()
        self.glocerry_fun()
        self.colddrink_fun()
        self.add_price()

        self.Main_Menu = tk.Menu(self)
        self.sub = tk.Menu(self.Main_Menu)
        self.Main_Menu.add_cascade(label="Go To Application", menu=self.sub)
        self.configure(menu=self.Main_Menu)
        self.sub.add_command(label="Click Here",command=self.new)
        self.configure(menu=self.Main_Menu)
    def new(self):
        self.destroy()
        m=software()


    def read_stock(self):

        try:
            All_Data = self.object.Reader()
            for i in self.cosmetic:
                data = i.replace(" ", "_")
                list = All_Data[data].strip('[]', ).split(',')
                if i == self.cosmetic[0]:
                    self.soap_price.set(list[0])
                    self.soap_new.set(list[1])
                if i == self.cosmetic[1]:
                    self.face_cream_price.set(list[0])
                    self.face_cream_new.set(list[1])
                if i == self.cosmetic[2]:
                    self.hair_s_price.set(list[0])
                    self.hair_s_new.set(list[1])
                if i == self.cosmetic[3]:
                    self.hair_g_price.set(list[0])
                    self.hair_g_new.set(list[1])

                if i == self.cosmetic[4]:
                    self.lotion_price.set(list[0])
                    self.lotion_new.set(list[1])
                if i == self.cosmetic[5]:
                    self.face_wash_price.set(list[0])
                    self.face_wash_new.set(list[1])

            for i in self.grocerry:
                data = i.replace(" ", "_")
                list = All_Data[data].strip('[]', ).split(',')
                if i == self.grocerry[0]:
                    self.tea_price.set(list[0])
                    self.tea_new.set(list[1])
                if i == self.grocerry[1]:
                    self.daal_price.set(list[0])
                    self.daal_new.set(list[1])
                if i == self.grocerry[2]:
                    self.rice_price.set(list[0])
                    self.rice_new.set(list[1])
                if i == self.grocerry[3]:
                    self.food_oil_price.set(list[0])
                    self.food_oil_new.set(list[1])

                if i == self.grocerry[4]:
                    self.sugar_price.set(list[0])
                    self.sugar_new.set(list[1])
                if i == self.grocerry[5]:
                    self.wheat_price.set(list[0])
                    self.wheat_new.set(list[1])

            for i in self.coldrink:
                data = i.replace(" ", "_")
                list = All_Data[data].strip('[]', ).split(',')
                if i == self.coldrink[0]:
                    self.thumsup_price.set(list[0])
                    self.thumsup_new.set(list[1])
                if i == self.coldrink[1]:
                    self.limca_price.set(list[0])
                    self.limca_new.set(list[1])
                if i == self.coldrink[2]:
                    self.frooti_price.set(list[0])
                    self.frooti_new.set(list[1])
                if i == self.coldrink[3]:
                    self.cock_price.set(list[0])
                    self.cock_new.set(list[1])

                if i == self.coldrink[4]:
                    self.sprite_price.set(list[0])
                    self.sprite_new.set(list[1])
                if i == self.coldrink[5]:
                    self.maza_price.set(list[0])
                    self.maza_new.set(list[1])
        except:
            pass
        self.new_stock()

    def write_stock(self):

        try:
            # cosmetic Variables
            int(self.soap.get())
            int(self.face_cream.get())
            int(self.hair_s.get())
            int(self.hair_g.get())
            int(self.lotion.get())
            int(self.face_wash.get())

            # Grosery Variables
            int(self.rice.get())
            int(self.food_oil.get())
            int(self.wheat.get())
            int(self.sugar.get())
            int(self.daal.get())
            int(self.tea.get())

            # colddrink Variables
            int(self.maza.get())
            int(self.cock.get())
            int(self.frooti.get())
            int(self.thumsup.get())
            int(self.limca.get())
            int(self.sprite.get())

            # ______________________________________________Set Price Variables
            # cosmetic Variables
            int(self.soap_price.get())
            int(self.face_cream_price.get())
            int(self.hair_s_price.get())
            int(self.hair_g_price.get())
            int(self.lotion_price.get())
            int(self.face_wash_price.get())

            # Grosery Variables
            int(self.rice_price.get())
            int(self.food_oil_price.get())
            int(self.wheat_price.get())
            int(self.sugar_price.get())
            int(self.daal_price.get())
            int(self.tea_price.get())

            # colddrink Variables
            int(self.maza_price.get())
            int(self.cock_price.get())
            int(self.frooti_price.get())
            int(self.thumsup_price.get())
            int(self.limca_price.get())
            int(self.sprite_price.get())

        except:
            messagebox.showerror("Not allowed character", "Not valid a stock")
            self.reset()
        else:
            var = messagebox.askyesno("Add Products")

            if var == True:
                soap = self.soap.get() + self.soap_new.get()
                face_cream = self.face_cream.get() + self.face_cream_new.get()
                hair_spray = self.hair_s.get() + self.hair_s_new.get()
                hair_gail = self.hair_g.get() + self.hair_g_new.get()
                lotion = self.lotion.get() + self.lotion_new.get()
                f_wash = self.face_wash.get() + self.face_wash_new.get()

                tea = self.tea.get() + self.tea_new.get()
                daal = self.daal.get() + self.daal_new.get()
                rice = self.rice.get() + self.rice_new.get()
                oil = self.food_oil.get() + self.food_oil_new.get()
                sugar = self.sugar.get() + self.sugar_new.get()
                wheat = self.wheat.get() + self.wheat_new.get()

                thumsup = self.thumsup.get() + self.thumsup_new.get()
                limca = self.limca.get() + self.limca_new.get()
                frooti = self.frooti.get() + self.frooti_new.get()
                cock = self.cock.get() + self.cock_new.get()
                sprite = self.sprite.get() + self.sprite_new.get()
                maza = self.maza.get() + self.maza_new.get()
                self.object.write_stock_coldrinks(Thums_Up=[self.thumsup_price.get(), thumsup],
                                                  Frooti=[self.frooti_price.get(), frooti],
                                                  Cock=[self.cock_price.get(), cock],
                                                  Sprite=[self.sprite_price.get(), sprite],
                                                  Maza=[self.maza_price.get(), maza],
                                                  Limca=[self.limca_price.get(), limca])
                self.object.write_stock_grocerry(Tea=[self.tea_price.get(), tea], Daal=[self.daal_price.get(), daal],
                                                 Rice=[self.rice_price.get(), rice],
                                                 Food_Oil=[self.food_oil_price.get(), oil],
                                                 Sugar=[self.sugar_price.get(), sugar],
                                                 Wheat=[self.wheat_price.get(), wheat])
                self.object.write_stock_comsetic(Soap=[self.soap_price.get(), soap],
                                                 Face_Cream=[self.face_cream_price.get(), face_cream],
                                                 Hair_Spray=[self.hair_s_price.get(), hair_spray],
                                                 Hair_Gel=[self.hair_g_price.get(), hair_gail],
                                                 Body_Lotion=[self.lotion_price.get(), lotion],
                                                 Face_Wash=[self.face_wash_price.get(), f_wash])
                self.object.sorce("Incoming")
                self.object.Writer()
                self.read_stock()
                self.reset()

    def new_stock(self):
        font = self.font
        pady = 5
        width = 0
        bg=self.bgcolor
        fg = 'white'
        fg_value = '#00FF00'

        def fun1():
            var1 = tk.Label(self.f5, text=f"{self.cosmetic[0]} Avalable Stock Is\t", bg=bg,
                            font=font, width=width, fg=fg).grid(row=0, column=0, sticky='w', pady=pady)
            var2 = tk.Label(self.f5, text=f"{self.cosmetic[1]} Avalable Stock Is\t", bg=bg,
                            font=font, width=width, fg=fg).grid(row=1, column=0, sticky='w', pady=pady)
            var3 = tk.Label(self.f5, text=f"{self.cosmetic[2]} Avalable Stock Is\t", bg=bg,
                            font=font, width=width, fg=fg).grid(row=2, column=0, sticky='w', pady=pady)
            var4 = tk.Label(self.f5, text=f"{self.cosmetic[3]} Avalable Stock Is\t", bg=bg,
                            font=font, width=width, fg=fg).grid(row=3, column=0, sticky='w', pady=pady)
            var5 = tk.Label(self.f5, text=f"{self.cosmetic[4]} Avalable Stock Is\t", bg=bg,
                            font=font, width=width, fg=fg).grid(row=4, column=0, sticky='w', pady=pady)
            var6 = tk.Label(self.f5, text=f"{self.cosmetic[5]} Avalable Stock Is\t", bg=bg,
                            font=font, width=width, fg=fg).grid(row=5, column=0, sticky='w')

            value1 = tk.Label(self.f5, text=self.soap_new.get(), bg=bg, font=font, fg=fg_value).grid(row=0, column=1)
            value2 = tk.Label(self.f5, text=self.face_cream_new.get(), bg=bg, font=font, fg=fg_value).grid(row=1,
                                                                                                              column=1)
            value3 = tk.Label(self.f5, text=self.hair_s_new.get(), bg=bg, font=font, fg=fg_value).grid(row=2,
                                                                                                          column=1)
            value4 = tk.Label(self.f5, text=self.hair_g_new.get(), bg=bg, font=font, fg=fg_value).grid(row=3,
                                                                                                          column=1)
            value5 = tk.Label(self.f5, text=self.lotion_new.get(), bg=bg, font=font, fg=fg_value).grid(row=4,
                                                                                                          column=1)
            value6 = tk.Label(self.f5, text=self.face_wash_new.get(), bg=bg, font=font, fg=fg_value).grid(row=5,
                                                                                                             column=1)

        def fun2():
            var1 = tk.Label(self.f5, text=f"\t{self.grocerry[0]} Avalable Stock Is\t", bg=bg,
                            font=font, width=width, fg=fg).grid(row=0, column=2, sticky='w', pady=pady)
            var2 = tk.Label(self.f5, text=f"\t{self.grocerry[1]} Avalable Stock Is\t", bg=bg,
                            font=font, width=width, fg=fg).grid(row=1, column=2, sticky='w', pady=pady)
            var3 = tk.Label(self.f5, text=f"\t{self.grocerry[2]} Avalable Stock Is\t", bg=bg,
                            font=font, width=width, fg=fg).grid(row=2, column=2, sticky='w', pady=pady)
            var4 = tk.Label(self.f5, text=f"\t{self.grocerry[3]} Avalable Stock Is\t", bg=bg,
                            font=font, width=width, fg=fg).grid(row=3, column=2, sticky='w', pady=pady)
            var5 = tk.Label(self.f5, text=f"\t{self.grocerry[4]} Avalable Stock Is\t", bg=bg,
                            font=font, width=width, fg=fg).grid(row=4, column=2, sticky='w', pady=pady)
            var6 = tk.Label(self.f5, text=f"\t{self.grocerry[5]} Avalable Stock Is\t", bg=bg,
                            font=font, width=width, fg=fg).grid(row=5, column=2, sticky='w')

            value1 = tk.Label(self.f5, text=self.tea_new.get(), bg=bg, font=font, fg=fg_value).grid(row=0, column=4)
            value2 = tk.Label(self.f5, text=self.daal_new.get(), bg=bg, font=font, fg=fg_value).grid(row=1,
                                                                                                        column=4)
            value3 = tk.Label(self.f5, text=self.rice_new.get(), bg=bg, font=font, fg=fg_value).grid(row=2,
                                                                                                        column=4)
            value4 = tk.Label(self.f5, text=self.food_oil_new.get(), bg=bg, font=font, fg=fg_value).grid(row=3,
                                                                                                            column=4)
            value5 = tk.Label(self.f5, text=self.sugar_new.get(), bg=bg, font=font, fg=fg_value).grid(row=4,
                                                                                                         column=4)
            value6 = tk.Label(self.f5, text=self.wheat_new.get(), bg=bg, font=font, fg=fg_value).grid(row=5,
                                                                                                         column=4)

        def fun3():
            var1 = tk.Label(self.f5, text=f"\t{self.coldrink[0]} Avalable Stock Is\t", bg=bg,
                            font=font, width=width, fg=fg).grid(row=0, column=5, sticky='w', pady=pady)
            var2 = tk.Label(self.f5, text=f"\t{self.coldrink[1]} Avalable Stock Is\t", bg=bg,
                            font=font, width=width, fg=fg).grid(row=1, column=5, sticky='w', pady=pady)
            var3 = tk.Label(self.f5, text=f"\t{self.coldrink[2]} Avalable Stock Is\t", bg=bg,
                            font=font, width=width, fg=fg).grid(row=2, column=5, sticky='w', pady=pady)
            var4 = tk.Label(self.f5, text=f"\t{self.coldrink[3]} Avalable Stock Is\t", bg=bg,
                            font=font, width=width, fg=fg).grid(row=3, column=5, sticky='w', pady=pady)
            var5 = tk.Label(self.f5, text=f"\t{self.coldrink[4]} Avalable Stock Is\t", bg=bg,
                            font=font, width=width, fg=fg).grid(row=4, column=5, sticky='w', pady=pady)
            var6 = tk.Label(self.f5, text=f"\t{self.coldrink[5]} Avalable Stock Is\t", bg=bg,
                            font=font, width=width, fg=fg).grid(row=5, column=5, sticky='w')

            value1 = tk.Label(self.f5, text=self.thumsup_new.get(), bg=bg, font=font, fg=fg_value).grid(row=0,
                                                                                                           column=6)
            value2 = tk.Label(self.f5, text=self.limca_new.get(), bg=bg, font=font, fg=fg_value).grid(row=1,
                                                                                                         column=6)
            value3 = tk.Label(self.f5, text=self.frooti_new.get(), bg=bg, font=font, fg=fg_value).grid(row=2,
                                                                                                          column=6)
            value4 = tk.Label(self.f5, text=self.cock_new.get(), bg=bg, font=font, fg=fg_value).grid(row=3,
                                                                                                        column=6)
            value5 = tk.Label(self.f5, text=self.sprite_new.get(), bg=bg, font=font, fg=fg_value).grid(row=4,
                                                                                                          column=6)
            value6 = tk.Label(self.f5, text=self.maza_new.get(), bg=bg, font=font, fg=fg_value).grid(row=5,
                                                                                                        column=6)

        fun1()
        fun2()
        fun3()

    def cosmetic_fun(self):

        # __________________________Cosmetic frame___________________________________________________

        cosmetic_frame_x = 10
        cosmetic_frane_y = 20
        bgcolor = self.bgcolor

        bath_lbl = tk.Label(self.f1, text=self.cosmetic[0], font=("times new roman", 18, "bold"), bg=bgcolor,
                            fg="white").grid(row=0, column=0, sticky="w", padx=cosmetic_frame_x, pady=cosmetic_frane_y)
        bath_txt = ttk.Entry(self.f1, textvariable=self.soap, width=15).grid(row=0, column=1,
                                                                             padx=cosmetic_frame_x,
                                                                             pady=cosmetic_frane_y)

        face_cream_lbl = tk.Label(self.f1, text=self.cosmetic[1], font=("times new roman", 18, "bold"), bg=bgcolor,
                                  fg="white").grid(row=1, column=0, sticky="w", padx=cosmetic_frame_x,
                                                   pady=cosmetic_frane_y)
        face_cream_txt = ttk.Entry(self.f1, textvariable=self.face_cream, width=15).grid(row=1, column=1,
                                                                                         padx=cosmetic_frame_x,
                                                                                         pady=cosmetic_frane_y)

        Hair_Spray_lbl = tk.Label(self.f1, text=self.cosmetic[2], font=("times new roman", 18, "bold"), bg=bgcolor,
                                  fg="white").grid(row=2, column=0, sticky="w", padx=cosmetic_frame_x,
                                                   pady=cosmetic_frane_y)
        Hair_Spray_txt = ttk.Entry(self.f1, textvariable=self.hair_s, width=15).grid(row=2, column=1,
                                                                                     padx=cosmetic_frame_x,
                                                                                     pady=cosmetic_frane_y)

        Hair_Gel_lbl = tk.Label(self.f1, text=self.cosmetic[3], font=("times new roman", 18, "bold"), bg=bgcolor,
                                fg="white").grid(row=3, column=0, sticky="w", padx=cosmetic_frame_x,
                                                 pady=cosmetic_frane_y)
        Hair_Gel_txt = ttk.Entry(self.f1, textvariable=self.hair_g, width=15).grid(row=3, column=1,
                                                                                   padx=cosmetic_frame_x,
                                                                                   pady=cosmetic_frane_y)

        Body_Lotion_lbl = tk.Label(self.f1, text=self.cosmetic[4], font=("times new roman", 18, "bold"), bg=bgcolor,
                                   fg="white").grid(row=4, column=0, sticky="w", padx=cosmetic_frame_x,
                                                    pady=cosmetic_frane_y)
        Body_Lotion_txt = ttk.Entry(self.f1, textvariable=self.lotion, width=15).grid(row=4, column=1,
                                                                                      padx=cosmetic_frame_x,
                                                                                      pady=cosmetic_frane_y)

        Face_Wash_lbl = tk.Label(self.f1, text=self.cosmetic[5], font=("times newtk.Spinbox", 18, "bold"), bg=bgcolor,
                                 fg="white").grid(row=5, column=0, sticky="w", padx=cosmetic_frame_x,
                                                  pady=cosmetic_frane_y)
        Face_Wash_txt = ttk.Entry(self.f1, textvariable=self.face_wash, width=15).grid(row=5, column=1,
                                                                                       padx=cosmetic_frame_x,
                                                                                       pady=cosmetic_frane_y)

    def glocerry_fun(self):
        cosmetic_frame_x = 10
        cosmetic_frane_y = 20
        bgcolor = self.bgcolor
        # __________________________grossery frame___________________________________________________

        tea_lbl = tk.Label(self.f2, text=self.grocerry[0], font=("times new roman", 18, "bold"), bg=bgcolor,
                           fg="white").grid(row=1, column=0, sticky="w", padx=cosmetic_frame_x, pady=cosmetic_frane_y)
        tea_txt = ttk.Entry(self.f2, font=("arial", 15), textvariable=self.tea).grid(row=1, column=1,
                                                                                     padx=cosmetic_frame_x,
                                                                                     pady=cosmetic_frane_y)
        daal_lbl = tk.Label(self.f2, text=self.grocerry[1], font=("times new roman", 18, "bold"), bg=bgcolor,
                            fg="white").grid(row=2, column=0, sticky="w", padx=cosmetic_frame_x, pady=cosmetic_frane_y)
        daal_txt = ttk.Entry(self.f2, font=("arial", 15), textvariable=self.daal).grid(row=2, column=1,
                                                                                       padx=cosmetic_frame_x,
                                                                                       pady=cosmetic_frane_y)

        rice_lbl = tk.Label(self.f2, text=self.grocerry[2], font=("times new roman", 18, "bold"), bg=bgcolor,
                            fg="white").grid(row=3, column=0, sticky="w", padx=cosmetic_frame_x, pady=cosmetic_frane_y)
        rice_txt = ttk.Entry(self.f2, font=("arial", 15), textvariable=self.rice).grid(row=3, column=1,
                                                                                       padx=cosmetic_frame_x,
                                                                                       pady=cosmetic_frane_y)

        oil_lbl = tk.Label(self.f2, text=self.grocerry[3], font=("times new roman", 18, "bold"), bg=bgcolor,
                           fg="white").grid(row=4, column=0, sticky="w", padx=cosmetic_frame_x, pady=cosmetic_frane_y)
        oil_txt = ttk.Entry(self.f2, font=("arial", 15), textvariable=self.food_oil).grid(row=4, column=1,
                                                                                          padx=cosmetic_frame_x,
                                                                                          pady=cosmetic_frane_y)
        sugar_lbl = tk.Label(self.f2, text=self.grocerry[4], font=("times new roman", 18, "bold"), bg=bgcolor,
                             fg="white").grid(row=5, column=0, sticky="w", padx=cosmetic_frame_x, pady=cosmetic_frane_y)
        sugar_txt = ttk.Entry(self.f2, font=("arial", 15), textvariable=self.sugar).grid(row=5, column=1,
                                                                                         padx=cosmetic_frame_x,
                                                                                         pady=cosmetic_frane_y)

        wheat_lbl = tk.Label(self.f2, text=self.grocerry[5], font=("times new roman", 18, "bold"), bg=bgcolor,
                             fg="white").grid(row=6, column=0, sticky="w", padx=cosmetic_frame_x, pady=cosmetic_frane_y)
        wheat_txt = ttk.Entry(self.f2, font=("arial", 15), textvariable=self.wheat).grid(row=6, column=1,
                                                                                         padx=cosmetic_frame_x,
                                                                                         pady=cosmetic_frane_y)

    def colddrink_fun(self):
        cosmetic_frame_x = 10
        cosmetic_frane_y = 20
        bgcolor = self.bgcolor

        # __________________________Cold Drink___________________________________________________

        thumsup_lbl = tk.Label(self.f3, text=self.coldrink[0], font=("times new roman", 18, "bold"), bg=bgcolor,
                               fg="white").grid(row=0, column=0, sticky="w", padx=cosmetic_frame_x,
                                                pady=cosmetic_frane_y)
        self.thumsup_txt = ttk.Entry(self.f3, textvariable=self.thumsup, width=18).grid(row=0, column=1,
                                                                                        padx=cosmetic_frame_x,
                                                                                        pady=cosmetic_frane_y)

        limca_lbl = tk.Label(self.f3, text=self.coldrink[1], font=("times new roman", 18, "bold"), bg=bgcolor,
                             fg="white").grid(row=1, column=0, sticky="w", padx=cosmetic_frame_x, pady=cosmetic_frane_y)
        self.limca_txt = ttk.Entry(self.f3, textvariable=self.limca, width=18).grid(row=1, column=1,
                                                                                    padx=cosmetic_frame_x,
                                                                                    pady=cosmetic_frane_y)
        frooty_lbl = tk.Label(self.f3, text=self.coldrink[2], font=("times new roman", 18, "bold"), bg=bgcolor,
                              fg="white").grid(row=2, column=0, sticky="w", padx=cosmetic_frame_x,
                                               pady=cosmetic_frane_y)
        self.frooty_txt = ttk.Entry(self.f3, textvariable=self.frooti, width=18).grid(row=2, column=1,
                                                                                      padx=cosmetic_frame_x,
                                                                                      pady=cosmetic_frane_y)
        cock_lbl = tk.Label(self.f3, text=self.coldrink[3], font=("times new roman", 18, "bold"), bg=bgcolor,
                            fg="white").grid(row=3, column=0, sticky="w", padx=cosmetic_frame_x, pady=cosmetic_frane_y)
        self.cock_txt = ttk.Entry(self.f3, textvariable=self.cock, width=18).grid(row=3, column=1,
                                                                                  padx=cosmetic_frame_x,
                                                                                  pady=cosmetic_frane_y)
        sprite_lbl = tk.Label(self.f3, text=self.coldrink[4], font=("times new roman", 18, "bold"), bg=bgcolor,
                              fg="white").grid(row=4, column=0, sticky="w", padx=cosmetic_frame_x,
                                               pady=cosmetic_frane_y)
        self.sprite_txt = ttk.Entry(self.f3, textvariable=self.sprite, width=18).grid(row=4, column=1,
                                                                                      padx=cosmetic_frame_x,
                                                                                      pady=cosmetic_frane_y)

        maza_lbl = tk.Label(self.f3, text=self.coldrink[5], font=("times new roman", 18, "bold"), bg=bgcolor,
                            fg="white").grid(row=5, column=0, sticky="w", padx=cosmetic_frame_x, pady=cosmetic_frane_y)
        self.maza_txt = ttk.Entry(self.f3, textvariable=self.maza, width=18).grid(row=5, column=1,
                                                                                  padx=cosmetic_frame_x,
                                                                                  pady=cosmetic_frane_y)

        # ADD Pricing Label f4_______________________________________________________________

    def add_price(self):
        gloserry_bg = "#800000"
        gloserry_fg = "cyan"

        cosmetic_bg = "#000080"
        csometic_fg = "white"

        coldrink_bg = "#800080"
        coldrink_fg = "yellow"

        def cosmetic_page():

            try:
                self.frame3.destroy()
            except:
                pass

            try:
                self.frame1.destroy()
            except:
                pass
            try:
                self.frame2.destroy()
            except:
                pass
            bg = "blue"
            self.frame1 = tk.Frame(self.f4, bg=cosmetic_bg)
            self.frame1.pack(fill="both", expand=True)

            LABEL1 = tk.Label(self.frame1, text=self.cosmetic[0], font=self.font, bg=cosmetic_bg, fg=csometic_fg).grid(
                row=0,
                column=0,
                sticky="w")
            LABEL1_ENTRY = ttk.Entry(self.frame1, textvariable=self.soap_price).grid(row=0, column=1, padx=20, pady=21)

            LABEL2 = tk.Label(self.frame1, text=self.cosmetic[1], font=self.font, bg=cosmetic_bg, fg=csometic_fg).grid(
                row=1,
                column=0,
                sticky="w")
            LABEL2_ENTRY = ttk.Entry(self.frame1, textvariable=self.face_cream_price).grid(row=1, column=1, padx=20,
                                                                                           pady=21)

            LABEL3 = tk.Label(self.frame1, text=self.cosmetic[2], font=self.font, bg=cosmetic_bg, fg=csometic_fg).grid(
                row=2,
                column=0,
                sticky="w")
            LABEL3_ENTRY = ttk.Entry(self.frame1, textvariable=self.hair_s_price).grid(row=2, column=1, padx=20,
                                                                                       pady=21)

            LABEL4 = tk.Label(self.frame1, text=self.cosmetic[3], font=self.font, bg=cosmetic_bg, fg=csometic_fg).grid(
                row=3,
                column=0,
                sticky="w")
            LABEL4_ENTRY = ttk.Entry(self.frame1, textvariable=self.hair_g_price).grid(row=3, column=1, padx=20,
                                                                                       pady=21)

            LABEL5 = tk.Label(self.frame1, text=self.cosmetic[4], font=self.font, bg=cosmetic_bg, fg=csometic_fg).grid(
                row=4,
                column=0,
                sticky="w")
            LABEL5_ENTRY = ttk.Entry(self.frame1, textvariable=self.lotion_price).grid(row=4, column=1, padx=20,
                                                                                       pady=21)

            LABEL6 = tk.Label(self.frame1, text=self.cosmetic[5], font=self.font, bg=cosmetic_bg, fg=csometic_fg).grid(
                row=5,
                column=0,
                sticky="w")
            LABEL6_ENTRY = ttk.Entry(self.frame1, textvariable=self.face_wash_price).grid(row=5, column=1, padx=20,
                                                                                          pady=21)

        def grocerry_page():
            try:
                self.frame3.destroy()
            except:
                pass

            try:
                self.frame1.destroy()
            except:
                pass
            try:
                self.frame2.destroy()
            except:
                pass
            bg = "#800000"
            self.frame2 = tk.Frame(self.f4, bg=gloserry_bg)
            self.frame2.pack(fill="both", expand=True)
            LABEL1 = tk.Label(self.frame2, text=self.grocerry[0], font=self.font, bg=gloserry_bg, fg=gloserry_fg).grid(
                row=0,
                column=0,
                sticky="w")
            LABEL1_ENTRY = ttk.Entry(self.frame2, textvariable=self.tea_price).grid(row=0, column=1, padx=20, pady=21)

            LABEL2 = tk.Label(self.frame2, text=self.grocerry[1], font=self.font, bg=gloserry_bg, fg=gloserry_fg).grid(
                row=1,
                column=0,
                sticky="w")
            LABEL2_ENTRY = ttk.Entry(self.frame2, textvariable=self.daal_price).grid(row=1, column=1, padx=20, pady=21)

            LABEL3 = tk.Label(self.frame2, text=self.grocerry[2], font=self.font, bg=gloserry_bg, fg=gloserry_fg).grid(
                row=2,
                column=0,
                sticky="w")
            LABEL3_ENTRY = ttk.Entry(self.frame2, textvariable=self.rice_price).grid(row=2, column=1, padx=20, pady=21)

            LABEL4 = tk.Label(self.frame2, text=self.grocerry[3], font=self.font, bg=gloserry_bg, fg=gloserry_fg).grid(
                row=3,
                column=0,
                sticky="w")
            LABEL4_ENTRY = ttk.Entry(self.frame2, textvariable=self.food_oil_price).grid(row=3, column=1, padx=20,
                                                                                         pady=21)

            LABEL5 = tk.Label(self.frame2, text=self.grocerry[4], font=self.font, bg=gloserry_bg, fg=gloserry_fg).grid(
                row=4,
                column=0,
                sticky="w")
            LABEL5_ENTRY = ttk.Entry(self.frame2, textvariable=self.sugar_price).grid(row=4, column=1, padx=20, pady=21)

            LABEL6 = tk.Label(self.frame2, text=self.grocerry[5], font=self.font, bg=gloserry_bg, fg=gloserry_fg).grid(
                row=5,
                column=0,
                sticky="w")
            LABEL6_ENTRY = ttk.Entry(self.frame2, textvariable=self.wheat_price).grid(row=5, column=1, padx=20, pady=21)

        def colddrink_page():

            try:
                self.frame3.destroy()
            except:
                pass

            try:
                self.frame1.destroy()
            except:
                pass
            try:
                self.frame2.destroy()
            except:
                pass

            self.frame3 = tk.Frame(self.f4, bg=coldrink_bg)
            self.frame3.pack(fill="both", expand=True)
            LABEL1 = tk.Label(self.frame3, text=self.coldrink[0], font=self.font, bg=coldrink_bg, fg=coldrink_fg).grid(
                row=0,
                column=0,
                sticky="w")
            LABEL1_ENTRY = ttk.Entry(self.frame3, textvariable=self.thumsup_price).grid(row=0, column=1, padx=20,
                                                                                        pady=21)

            LABEL2 = tk.Label(self.frame3, text=self.coldrink[1], font=self.font, bg=coldrink_bg, fg=coldrink_fg).grid(
                row=1,
                column=0,
                sticky="w")
            LABEL2_ENTRY = ttk.Entry(self.frame3, textvariable=self.limca_price).grid(row=1, column=1, padx=20, pady=21)

            LABEL3 = tk.Label(self.frame3, text=self.coldrink[2], font=self.font, bg=coldrink_bg, fg=coldrink_fg).grid(
                row=2,
                column=0,
                sticky="w")
            LABEL3_ENTRY = ttk.Entry(self.frame3, textvariable=self.frooti_price).grid(row=2, column=1, padx=20,
                                                                                       pady=21)

            LABEL4 = tk.Label(self.frame3, text=self.coldrink[3], font=self.font, bg=coldrink_bg, fg=coldrink_fg).grid(
                row=3,
                column=0,
                sticky="w")
            LABEL4_ENTRY = ttk.Entry(self.frame3, textvariable=self.cock_price).grid(row=3, column=1, padx=20, pady=21)

            LABEL5 = tk.Label(self.frame3, text=self.coldrink[4], font=self.font, bg=coldrink_bg, fg=coldrink_fg).grid(
                row=4,
                column=0,
                sticky="w")
            LABEL5_ENTRY = ttk.Entry(self.frame3, textvariable=self.sprite_price).grid(row=4, column=1, padx=20,
                                                                                       pady=21)

            LABEL6 = tk.Label(self.frame3, text=self.coldrink[5], font=self.font, bg=coldrink_bg, fg=coldrink_fg).grid(
                row=5,
                column=0,
                sticky="w")
            LABEL6_ENTRY = ttk.Entry(self.frame3, textvariable=self.maza_price).grid(row=5, column=1, padx=20, pady=21)

        self.cosmetic_button1 = tk.Button(self.t, highlightbackground=cosmetic_bg, fg=csometic_fg, text="Cosmetic",
                                          width=15, font=("times new roman", 15, "bold"), command=cosmetic_page).grid(
            row=0, column=0, padx=2)
        self.grocerry_button1 = tk.Button(self.t, highlightbackground=gloserry_bg, fg=gloserry_fg, text="Grocerry",
                                          width=15, font=("times new roman", 15, "bold"), command=grocerry_page).grid(
            row=0, column=1, padx=2)
        self.coldderink_button1 = tk.Button(self.t, highlightbackground=coldrink_bg, text="Cold Drink", fg=coldrink_fg,
                                            width=15, font=("times new roman", 15, "bold"),
                                            command=colddrink_page).grid(row=0, column=2, padx=2)
        cosmetic_page()

    def reset(self):
        # cosmetic Variables
        self.soap.set(0)
        self.face_cream.set(0)
        self.hair_s.set(0)
        self.hair_g.set(0)
        self.lotion.set(0)
        self.face_wash.set(0)

        # Grosery Variables
        self.rice.set(0)
        self.food_oil.set(0)
        self.wheat.set(0)
        self.sugar.set(0)
        self.daal.set(0)
        self.tea.set(0)

        # colddrink Variables
        self.maza.set(0)
        self.cock.set(0)
        self.frooti.set(0)
        self.thumsup.set(0)
        self.limca.set(0)
        self.sprite.set(0)





class software(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1900x1100")
        self.title("Sitaram")
        color_list=["#074463","purple","maroon",'#483d8b',"#2f4f4f","#ff1493"]
        ranno=random.randrange(0,len(color_list))
        bgcolor =color_list[ranno]



        def f1():



            def k():
                self.title.configure(fg='black',relief='sunken')
                self.title.after(100,lambda :self.title.configure(text='V'))
                self.title.after(500, lambda: self.title.configure(text='Vi'))
                self.title.after(1000, lambda: self.title.configure(text='Vick'))
                self.title.after(1500, lambda: self.title.configure(text='Vicky'))
                self.title.after(2000, lambda: self.title.configure(text='Vicky En'))
                self.title.after(2500, lambda: self.title.configure(text='Vicky Ente'))
                self.title.after(3000, lambda: self.title.configure(text='Vicky Enter'))
                self.title.after(3500, lambda: self.title.configure(text='Vicky Enterp'))
                self.title.after(4000, lambda: self.title.configure(text='Vicky Enterpr'))
                self.title.after(4500, lambda: self.title.configure(text='Vicky Enterpri'))
                self.title.after(5000, lambda: self.title.configure(text='Vicky Enterpris'))
                self.title.after(5000, lambda: self.title.configure(text='Vicky Enterprise'))
                self.title.after(5000, lambda: self.title.configure(text='Vicky Enterprises'))


                self.title.after(6500,k1)



            def k1():
                self.title.configure(bg=bgcolor, fg='White',font=("times new roman", 30, "bold"),bd=12,relief='groove',highlightthickness=1)
                self.title.configure(text='')
                self.title.configure(text='Billing Software')
                self.title.after(1900,lambda :self.title.configure(text=''))
                self.title.after(2000, k)




            k1()

        def clock():
            time2 = time.strftime('%H:%M:%S')
            self.label.configure(text=time2)
            if time2 == "11:47:09":
                messagebox.showinfo("Good afternoon","Have A Nice Day")
            if time2 == "11:50:01":
                messagebox.showinfo("Dinner Break","Hey go to the dinner")
            if time2 == "11:51:01":
                messagebox.showinfo("end","Hey please go to the home")
            self.after(200,clock)


        self.title = tk.Label(self, text="Billing Software", bd=12, relief="groove", bg=bgcolor, fg="white",
                         font=("times new roman", 30, "bold"))
        self.title.pack(fill=tk.X)
        self.after(300,f1)
        self.inflect_object=inflect.engine()
        self.configure(bg='black')
        self.label = tk.Label(self, bg=bgcolor,font=("Arial",20,"bold"),fg='white')
        self.label.place(x=20,y=19,width=100)
        self.after(200, clock)



        self.file_save_adress = "/Users/vicky/Desktop/Bills"
        # Maximum Product quantity
        self.value = 100
        self.cosmetic = ['Soap', 'Face Cream', 'Hair Spray', 'Hair Gel', 'Body Lotion', 'Face Wash']
        self.grocerry = ['Tea', 'Daal', 'Rice', "Food Oil", 'Sugar', 'Wheat']
        self.coldrink = ['Thums Up', 'Limca', 'Frooti', 'Cock', 'Sprite', 'Maza']
        # _____________________________________________Price set each product
        # Price Set
        self.All_price=0
        # Cosmetic
        self.soap1 =tk.IntVar()
        self.face_cream1 =tk.IntVar()
        self.hair_g1 =tk.IntVar()
        self.hair_s1 =tk.IntVar()
        self.lotion1 =tk.IntVar()
        self.face_wash1 =tk.IntVar()

        # Grocerry
        self.tea1 =tk.IntVar()
        self.daal_1 =tk.IntVar()
        self.rice1 =tk.IntVar()
        self.food_oil1 =tk.IntVar()
        self.sugar1 =tk.IntVar()
        self.wheat1 =tk.IntVar()

        # colddrink
        self.thumsup1 =tk.IntVar()
        self.limca1 =tk.IntVar()
        self.frooti1 =tk.IntVar()
        self.cock1 =tk.IntVar()
        self.sprite1 =tk.IntVar()
        self.maza1 =tk.IntVar()

        # _______________________________________________________Variables


        # cosmetic Variables

        self.soap = tk.IntVar()
        self.face_cream = tk.IntVar()
        self.hair_s = tk.IntVar()
        self.hair_g = tk.IntVar()
        self.lotion = tk.IntVar()
        self.face_wash = tk.IntVar()

        # Grosery Variables
        self.rice = tk.IntVar()
        self.food_oil = tk.IntVar()
        self.wheat = tk.IntVar()
        self.sugar = tk.IntVar()
        self.daal = tk.IntVar()
        self.tea = tk.IntVar()

        # colddrink Variables
        self.maza = tk.IntVar()
        self.cock = tk.IntVar()
        self.frooti = tk.IntVar()
        self.thumsup = tk.IntVar()
        self.limca = tk.IntVar()
        self.sprite = tk.IntVar()
        #___________________________________________Maxx stock of product
        # cosmetic Variables
        self.soap_max = tk.IntVar()
        self.face_cream_max = tk.IntVar()
        self.hair_s_max = tk.IntVar()
        self.hair_g_max = tk.IntVar()
        self.lotion_max = tk.IntVar()
        self.face_wash_max = tk.IntVar()

        # Grosery Variables
        self.rice_max = tk.IntVar()
        self.food_oil_max = tk.IntVar()
        self.wheat_max = tk.IntVar()
        self.sugar_max = tk.IntVar()
        self.daal_max = tk.IntVar()
        self.tea_max = tk.IntVar()

        # colddrink Variables
        self.maza_max = tk.IntVar()
        self.cock_max = tk.IntVar()
        self.frooti_max = tk.IntVar()
        self.thumsup_max = tk.IntVar()
        self.limca_max = tk.IntVar()
        self.sprite_max = tk.IntVar()
        #_________________________________________________

        # Total product Price
        self.cosmetic_price = tk.StringVar()
        self.grossery_price = tk.StringVar()
        self.cold_drink_price = tk.StringVar()

        self.cosmetic_tax = tk.StringVar()
        self.grossery_tax = tk.StringVar()
        self.cold_drink_tax = tk.StringVar()
        # Custumor
        self.c_name = tk.StringVar()
        self.c_phn = tk.StringVar()
        self.c_bill_no = tk.StringVar()
        self.c_search_bill = tk.StringVar()


        self.genrated_bill_no = self.bill_no()
        self.c_search_bill.set(self.genrated_bill_no)
        self.object=Stock()
        self.reader()
        #______________________________________________________________________Creating A Menu Bar
        self.Main_Menu = tk.Menu(self)
        self.sub = tk.Menu(self.Main_Menu)
        self.Main_Menu.add_cascade(label="Check Stock", menu=self.sub)
        self.configure(menu=self.Main_Menu)
        self.sub.add_command(label="Click Here", command=self.new)
        self.configure(menu=self.Main_Menu)
       # audio(1)


        def on_click(event):
            self.cphn_txt.configure(state="normal")
            #audio(2)

            if self.c_name.get()=="Enter A Name":
                self.cphn_txt.delete(0,tk.END)
        def out(event):
            if len(self.c_name.get())==0:
                self.cphn_txt.insert(0, "Enter A Name")
                self.cphn_txt.configure(state="disable")
        def on_click1(event):
            self.cname_txt.configure(state="normal")
            #audio(3)

            if self.cname_txt.get()=="Enter A Ph.No":
                self.cname_txt.delete(0,tk.END)
        def out1(event):
            if len(self.cname_txt.get())==0 or len(self.cname_txt.get())!=10:
                self.cname_txt.delete(0,tk.END)
                self.cname_txt.insert(0, "Enter A Ph.No")
                self.cname_txt.configure(state="disable")
        def key(event):
            if len(self.cname_txt.get())!=0:
                try:
                    int(self.cname_txt.get())
                except:
                    messagebox.showwarning("Please input a only integer number not a character")
                    audio("Please input a only integer number not a character")
                    self.cname_txt.delete(0, tk.END)
        def bill_release(event):
            if len(cbill_txt.get())==0:
                try:
                    int(cbill_txt.get())
                except:
                    cbill_txt.after(500,lambda :audio(4))
                    cbill_txt.after(100, lambda: self.c_search_bill.set("S"))
                    cbill_txt.after(150, lambda: self.c_search_bill.set("Se"))
                    cbill_txt.after(200, lambda: self.c_search_bill.set("Sea"))
                    cbill_txt.after(250, lambda: self.c_search_bill.set("Sear"))
                    cbill_txt.after(300, lambda: self.c_search_bill.set("Searc"))
                    cbill_txt.after(350, lambda: self.c_search_bill.set("Search"))
                    cbill_txt.after(400, lambda: self.c_search_bill.set("Search B"))
                    cbill_txt.after(450, lambda: self.c_search_bill.set("Search Bi"))
                    cbill_txt.after(500, lambda: self.c_search_bill.set("Search Bil"))
                    cbill_txt.after(560, lambda: self.c_search_bill.set("Search Bill"))




                cbill_txt.icursor(0)
        def bill_press(event):
            if cbill_txt.get()=='Search Bill':
                cbill_txt.delete(0,tk.END)

        def bill_press_B(event):
            if cbill_txt.get()=='Search Bill':
                cbill_txt.icursor(0)




        # _________________Custumor Detail Frame_____________________________________



        f1 = tk.LabelFrame(self, text="Custumor Details", font=("times new roman", "15", "bold"), bg=bgcolor, fg="gold",
                           bd=10, relief="groove")
        f1.place(x=0, y=80, relwidth=1)


        cname_lbl = tk.Label(f1, text="Custumor Phone Number", font=("times new roman", 18, "bold"), bg=bgcolor,
                             fg="white").grid(row=0, column=2, pady=5, padx=20)
        self.cname_txt = tk.Entry(f1, font=("arial", 15), bd=7, relief="sunken", textvariable=self.c_phn)
        self.cname_txt.grid(row=0,column=3)
        self.cname_txt.insert(0,"Enter A Ph.No")
        self.cname_txt.configure(state="disable")
        self.cname_txt.bind("<Button-1>", on_click1)
        self.cname_txt.bind("<FocusOut>", out1)
        self.cname_txt.bind("<KeyRelease>",key)










        self.cphn_lbl = tk.Label(f1, text="Custumor Name", font=("times new roman", 18, "bold"), bg=bgcolor,
                            fg="white")
        self.cphn_lbl.grid(row=0, column=0, pady=5, padx=20)
        self.cphn_txt = tk.Entry(f1, font=("arial", 15), bd=7, relief="sunken", textvariable=self.c_name)
        self.cphn_txt.grid(row=0,column=1)
        self.cphn_txt.insert(0, "Enter A Name")
        self.cphn_txt.configure(state="disable")
        self.cphn_txt.bind("<Button-1>",on_click)
        self.cphn_txt.bind("<FocusOut>",out)

        cbill_lbl = tk.Label(f1, text="Custumor Bill Number", font=("times new roman", 18, "bold"), bg=bgcolor,
                             fg="white").grid(row=0, column=4, pady=5, padx=20)

        cbill_txt = tk.Entry(f1,font=("arial", 15), bd=7, relief="sunken", textvariable=self.c_search_bill)
        cbill_txt.grid(row=0,column=5)
        cbill_txt.bind("<KeyRelease>",bill_release)
        cbill_txt.bind("<KeyPress>",bill_press)
        cbill_txt.bind("<ButtonRelease>",bill_press_B)
        sumbit = tk.Button(f1, text="Search", width=15, font=("arial", 12, "bold"), bd=7, command=self.find_bill).grid(
            row=0, column=6, pady=5, padx=40)



        self.cosmetic_name = ['Soap', 'Face_Cream', 'Hair_Spray', 'Hair_Gel', 'Body_Lotion', 'Face_Wash']
        self.grocerry_name = ['Tea', 'Daal', 'Rice', "Food_Oil", 'Sugar', 'Wheat']
        self.cold_drink_name = ['Thums_Up', 'Limca', 'Frooti', 'Cock', 'Sprite', 'Maza']
        #_________________________________________________Defimimg Functions
        def thumsup():
            if self.thumsup_max.get()-self.thumsup.get() == 0:
                self.statsvariable.set("Stock Is Emty ")
                messagebox.showwarning("Stock is emty")
            else:
                self.statsvariable.set(
                    f"Price: {self.thumsup1.get()} , Total Stock : {self.thumsup_max.get()}, Available stock :{self.thumsup_max.get() - self.thumsup.get()} ")
            self.total()
        def limca():
            if self.limca_max.get()-self.limca.get() == 0:
                self.statsvariable.set("Stock Is Emty ")
                messagebox.showwarning("Stock is emty")
            else:
                self.statsvariable.set(
                    f"Price: {self.limca1.get()} , Total Stock : {self.limca_max.get()}, Available stock :{self.limca_max.get() - self.limca.get()} ")
            self.total()
        def frooti():
            if self.frooti_max.get()-self.frooti.get() == 0:
                self.statsvariable.set("Stock Is Emty ")
                messagebox.showwarning("Stock is emty")
            else:
                self.statsvariable.set(
                    f"Price: {self.frooti1.get()} , Total Stock : {self.frooti_max.get()}, Available stock :{self.frooti_max.get() - self.frooti.get()} ")
            self.total()
        def cock():
            if self.cock_max.get()-self.cock.get() == 0:
                self.statsvariable.set("Stock Is Emty ")
                messagebox.showwarning("Stock is emty")
            else:
                self.statsvariable.set(
                    f"Price: {self.cock1.get()} , Total Stock : {self.cock_max.get()}, Available stock :{self.cock_max.get() - self.cock.get()} ")
            self.total()
        def sprite():
            if self.sprite_max.get()-self.sprite.get() == 0:
                self.statsvariable.set("Stock Is Emty ")
                messagebox.showwarning("Stock is emty")
            else:
                self.statsvariable.set(
                    f"Price: {self.sprite1.get()} , Total Stock : {self.sprite_max.get()}, Available stock :{self.sprite_max.get() - self.sprite.get()} ")
            self.total()
        def maza():
            if self.maza_max.get()-self.maza.get() == 0:
                self.statsvariable.set("Stock Is Emty ")
                messagebox.showwarning("Stock is emty")
            else:
                self.statsvariable.set(
                    f"Price: {self.maza1.get()} , Total Stock : {self.maza_max.get()}, Available stock :{self.maza_max.get() - self.maza.get()} ")
            self.total()
        def tea():
            if self.tea_max.get()-self.tea.get() == 0:
                self.statsvariable.set("Stock Is Emty ")
                messagebox.showwarning("Stock is emty")
            else:
                self.statsvariable.set(
                    f"Price: {self.tea1.get()} , Total Stock : {self.tea_max.get()}, Available stock :{self.tea_max.get() - self.tea.get()} ")
            self.total()
        def daal():
            if self.daal_max.get()-self.daal.get() == 0:
                self.statsvariable.set("Stock Is Emty ")
                messagebox.showwarning("Stock is emty")
            else:
                self.statsvariable.set(
                    f"Price: {self.daal_1.get()} , Total Stock : {self.daal_max.get()}, Available stock :{self.daal_max.get() - self.daal.get()} ")
            self.total()
        def rice():
            if self.rice_max.get()-self.rice.get() == 0:
                self.statsvariable.set("Stock Is Emty ")
                messagebox.showwarning("Stock is emty")
            else:
                self.statsvariable.set(
                    f"Price: {self.rice1.get()} , Total Stock : {self.rice_max.get()}, Available stock :{self.rice_max.get() - self.rice.get()} ")
            self.total()
        def food_oil():
            if self.food_oil_max.get()-self.food_oil.get() == 0:
                self.statsvariable.set("Stock Is Emty ")
                messagebox.showwarning("Stock is emty")
            else:
                self.statsvariable.set(
                    f"Price: {self.food_oil1.get()} , Total Stock : {self.food_oil_max.get()}, Available stock :{self.food_oil_max.get() - self.food_oil.get()} ")
            self.total()
        def sugar():
            if self.sugar_max.get()-self.sugar.get() == 0:
                self.statsvariable.set("Stock Is Emty ")
                messagebox.showwarning("Stock is emty")
            else:
                self.statsvariable.set(
                    f"Price: {self.sugar1.get()} , Total Stock : {self.sugar_max.get()}, Available stock :{self.sugar_max.get() - self.sugar.get()} ")
            self.total()
        def wheat():
            if self.wheat_max.get()-self.wheat.get() == 0:
                self.statsvariable.set("Stock Is Emty ")
                messagebox.showwarning("Stock is emty")
            else:
                self.statsvariable.set(
                    f"Price: {self.wheat1.get()} , Total Stock : {self.wheat_max.get()}, Available stock :{self.wheat_max.get() - self.wheat.get()} ")
            self.total()
        def soap():
            if self.soap_max.get()-self.soap.get() == 0:
                self.statsvariable.set("Stock Is Emty ")
                messagebox.showwarning("soap Stock emty")
            else:
                self.statsvariable.set(
                    f"Price: {self.soap1.get()} , Total Stock : {self.soap_max.get()}, Available stock :{self.soap_max.get() - self.soap.get()} ")
            self.total()
        def face_cream():
            if self.face_cream_max.get()-self.face_cream.get() == 0:
                self.statsvariable.set("Stock Is Emty ")
                messagebox.showwarning("Stock is emty")
            else:
                self.statsvariable.set(
                    f"Price: {self.face_cream1.get()} , Total Stock : {self.face_cream_max.get()}, Available stock :{self.face_cream_max.get() - self.face_cream.get()} ")
            self.total()
        def hair_s():
            if self.hair_s_max.get()-self.hair_s.get() == 0:
                self.statsvariable.set("Stock Is Emty ")
                messagebox.showwarning("Stock is emty")
            else:
                self.statsvariable.set(
                    f"Price: {self.hair_s1.get()} , Total Stock : {self.hair_s_max.get()}, Available stock :{self.hair_s_max.get() - self.hair_s.get()} ")
            self.total()
        def hair_g():
            if self.hair_g_max.get()-self.hair_g.get() == 0:
                self.statsvariable.set("Stock Is Emty ")
                messagebox.showwarning("Stock is emty")
            else:
                self.statsvariable.set(
                    f"Price: {self.hair_g1.get()} , Total Stock : {self.hair_g_max.get()}, Available stock :{self.hair_g_max.get() - self.hair_g.get()} ")
            self.total()
        def lotion():
            if self.lotion_max.get()-self.lotion.get() == 0:
                self.statsvariable.set("Stock Is Emty ")
                messagebox.showwarning("Stock is emty")
            else:
                self.statsvariable.set(
                    f"Price: {self.lotion1.get()} , Total Stock : {self.lotion_max.get()}, Available stock :{self.lotion_max.get() - self.lotion.get()} ")
            self.total()
        def face_wash():
            if self.face_wash_max.get()-self.face_wash.get() == 0:
                self.statsvariable.set("Stock Is Emty ")
                messagebox.showwarning("Stock is emty")
            else:
                self.statsvariable.set(
                    f"Price: {self.face_wash1.get()} , Total Stock : {self.face_wash_max.get()}, Available stock :{self.face_wash_max.get() - self.face_wash.get()} ")
            self.total()



        # __________________________Cosmetic frame___________________________________________________
        cosmetic_frame_x = 3
        cosmetic_frane_y = 20

        style = ttk.Style()
        style.configure("TSpinbox", background="cyan", foreground="blue")


        f2 = tk.LabelFrame(self, text="Cosmetic", font=("times new roman", "15", "bold"), bg=bgcolor, fg="gold",
                           bd=10, relief="groove")
        f2.place(x=5, y=150, width=350, height=500)

        bath_lbl = tk.Label(f2, text="Bath Soap", font=("times new roman", 18, "bold"), bg=bgcolor,
                            fg="white").grid(row=0, column=0, sticky="w", padx=cosmetic_frame_x, pady=cosmetic_frane_y)
        bath_txt = ttk.Spinbox(f2, textvariable=self.soap, from_=0, to=self.soap_max.get(),command=soap,state="readonly")
        bath_txt.grid(row=0, column=1,
                                                                                        padx=cosmetic_frame_x,
                                                                                        pady=cosmetic_frane_y)


        face_cream_lbl = tk.Label(f2, text="Face Cream", font=("times new roman", 18, "bold"), bg=bgcolor,
                                  fg="white").grid(row=1, column=0, sticky="w", padx=cosmetic_frame_x,
                                                   pady=cosmetic_frane_y)
        face_cream_txt = ttk.Spinbox(f2, textvariable=self.face_cream, from_=0, to=self.face_cream_max.get(),command=face_cream,state="readonly").grid(row=1, column=1,
                                                                                                    padx=cosmetic_frame_x,
                                                                                                    pady=cosmetic_frane_y)

        Hair_Spray_lbl = tk.Label(f2, text="Hair Spray", font=("times new roman", 18, "bold"), bg=bgcolor,
                                  fg="white").grid(row=2, column=0, sticky="w", padx=cosmetic_frame_x,
                                                   pady=cosmetic_frane_y)
        Hair_Spray_txt = ttk.Spinbox(f2, textvariable=self.hair_s, from_=0, to=self.hair_s_max.get(),command=hair_s,state="readonly").grid(row=2, column=1,
                                                                                                padx=cosmetic_frame_x,
                                                                                                pady=cosmetic_frane_y)

        Hair_Gel_lbl = tk.Label(f2, text="Hair Gel", font=("times new roman", 18, "bold"), bg=bgcolor,
                                fg="white").grid(row=3, column=0, sticky="w", padx=cosmetic_frame_x,
                                                 pady=cosmetic_frane_y)
        Hair_Gel_txt = ttk.Spinbox(f2, textvariable=self.hair_g, from_=0, to=self.hair_g_max.get(),command=hair_g,state="readonly").grid(row=3, column=1,
                                                                                              padx=cosmetic_frame_x,
                                                                                              pady=cosmetic_frane_y)

        Body_Lotion_lbl = tk.Label(f2, text="Body Lotion", font=("times new roman", 18, "bold"), bg=bgcolor,
                                   fg="white").grid(row=4, column=0, sticky="w", padx=cosmetic_frame_x,
                                                    pady=cosmetic_frane_y)
        Body_Lotion_txt = ttk.Spinbox(f2, textvariable=self.lotion, from_=0, to=self.lotion_max.get(),command=lotion,state="readonly").grid(row=4, column=1,
                                                                                                 padx=cosmetic_frame_x,
                                                                                                 pady=cosmetic_frane_y)

        Face_Wash_lbl = tk.Label(f2, text="Face Wash", font=("times newtk.Spinbox", 18, "bold"), bg=bgcolor,
                                 fg="white").grid(row=5, column=0, sticky="w", padx=cosmetic_frame_x,
                                                  pady=cosmetic_frane_y)
        Face_Wash_txt = ttk.Spinbox(f2, textvariable=self.face_wash, from_=0, to=self.face_wash_max.get(),command=face_wash,state="readonly").grid(row=5, column=1,
                                                                                                  padx=cosmetic_frame_x,
                                                                                                  pady=cosmetic_frane_y)

        # __________________________grossery frame___________________________________________________

        f3 = tk.LabelFrame(self, text="Grossery", font=("times new roman", "15", "bold"), bg=bgcolor, fg="gold",
                           bd=10, relief="groove")
        f3.place(x=350, y=150, width=330, height=500)

        rice_lbl = tk.Label(f3, text="Rice", font=("times new roman", 18, "bold"), bg=bgcolor,
                            fg="white").grid(row=0, column=0, sticky="w", padx=cosmetic_frame_x, pady=cosmetic_frane_y)
        rice_txt = ttk.Spinbox(f3, font=("arial", 15), textvariable=self.rice,from_=0, to=self.rice_max.get(),state="readonly",command=rice).grid(row=0, column=1,
                                                                                    padx=cosmetic_frame_x,
                                                                                    pady=cosmetic_frane_y)

        oil_lbl = tk.Label(f3, text="Food Oil", font=("times new roman", 18, "bold"), bg=bgcolor,
                           fg="white").grid(row=1, column=0, sticky="w", padx=cosmetic_frame_x, pady=cosmetic_frane_y)
        oil_txt = ttk.Spinbox(f3, font=("arial", 15), textvariable=self.food_oil,from_=0, to=self.food_oil_max.get(),command=food_oil,state="readonly").grid(row=1, column=1,
                                                                                       padx=cosmetic_frame_x,
                                                                                       pady=cosmetic_frane_y)

        wheat_lbl = tk.Label(f3, text="Wheat", font=("times new roman", 18, "bold"), bg=bgcolor,
                             fg="white").grid(row=2, column=0, sticky="w", padx=cosmetic_frame_x, pady=cosmetic_frane_y)
        wheat_txt = ttk.Spinbox(f3, font=("arial", 15), textvariable=self.wheat,from_=0, to=self.wheat_max.get(),command=wheat,state="readonly").grid(row=2, column=1,
                                                                                      padx=cosmetic_frame_x,
                                                                                      pady=cosmetic_frane_y)

        sugar_lbl = tk.Label(f3, text="Sugar", font=("times new roman", 18, "bold"), bg=bgcolor,
                             fg="white").grid(row=3, column=0, sticky="w", padx=cosmetic_frame_x, pady=cosmetic_frane_y)
        sugar_txt = ttk.Spinbox(f3, font=("arial", 15), textvariable=self.sugar,from_=0, to=self.sugar_max.get(),command=sugar,state="readonly").grid(row=3, column=1,
                                                                                      padx=cosmetic_frame_x,
                                                                                      pady=cosmetic_frane_y)

        daal_lbl = tk.Label(f3, text="Daal", font=("times new roman", 18, "bold"), bg=bgcolor,
                            fg="white").grid(row=4, column=0, sticky="w", padx=cosmetic_frame_x, pady=cosmetic_frane_y)
        daal_txt = ttk.Spinbox(f3, font=("arial", 15), textvariable=self.daal,from_=0, to=self.daal_max.get(),command=daal,state="readonly").grid(row=4, column=1,
                                                                                    padx=cosmetic_frame_x,
                                                                                    pady=cosmetic_frane_y)

        tea_lbl = tk.Label(f3, text="Tea", font=("times new roman", 18, "bold"), bg=bgcolor,
                           fg="white").grid(row=5, column=0, sticky="w", padx=cosmetic_frame_x, pady=cosmetic_frane_y)
        tea_txt = ttk.Spinbox(f3, font=("arial", 15), textvariable=self.tea,from_=0, to=self.tea_max.get(),command=tea,state="readonly").grid(row=5, column=1,
                                                                                  padx=cosmetic_frame_x,
                                                                                  pady=cosmetic_frane_y)

        # __________________________Cold Drink___________________________________________________

        f4 = tk.LabelFrame(self, text="Cold Drink", font=("times new roman", "15", "bold"), bg=bgcolor, fg="gold",
                           bd=10, relief="groove")
        f4.place(x=680, y=150, width=355, height=500)


        maza_lbl = tk.Label(f4, text="Maza", font=("times new roman", 18, "bold"), bg=bgcolor,
                            fg="white").grid(row=0, column=0, sticky="w", padx=cosmetic_frame_x, pady=cosmetic_frane_y)
        maza_txt = ttk.Spinbox(f4, textvariable=self.maza,from_=0, to=self.maza_max.get(),command=maza,state="readonly").grid(row=0, column=1, padx=cosmetic_frame_x,
                                                                pady=cosmetic_frane_y)

        cock_lbl = tk.Label(f4, text="Cock", font=("times new roman", 18, "bold"), bg=bgcolor,
                            fg="white").grid(row=1, column=0, sticky="w", padx=cosmetic_frame_x, pady=cosmetic_frane_y)
        cock_txt = ttk.Spinbox(f4, textvariable=self.cock,from_=0, to=self.cock_max.get(),command=cock,state="readonly").grid(row=1, column=1, padx=cosmetic_frame_x,
                                                                pady=cosmetic_frane_y)

        frooty_lbl = tk.Label(f4, text="Frooti", font=("times new roman", 18, "bold"), bg=bgcolor,
                              fg="white").grid(row=2, column=0, sticky="w", padx=cosmetic_frame_x,
                                               pady=cosmetic_frane_y)
        frooty_txt = ttk.Spinbox(f4, textvariable=self.frooti,from_=0, to=self.frooti_max.get(),command=frooti,state="readonly").grid(row=2, column=1, padx=cosmetic_frame_x,
                                                                    pady=cosmetic_frane_y)

        thumsup_lbl = tk.Label(f4, text="Thums Up", font=("times new roman", 18, "bold"), bg=bgcolor,
                               fg="white").grid(row=3, column=0, sticky="w", padx=cosmetic_frame_x,
                                                pady=cosmetic_frane_y)
        thumsup_txt = ttk.Spinbox(f4, textvariable=self.thumsup,from_=0, to=self.thumsup_max.get(),command=thumsup,state="readonly").grid(row=3, column=1, padx=cosmetic_frame_x,
                                                                      pady=cosmetic_frane_y)

        limca_lbl = tk.Label(f4, text="Limca", font=("times new roman", 18, "bold"), bg=bgcolor,
                             fg="white").grid(row=4, column=0, sticky="w", padx=cosmetic_frame_x, pady=cosmetic_frane_y)
        limca_txt = ttk.Spinbox(f4, textvariable=self.limca,from_=0, to=self.limca_max.get(),command=limca,state="readonly").grid(row=4, column=1, padx=cosmetic_frame_x,
                                                                  pady=cosmetic_frane_y)

        sprite_lbl = tk.Label(f4, text="Sprite", font=("times new roman", 18, "bold"), bg=bgcolor,
                              fg="white").grid(row=5, column=0, sticky="w", padx=cosmetic_frame_x,
                                               pady=cosmetic_frane_y)
        sprite_txt = ttk.Spinbox(f4, textvariable=self.sprite,from_=0, to=self.sprite_max.get(),command=sprite,state="readonly").grid(row=5, column=1, padx=cosmetic_frame_x,
                                                                    pady=cosmetic_frane_y)

        # __________________________Bill frame___________________________________________________

        f5 = tk.Frame(self, relief="groove", bd=10)
        f5.place(x=1050, y=150, width=390, height=500)
        bill_tittle = tk.Label(f5, text="Bill Area", font=("Arial", 15, "bold"), bd=7, relief="groove")
        bill_tittle.pack(fill=tk.X)
        scrool_y = tk.Scrollbar(f5)
        scrool_y.pack(side="right", fill=tk.Y)
        self.textarea = tk.Text(f5, yscrollcommand=scrool_y.set,highlightbackground='red',background='yellow',borderwidth=2,font='didot')
        self.textarea.pack(fill="both", expand=True)
        scrool_y.configure(command=self.textarea.yview)

        # __________________________Button frame___________________________________________________

        f6 = tk.LabelFrame(self, text="Bill Menu", font=("times new roman", "15", "bold"), bg=bgcolor, fg="gold",
                           bd=10, relief="groove")
        f6.place(x=0, y=650, relwidth=1, height=200)

        m1_lbl = tk.Label(f6, text="Total Cosmetic Price", font=("times new roman", 14, "bold"), bg=bgcolor,
                          fg="white").grid(row=0, column=0, padx=20, pady=5, sticky="w")
        m1_txt = tk.Entry(f6, width=18, font=("Arial", 20, "bold"), bd=3,state="readonly",textvariable=self.cosmetic_price).grid(row=0,
                                                                                                                 column=1,
                                                                                                                 padx=10,
                                                                                                                 pady=5)

        m2_lbl = tk.Label(f6, text="Total Grossery Price", font=("times new roman", 14, "bold"), bg=bgcolor,
                          fg="white").grid(row=1, column=0, padx=20, pady=5, sticky="w")
        m2_txt = tk.Entry(f6, width=18, font=("Arial", 20, "bold"), bd=3,textvariable=self.grossery_price,state="readonly").grid(row=1,
                                                                                                                 column=1,
                                                                                                                 padx=10,
                                                                                                                 pady=5)

        m3_lbl = tk.Label(f6, text="Total Cold Drink Price", font=("times new roman", 14, "bold"), bg=bgcolor,
                          fg="white").grid(row=2, column=0, padx=20, pady=5, sticky="w")
        m3_txt = tk.Entry(f6, width=18, font=("Arial", 20, "bold"), bd=3,textvariable=self.cold_drink_price,state="readonly").grid(
            row=2, column=1, padx=10, pady=5)

        c1_lbl = tk.Label(f6, text="Total Cost", font=("times new roman", 14, "bold"), bg=bgcolor,
                          fg="white").grid(row=0, column=2, padx=20, pady=5, sticky="w")
        c1_txt = tk.Entry(f6, width=18, font=("Arial", 20, "bold"), bd=3,textvariable=self.cosmetic_tax,state="readonly").grid(row=0,
                                                                                                               column=3,
                                                                                                               padx=10,
                                                                                                               pady=5)
        labelfram=tk.LabelFrame(f6,text="Total Cost",width=300,height=30,bg=bgcolor,fg="white")
        labelfram.place(x=480,y=50,bordermode='inside')
        self.Label=tk.Label(labelfram,text=self.inflect_object.number_to_words(0),width=50,height=7,font=('vardana',12),bg=bgcolor,fg="white")
        self.Label.pack(fill="both",expand=True)
        #self.Label=tk.Label(labelfram,text=self.inflect_object.number_to_words(0),width=50,height=7,bg=bgcolor,fg='white',font=('vardana',12))
        #self.Label.place(x=480,y=50,bordermode='inside')








        #c3_lbl = tk.Label(f6, text="Total Cold Drink Tax", font=("times new roman", 14, "bold"), bg=bgcolor,
                        #  fg="white").grid(row=2, column=2, padx=20, pady=5, sticky="w")
        #c3_txt = tk.Entry(f6, width=18, font=("Arial", 20, "bold"), bd=3, textvariable=self.cold_drink_tax).grid(row=2,
                                                                                              #                   column=3,
                                                                                               #                  padx=10,
                                                                                                #                 pady=5)

        buttun_fram = tk.LabelFrame(f6, bd=7, relief="groove", bg="white",text="Action Buttons")
        buttun_fram.place(x=900, height=120, width=500)


        Generate_Bill_button = tk.Button(buttun_fram, width=13, font=("arial", 14, "bold"), text="Generate Bill",
                                         highlightbackground="cadetblue",
                                         fg="blue", pady=25, bd=5, command=self.bill_area)
        Generate_Bill_button.grid(row=0, column=0, pady=5, padx=15)

        Clear_button = tk.Button(buttun_fram, width=13, font=("arial", 14, "bold"), text="Clear A Bill",
                                 highlightbackground="cadetblue",
                                 fg="blue", pady=25, bd=5, command=self.clear)
        Clear_button.grid(row=0, column=2, pady=5, padx=15)

        exit_button = tk.Button(buttun_fram, width=13, font=("arial", 14, "bold"), text="Exit",
                                 highlightbackground="cadetblue",
                                 fg="blue", pady=25, bd=5,command=self.quit)
        exit_button.grid(row=0, column=4, pady=5, padx=15)

        self.statsvariable=tk.StringVar()
        self.statusbar=tk.Label(f6,textvariable=self.statsvariable,height=2,width=50,justify=tk.LEFT,font=("pt monon",15,"bold"),bg=bgcolor,fg="white")
        self.statusbar.place(x=900,y=134)



    def new(self):
        self.destroy()
        new_class=creating()




    def total(self):

        self.total_cosmetic_price = (
            float((self.soap.get() * self.soap1.get()) +
                  (self.face_cream.get() * self.face_cream1.get()) +
                  (self.face_wash.get() * self.face_wash1.get()) +
                  (self.hair_s.get() * self.hair_s1.get()) +
                  (self.hair_g.get() * self.hair_g1.get()) +
                  (self.lotion.get() * self.lotion1.get())
                  ))


        self.total_grocesrry_price = (
            float((self.rice.get() * self.rice1.get()) +
                  (self.food_oil.get() * self.food_oil1.get()) +
                  (self.wheat.get() * self.wheat1.get()) +
                  (self.sugar.get() * self.sugar1.get()) +
                  (self.daal.get() * self.daal_1.get()) +
                  (self.tea.get() * self.tea1.get())
                  ))

        self.total_cold_drink_price = (
            float((self.thumsup.get() * self.thumsup1.get()) +
                  (self.sprite.get() * self.sprite1.get()) +
                  (self.limca.get() * self.limca1.get()) +
                  (self.cock.get() * self.cock1.get()) +
                  (self.frooti.get() * self.frooti1.get()) +
                  (self.maza.get() * self.maza1.get())
                  ))


        self.cosmetic_price.set(self.total_cosmetic_price)
        self.grossery_price.set(self.total_grocesrry_price)
        self.cold_drink_price.set(self.total_cold_drink_price)
        self.All_price = int(self.total_cosmetic_price + self.total_grocesrry_price + self.total_cold_drink_price)
        self.cosmetic_tax.set(f"Rs {self.All_price}")
        var=self.inflect_object.number_to_words(self.All_price).replace(',','\n')
        self.Label.configure(text=var)

        self.bill_area1()








    def welcome_bill(self):
        self.textarea.delete(1.0, tk.END)
        self.textarea.insert(tk.END, "\t\tWelcome To My Shop")
        self.textarea.insert(tk.END, f"\nBill No:\t{self.c_search_bill.get()}")
        self.textarea.insert(tk.END, f"\nDate:\t{time.strftime('%D')}")
        self.textarea.insert(tk.END, f"\nTime:\t{time.strftime('%T')}")

        self.textarea.insert(tk.END, f"\nCustumer Name:\t{self.c_name.get()}")
        self.textarea.insert(tk.END, f"\nCustumer Ph.No:\t{self.c_phn.get()}")
        self.textarea.insert(tk.END, "\n#################################################")
        self.textarea.insert(tk.END, "Product Name \t Price \t Quantity \t Total")
        self.textarea.insert(tk.END, "\n#################################################")

    def bill_area(self):
        self.textarea.configure(state="normal")
        var = True
        Already_exists = False
        self.welcome_bill()
        if not os.path.exists(self.file_save_adress):
            os.makedirs(self.file_save_adress)

        #if len(os.listdir(self.file_save_adress)) == 2 and self.c_search_bill.get() != '1000':
         #   messagebox.showwarning("Warning",
                           #        "All bills are deleted hence apllication are restart so please do not change a bill no")
          #  self.genrated_bill_no = self.bill_no()
           # self.c_search_bill.set(self.genrated_bill_no)
            #var = False
        elif self.c_name.get() == "Enter A Name" or self.c_phn.get() == "Enter A Ph.No" or len(self.c_phn.get())!=10:
            messagebox.showerror("Error", "Custumer Details Be Must")

            var = False


        elif self.All_price == 0.0:
            messagebox.showwarning("Warning", "No Anyone product are selected").capitalize()
            var = False

        elif self.c_search_bill.get() != str(self.genrated_bill_no):
            try:
                self.list[int(self.c_search_bill.get())]
            except:
                Already_exists = False
            else:
                Already_exists = True
            if Already_exists == True:
                var1 = messagebox.askyesnocancel("Alreday Exists Bill",
                                                 "if overite bill press yes else create new bill press no")
                if var1 == True:
                    var = True
                elif var1 == False:
                    var = False
                    self.genrated_bill_no = self.bill_no()
                    self.c_search_bill.set(self.genrated_bill_no)
                else:
                    var = False
                    self.clear()

            if Already_exists == False:
                messagebox.showwarning("Warning",
                                       "These bill no is a not valid new bill no is generated please do not change a bill number")
                self.genrated_bill_no = self.bill_no()
                self.c_search_bill.set(self.genrated_bill_no)
                var = False

        if var == True:

            if self.soap.get() != 0:
                self.textarea.insert(tk.END,
                                     f"\nBath Soap \t\t {self.soap.get()} \t {self.soap.get()} \t {self.soap.get() * self.soap1.get()}")
            if self.face_cream.get() != 0:
                self.textarea.insert(tk.END,
                                     f"\nFace Cream \t\t {self.face_cream1.get()} \t {self.face_cream.get()} \t {self.face_cream.get() * self.face_cream1.get()}")
            if self.hair_s.get() != 0:
                self.textarea.insert(tk.END,
                                     f"\nHair Spray \t\t {self.hair_s1.get()} \t {self.hair_s.get()} \t {self.hair_s.get() * self.hair_s1.get()}")
            if self.hair_g.get() != 0:
                self.textarea.insert(tk.END,
                                     f"\nHair Gel \t\t {self.hair_g1.get()} \t {self.hair_g.get()} \t {self.hair_g.get() * self.hair_g1.get()}")
            if self.lotion.get() != 0:
                self.textarea.insert(tk.END,
                                     f"\nBody Loion \t\t {self.lotion1.get()} \t {self.lotion.get()} \t {self.lotion.get() * self.lotion1.get()}")
            if self.face_wash.get():
                self.textarea.insert(tk.END,
                                     f"\nFace Wash \t\t {self.face_wash1.get()} \t {self.face_wash.get()} \t {self.face_wash.get() * self.face_wash1.get()}")

            if self.rice.get() != 0:
                self.textarea.insert(tk.END, f"\nRice \t\t {self.rice1.get()} \t {self.rice.get()} \t {self.rice.get() * self.rice1.get()}")
            if self.food_oil.get() != 0:
                self.textarea.insert(tk.END,
                                     f"\nFood oil \t\t {self.food_oil1.get()} \t {self.food_oil.get()} \t {self.food_oil.get() * self.food_oil1.get()}")
            if self.wheat.get() != 0:
                self.textarea.insert(tk.END,
                                     f"\nWheat \t\t {self.wheat1.get()} \t {self.wheat.get()} \t {self.wheat.get() * self.wheat1.get()}")
            if self.sugar.get() != 0:
                self.textarea.insert(tk.END,
                                     f"\nSugar \t\t {self.sugar1.get()} \t {self.sugar.get()} \t {self.sugar.get() * self.sugar1.get()}")
            if self.daal.get() != 0:
                self.textarea.insert(tk.END,
                                     f"\nDaal \t\t {self.daal_1.get()} \t {self.daal.get()} \t {self.daal.get() * self.daal_1.get()}")
            if self.tea.get():
                self.textarea.insert(tk.END, f"\nTea \t\t {self.tea1.get()} \t {self.tea.get()} \t {self.tea.get() * self.tea1.get()}")

            if self.maza.get() != 0:
                self.textarea.insert(tk.END, f"\nMaza \t\t {self.tea1.get()} \t {self.maza.get()} \t {self.maza.get() * self.maza1.get()}")
            if self.cock.get() != 0:
                self.textarea.insert(tk.END,
                                     f"\nCock \t\t {self.cock1.get()} \t {self.cock.get()} \t {self.cock.get() * self.cock1.get()}")
            if self.frooti.get() != 0:
                self.textarea.insert(tk.END,
                                     f"\nFrooti \t\t {self.frooti1.get()} \t {self.frooti.get()} \t {self.frooti.get() * self.frooti1.get()}")
            if self.thumsup.get() != 0:
                self.textarea.insert(tk.END,
                                     f"\nThumsup \t\t {self.thumsup1.get()} \t {self.thumsup.get()} \t {self.thumsup.get() * self.thumsup1.get()}")
            if self.limca.get() != 0:
                self.textarea.insert(tk.END,
                                     f"\nLimca \t\t {self.limca1.get()} \t {self.limca.get()} \t {self.limca.get() * self.limca1.get()}")
            if self.sprite.get() != 0:
                self.textarea.insert(tk.END,
                                     f"\nSprite \t\t {self.sprite1.get()} \t {self.sprite.get()} \t {self.sprite.get() * self.sprite1.get()}")
            self.textarea.insert(tk.END, "\n_________________________________________________")
            if self.total_cosmetic_price > 0:
                self.textarea.insert(tk.END, f"\nTotal Cosmetic Products Price :\t{self.total_cosmetic_price}")
            if self.total_grocesrry_price > 0:
                self.textarea.insert(tk.END, f"\nTotal Groserry Products Price :\t{self.total_grocesrry_price}")
            if self.total_cold_drink_price > 0:
                self.textarea.insert(tk.END, f"\nTotal Groserry Products Price :\t{self.total_cold_drink_price}")

            self.textarea.insert(tk.END, "\n_________________________________________________")

            self.textarea.insert(tk.END, f"\nTotal Price :{self.All_price}")
            self.textarea.insert(tk.END,
                                 f"\nTotal Price In Word :\t{self.inflect_object.number_to_words(self.All_price)}")

            self.save_bill()
            self.genrated_bill_no = self.bill_no()
    def bill_area1(self):

        self.textarea.configure(state="normal")
        self.textarea.delete(1.0,tk.END)

        self.textarea.insert(tk.END, "\n#############################################")
        self.textarea.insert(tk.END, "Product Name \t Price \t Quantity \t Total")
        self.textarea.insert(tk.END, "\n#############################################")



        if self.soap.get() != 0:
            self.textarea.insert(tk.END,
                                 f"\nBath Soap \t\t {self.soap1.get()} \t {self.soap.get()} \t {self.soap.get() * self.soap1.get()}")
        if self.face_cream.get() != 0:
            self.textarea.insert(tk.END,
                                 f"\nFace Cream \t\t {self.face_cream1.get()} \t {self.face_cream.get()} \t {self.face_cream.get() * self.face_cream1.get()}")
        if self.hair_s.get() != 0:
            self.textarea.insert(tk.END,
                                 f"\nHair Spray \t\t {self.hair_s1.get()} \t {self.hair_s.get()} \t {self.hair_s.get() * self.hair_s1.get()}")
        if self.hair_g.get() != 0:
            self.textarea.insert(tk.END,
                                 f"\nHair Gel \t\t {self.hair_g1.get()} \t {self.hair_g.get()} \t {self.hair_g.get() * self.hair_g1.get()}")
        if self.lotion.get() != 0:
            self.textarea.insert(tk.END,
                                 f"\nBody Loion \t\t {self.lotion1.get()} \t {self.lotion.get()} \t {self.lotion.get() * self.lotion1.get()}")
        if self.face_wash.get():
            self.textarea.insert(tk.END,
                                 f"\nFace Wash \t\t {self.face_wash1.get()} \t {self.face_wash.get()} \t {self.face_wash.get() * self.face_wash1.get()}")

        if self.rice.get() != 0:
            self.textarea.insert(tk.END, f"\nRice \t\t {self.rice1.get()} \t {self.rice.get()} \t {self.rice.get() * self.rice1.get()}")
        if self.food_oil.get() != 0:
            self.textarea.insert(tk.END,
                                 f"\nFood oil \t\t {self.food_oil1.get()} \t {self.food_oil.get()} \t {self.food_oil.get() * self.food_oil1.get()}")
        if self.wheat.get() != 0:
            self.textarea.insert(tk.END,
                                     f"\nWheat \t\t {self.wheat1.get()} \t {self.wheat.get()} \t {self.wheat.get() * self.wheat1.get()}")
        if self.sugar.get() != 0:
            self.textarea.insert(tk.END,
                                 f"\nSugar \t\t {self.sugar1.get()} \t {self.sugar.get()} \t {self.sugar.get() * self.sugar1.get()}")
        if self.daal.get() != 0:
            self.textarea.insert(tk.END,
                                 f"\nDaal \t\t {self.daal_1.get()} \t {self.daal.get()} \t {self.daal.get() * self.daal_1.get()}")
        if self.tea.get():
                self.textarea.insert(tk.END, f"\nTea \t\t {self.tea1.get()} \t {self.tea.get()} \t {self.tea.get() * self.tea1.get()}")

        if self.maza.get() != 0:
            self.textarea.insert(tk.END, f"\nMaza \t\t {self.tea1.get()} \t {self.maza.get()} \t {self.maza.get() * self.maza1.get()}")
        if self.cock.get() != 0:
            self.textarea.insert(tk.END,
                                 f"\nCock \t\t {self.cock1.get()} \t {self.cock.get()} \t {self.cock.get() * self.cock1.get()}")
        if self.frooti.get() != 0:
                self.textarea.insert(tk.END,
                                     f"\nFrooti \t\t {self.frooti1.get()} \t {self.frooti.get()} \t {self.frooti.get() * self.frooti1.get()}")
        if self.thumsup.get() != 0:
            self.textarea.insert(tk.END,
                                 f"\nThumsup \t\t {self.thumsup1.get()} \t {self.thumsup.get()} \t {self.thumsup.get() * self.thumsup1.get()}")
        if self.limca.get() != 0:
            self.textarea.insert(tk.END,
                                 f"\nLimca \t\t {self.limca1.get()} \t {self.limca.get()} \t {self.limca.get() * self.limca1.get()}")
        if self.sprite.get() != 0:
                self.textarea.insert(tk.END,
                                     f"\nSprite \t\t {self.sprite1.get()} \t {self.sprite.get()} \t {self.sprite.get() * self.sprite1.get()}")
        self.textarea.insert(tk.END, "\n_________________________________________________")
        if self.total_cosmetic_price > 0:
                self.textarea.insert(tk.END, f"\nTotal Cosmetic Products Price :\t{self.total_cosmetic_price}")
        if self.total_grocesrry_price > 0:
                self.textarea.insert(tk.END, f"\nTotal Groserry Products Price :\t{self.total_grocesrry_price}")
        if self.total_cold_drink_price > 0:
                self.textarea.insert(tk.END, f"\nTotal Groserry Products Price :\t{self.total_cold_drink_price}")

        self.textarea.insert(tk.END, "\n_________________________________________________")

        self.textarea.insert(tk.END, f"\nTotal Price:\tRs {self.All_price}")
        self.textarea.insert(tk.END, f"\nTotal Price In Word :\t{self.inflect_object.number_to_words(self.All_price)}")
        self.textarea.config(state='disable')






    def save_bill(self):

        mbs = messagebox.askyesno("Save Bill", "Do you want save the bill")
        date = time.strftime("%D").replace("/", "-")
        path = os.path.join(self.file_save_adress, date)
        if mbs == 1:
            if not os.path.exists(path):
                os.makedirs(path)
            if os.getcwd() != path:
                os.chdir(path)
            self.bill_data = self.textarea.get(1.0, tk.END)
            f1 = open(f"{self.c_search_bill.get()}.txt", "w")
            f1.write(self.bill_data)
            self.list[int(self.c_search_bill.get())] = os.path.join(os.getcwd(), f"{self.c_search_bill.get()}.txt")
            self.write_stock()


        else:
            return

    def find_bill(self):
        try:
            path = self.list[int(self.c_search_bill.get())]
        except:
            messagebox.showinfo("BILL", "Bill Not Found")
        else:
            f2 = open(path)
            self.textarea.delete(1.0, tk.END)
            self.textarea.insert(tk.END, f2.read())
            f2.close()

    def clear(self):
        intno = messagebox.askyesno("Reset", "Do you want reset")
        if intno == 1:
            # _______________________________________________________Variables resets
            # cosmetic Variables
            self.soap.set(0)
            self.face_cream.set(0)
            self.hair_s.set(0)
            self.hair_g.set(0)
            self.lotion.set(0)
            self.face_wash.set(0)

            # Grosery Variables
            self.rice.set(0)
            self.food_oil.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.daal.set(0)
            self.tea.set(0)

            # colddrink Variables
            self.maza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.thumsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)

            # Total product Price
            self.cosmetic_price.set("")
            self.grossery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grossery_tax.set("")
            self.cold_drink_tax.set("")
            # Custumor

            self.cphn_txt.delete(0,tk.END)
            self.cname_txt.delete(0,tk.END)
            self.cphn_txt.insert(0,"Enter A Name")
            self.cname_txt.insert(0,"Enter A Ph.No")
            self.c_bill_no.set("")
            self.c_search_bill.set("")
            self.cphn_txt.configure(state="disable")


            self.genrated_bill_no = self.bill_no()
            self.c_search_bill.set(self.genrated_bill_no)
            self.welcome_bill()
            self.cphn_txt.configure(state='disable')
            self.cname_txt.configure(state='disable')


    def bill_no(self):
        self.list = {}
        for i, j, l in os.walk(self.file_save_adress):
            for file in l:

                file_name = file.split(".")[0]
                try:
                    int(file_name)

                except:
                    pass
                else:
                    if len(file_name) == 4:
                        self.list[int(file_name)] = os.path.join(i, file)
        if len(self.list) == 0:
            return 1000
        else:
            return int(max(self.list)) + 1
    def reader(self):
        try:
            All_Data = self.object.Reader()
            for i in self.cosmetic:
                data = i.replace(" ", "_")
                list = All_Data[data].strip('[]', ).split(',')
                if i == self.cosmetic[0]:
                    self.soap1.set(list[0])
                    self.soap_max.set(list[1])
                if i == self.cosmetic[1]:
                    self.face_cream1.set(list[0])
                    self.face_cream_max.set(list[1])
                if i == self.cosmetic[2]:
                    self.hair_s1.set(list[0])
                    self.hair_s_max.set(list[1])
                if i == self.cosmetic[3]:
                    self.hair_g1.set(list[0])
                    self.hair_g_max.set(list[1])

                if i == self.cosmetic[4]:
                    self.lotion1.set(list[0])
                    self.lotion_max.set(list[1])
                if i == self.cosmetic[5]:
                    self.face_wash1.set(list[0])
                    self.face_wash_max.set(list[1])

            for i in self.grocerry:
                data = i.replace(" ", "_")
                list = All_Data[data].strip('[]', ).split(',')
                if i == self.grocerry[0]:
                    self.tea1.set(list[0])
                    self.tea_max.set(list[1])
                if i == self.grocerry[1]:
                    self.daal_1.set(list[0])
                    self.daal_max.set(list[1])
                if i == self.grocerry[2]:
                    self.rice1.set(list[0])
                    self.rice_max.set(list[1])
                if i == self.grocerry[3]:
                    self.food_oil1.set(list[0])
                    self.food_oil_max.set(list[1])

                if i == self.grocerry[4]:
                    self.sugar1.set(list[0])
                    self.sugar_max.set(list[1])
                if i == self.grocerry[5]:
                    self.wheat1.set(list[0])
                    self.wheat_max.set(list[1])

            for i in self.coldrink:
                data = i.replace(" ", "_")
                list = All_Data[data].strip('[]', ).split(',')
                if i == self.coldrink[0]:
                    self.thumsup1.set(list[0])
                    self.thumsup_max.set(list[1])
                if i == self.coldrink[1]:
                    self.limca1.set(list[0])
                    self.limca_max.set(list[1])
                if i == self.coldrink[2]:
                    self.frooti1.set(list[0])
                    self.frooti_max.set(list[1])
                if i == self.coldrink[3]:
                    self.cock1.set(list[0])
                    self.cock_max.set(list[1])

                if i == self.coldrink[4]:
                    self.sprite1.set(list[0])
                    self.sprite_max.set(list[1])
                if i == self.coldrink[5]:
                    self.maza1.set(list[0])
                    self.maza_max.set(list[1])

        except:
            var=messagebox.askyesno("Welcome","Your stock is emty if you add a new stock")
            if var ==True:
                self.after(1,self.new)




    def write_stock(self):


        if self.All_price !=0:
            self.object.write_stock_coldrinks(Thums_Up=[self.thumsup1.get(), self.thumsup_max.get()-self.thumsup.get()],
                                              Frooti=[self.frooti1.get(), self.frooti_max.get()-self.frooti.get()],
                                              Cock=[self.cock1.get(), self.cock_max.get()-self.cock.get()],
                                              Sprite=[self.sprite1.get(), self.sprite_max.get()-self.sprite.get()],
                                              Maza=[self.maza1.get(), self.maza_max.get()-self.maza.get()],
                                              Limca=[self.limca1.get(), self.limca_max.get()-self.limca.get()])
            self.object.write_stock_grocerry(Tea=[self.tea1.get(), self.tea_max.get()-self.tea.get()],
                                             Daal=[self.daal_1.get(),self.daal_max.get()-self.daal.get()],
                                             Rice=[self.rice1.get(),self.rice_max.get()-self.rice.get()],
                                             Food_Oil=[self.food_oil1.get(),self.food_oil_max.get()-self.food_oil.get()],
                                             Sugar=[self.sugar1.get(), self.sugar_max.get()-self.sugar.get()],
                                             Wheat=[self.wheat1.get(), self.wheat_max.get()-self.wheat.get()])

            self.object.write_stock_comsetic(Soap=[self.soap1.get(),(self.soap_max.get()-self.soap.get())],
                                             Face_Cream=[self.face_cream1.get(),self.face_cream_max.get()-self.face_cream.get()],
                                             Hair_Spray=[self.hair_s1.get(),self.hair_s_max.get()-self.hair_s.get()],
                                             Hair_Gel=[self.hair_g1.get(),self.hair_g_max.get()-self.hair_g.get()],
                                             Body_Lotion=[self.lotion1.get(),self.lotion_max.get()-self.lotion.get()],
                                             Face_Wash=[self.face_wash1.get(),self.face_wash_max.get()-self.face_wash.get()])

            self.object.sorce(self.c_search_bill.get())
            self.object.Writer()
            self.reader()














s = software()
s.mainloop()









