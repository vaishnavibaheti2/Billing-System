from tkinter import *
import math
import os
import random
from tkinter import messagebox


class BillApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#004d4d"
        title = Label(self.root, text="Billing Software", bd=12, relief=GROOVE, bg=bg_color,
                      fg="gold", font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        # ===================== Variables==========================
        # ====================== Cosmetic variable==========================

        self.lipstick = IntVar()
        self.mascare = IntVar()
        self.bath_soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.body_lotion = IntVar()

        # =============== Grocery variables==================

        self.rice = IntVar()
        self.wheat = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.tea = IntVar()
        self.sugar = IntVar()

        # =============== cold drinks variables===============

        self.spirit = IntVar()
        self.pepsi = IntVar()
        self.limca = IntVar()
        self.fanta = IntVar()
        self.coca_cola = IntVar()
        self.thumbsup = IntVar()

        # ================== Total product price and Tax vaibales===============

        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        # ================= Customer variable===========================

        self.c_name = StringVar()
        self.c_phon = StringVar()

        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))

        self.search_bill = StringVar()

        # ======== Customer Details Frame================

        F1 = LabelFrame(self.root, bd=7, relief=GROOVE, text="Customer Details", font=(
            "times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name", font=(
            "times new roman", 18, "bold"), fg="White", bg=bg_color).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Phone No.", font=(
            "times new roman", 18, "bold"), fg="White", bg=bg_color).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phon, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number", font=(
            "times new roman", 18, "bold"), fg="White", bg=bg_color).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=5, pady=5, padx=10)
        bill_btn = Button(F1, command=self.find_bill, text="Search", width=10, bd=7, font="arial 12 bold").grid(
            row=0, column=6, padx=10, pady=10)

        # ==================== Cosmetic Frame========================

        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics", font=(
            "times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F2.place(x=5, y=180, width=325, height=380)

        lip_lable = Label(F2, text="Lipstick", font=(
            "times new roman", 16, " bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        lip_txt = Entry(F2, width=10, textvariable=self.lipstick, font=("times new roman", 16, "bold"),
                        bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        mas_lable = Label(F2, text="Mascara", font=(
            "times new roman", 16, " bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        mas_txt = Entry(F2, width=10, textvariable=self.mascare, font=("times new roman", 16, "bold"),
                        bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        bath_lable = Label(F2, text="Bath Soap", font=(
            "times new roman", 16, " bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        bath_txt = Entry(F2, width=10, textvariable=self.bath_soap, font=("times new roman", 16, "bold"),
                         bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        face_cream_lable = Label(F2, text="Face Cream", font=(
            "times new roman", 16, " bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        face_cream_txt = Entry(F2, width=10, textvariable=self.face_cream, font=("times new roman", 16, "bold"),
                               bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        face_wash_lable = Label(F2, text="Face Wash", font=(
            "times new roman", 16, " bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        face_wash_txt = Entry(F2, width=10, textvariable=self.face_wash, font=("times new roman", 16, "bold"),
                              bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        body_lotion_lable = Label(F2, text="Body Lotion", font=(
            "times new roman", 16, " bold"), bg=bg_color, fg="lightgreen").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        body_lotion_txt = Entry(F2, width=10, textvariable=self.body_lotion, font=("times new roman", 16, "bold"),
                                bd=5, relief=SUNKEN).grid(row=6, column=1, padx=10, pady=10)

        # ==================== Grocery Frame========================

        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocery", font=(
            "times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F3.place(x=335, y=180, width=325, height=380)

        g1_lable = Label(F3, text="Rice", font=(
            "times new roman", 16, " bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        g1_txt = Entry(F3, width=10, textvariable=self.rice, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        g2_lable = Label(F3, text="Wheat", font=(
            "times new roman", 16, " bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F3, width=10, textvariable=self.wheat, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        g3_lable = Label(F3, text="Food Oil", font=(
            "times new roman", 16, " bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        g3_txt = Entry(F3, width=10, textvariable=self.food_oil, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        g4_lable = Label(F3, text="Daal", font=(
            "times new roman", 16, " bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        g4_txt = Entry(F3, width=10, textvariable=self.daal, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        g5_lable = Label(F3, text="Tea", font=(
            "times new roman", 16, " bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        g5_txt = Entry(F3, width=10, textvariable=self.tea, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        g6_lable = Label(F3, text="Sugar", font=(
            "times new roman", 16, " bold"), bg=bg_color, fg="lightgreen").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        g6_txt = Entry(F3, width=10, textvariable=self.sugar, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=6, column=1, padx=10, pady=10)

        # ==================== Cold Drinks Frame========================

        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cold Drinks", font=(
            "times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F4.place(x=665, y=180, width=325, height=380)

        cd_lable = Label(F4, text="Spirit", font=(
            "times new roman", 16, " bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        cd_txt = Entry(F4, width=10, textvariable=self.spirit, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        cd2_lable = Label(F4, text="Pepsi", font=(
            "times new roman", 16, " bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        cd2_txt = Entry(F4, width=10, textvariable=self.pepsi, font=("times new roman", 16, "bold"),
                        bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        cd3_lable = Label(F4, text="Fanta", font=(
            "times new roman", 16, " bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        cd3_txt = Entry(F4, width=10, textvariable=self.fanta, font=("times new roman", 16, "bold"),
                        bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        cd4_lable = Label(F4, text="Limca", font=(
            "times new roman", 16, " bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        cd4_txt = Entry(F4, width=10, textvariable=self.limca, font=("times new roman", 16, "bold"),
                        bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        cd5_lable = Label(F4, text="Thumps Up", font=(
            "times new roman", 16, " bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        cd5_txt = Entry(F4, width=10, textvariable=self.thumbsup, font=("times new roman", 16, "bold"),
                        bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        cd6_lable = Label(F4, text="Coca Cola", font=(
            "times new roman", 16, " bold"), bg=bg_color, fg="lightgreen").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        cd6_txt = Entry(F4, width=10, textvariable=self.coca_cola, font=("times new roman", 16, "bold"),
                        bd=5, relief=SUNKEN).grid(row=6, column=1, padx=10, pady=10)

        # =================== Bill Area======================

        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=995, y=180, width=360, height=380)

        bill_title = Label(
            F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # =============== Button Frame========================

        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=(
            "times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl = Label(F6, text="Total Cosmetic Price", bg=bg_color, fg="white", font=(
            "times new roman", 14, "bold")).grid(row=0, column=0, padx=20, pady=1, sticky="w")
        m1_txt = Entry(F6, width=18, textvariable=self.cosmetic_price, font="arial 10 bold", bd=7,
                       relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)

        m2_lbl = Label(F6, text="Total Grocery Price", bg=bg_color, fg="white", font=(
            "times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price, font="arial 10 bold", bd=7,
                       relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text="Total Cold Drinks Price", bg=bg_color, fg="white", font=(
            "times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(F6, width=18, textvariable=self.cold_drink_price, font="arial 10 bold", bd=7,
                       relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        c1_lbl = Label(F6, text="Cosmetic Tax", bg=bg_color, fg="white", font=(
            "times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        c1_txt = Entry(F6, width=18, textvariable=self.cosmetic_tax, font="arial 10 bold", bd=7,
                       relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        c2_lbl = Label(F6, text="Grocery Tax", bg=bg_color, fg="white", font=(
            "times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        c2_txt = Entry(F6, width=18, textvariable=self.grocery_tax, font="arial 10 bold", bd=7,
                       relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        c3_lbl = Label(F6, text="Cold Drinks Tax", bg=bg_color, fg="white", font=(
            "times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        c3_txt = Entry(F6, width=18, textvariable=self.cold_drink_tax, font="arial 10 bold", bd=7,
                       relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=750, width=585, height=105)

        total_btn = Button(btn_f, command=self.total, text="Total", bg="#008080", fg="white", bd=3,
                           pady=15, width=10, font="arial 15 bold").grid(row=0, column=0, pady=5, padx=5)

        gbill_btn = Button(btn_f, text="Generate Bill", command=self.bill_area, bg="#008080", fg="white", bd=3,
                           pady=15, width=10, font="arial 15 bold").grid(row=0, column=1, pady=5, padx=5)

        clear_btn = Button(btn_f, text="Clear", command=self.clear_data, bg="#008080", fg="white", bd=3,
                           pady=15, width=10, font="arial 15 bold").grid(row=0, column=2, pady=5, padx=5)

        exit_btn = Button(btn_f, text="Exit", command=self.exit_app, bg="#008080", fg="white", bd=3,
                          pady=15, width=10, font="arial 15 bold").grid(row=0, column=3, pady=5, padx=5)

        self.welcome_bill()

    def total(self):
        self.c_l_p = self.lipstick.get() * 100
        self.c_m_p = self.mascare.get() * 50
        self.c_b_p = self.bath_soap.get() * 25
        self.c_fc_p = self.face_cream.get() * 50
        self.c_fw_p = self.face_wash.get() * 60
        self.c_bl_p = self.body_lotion.get() * 80

        self.total_cosmetic_price = float(
            self.c_l_p +
            self.c_m_p +
            self.c_b_p +
            self.c_fc_p +
            self.c_fw_p +
            self.c_bl_p
        )

        self.cosmetic_price.set("Rs. " + str(self.total_cosmetic_price))
        self.c_tax = round((self.total_cosmetic_price * 0.05), 2)
        self.cosmetic_tax.set(
            "Rs. " + str(self.c_tax))

        self.g_r_p = self.rice.get() * 50
        self.g_w_p = self.wheat.get() * 30
        self.g_d_p = self.daal.get() * 50
        self.g_fo_p = self.food_oil.get() * 80
        self.g_t_p = self.tea.get() * 30
        self.g_s_p = self.sugar.get() * 38

        self.total_grocery_price = float(
            self.g_r_p +
            self.g_w_p +
            self.g_d_p +
            self.g_fo_p +
            self.g_t_p +
            self.g_s_p
        )

        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price * 0.03), 2)
        self.grocery_tax.set(
            "Rs. " + str(self.g_tax))

        self.cd_s_p = self.spirit.get() * 30
        self.cd_p_p = self.pepsi.get() * 30
        self.cd_l_p = self.limca.get() * 30
        self.cd_f_p = self.fanta.get() * 30
        self.cd_tp_p = self.coca_cola.get() * 30
        self.cd_cc_p = self.thumbsup.get() * 30

        self.total_cold_drink_price = float(
            self.cd_s_p +
            self.cd_p_p +
            self.cd_l_p +
            self.cd_f_p +
            self.cd_tp_p +
            self.cd_cc_p
        )

        self.cold_drink_price.set("Rs. " + str(self.total_cold_drink_price))
        self.cd_tax = round((self.total_cold_drink_price*0.05), 2)
        self.cold_drink_tax.set(
            "Rs. " + str(self.cd_tax))

        self.Total_bill = float(self.total_cosmetic_price +
                                self.total_grocery_price +
                                self.total_cold_drink_price +
                                self.c_tax +
                                self.g_tax +
                                self.cd_tax
                                )

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome To Baheti Provision\n")
        self.txtarea.insert(END, f"\n Bill Number   : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number  : {self.c_phon.get()}")
        self.txtarea.insert(END, f"\n ======================================")
        self.txtarea.insert(END, f"\n Products\t\tQTY\t\tPrice")
        self.txtarea.insert(END, f"\n ======================================")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phon.get == "":
            messagebox.showerror("Error", "Customer Details are required")
        elif self.cosmetic_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_drink_price.get() == "Rs. 0.0":
            messagebox.showerror("Error", "No product purchased")
        else:
            self.welcome_bill()
            # =========cosmetics===============
            if self.lipstick.get() != 0:
                self.txtarea.insert(
                    END, f"\n Lipstick\t\t{self.lipstick.get()}\t\t{self.c_l_p}")
            if self.face_cream.get() != 0:
                self.txtarea.insert(
                    END, f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.mascare.get() != 0:
                self.txtarea.insert(
                    END, f"\n Mascara\t\t{self.mascare.get()}\t\t{self.c_m_p}")
            if self.bath_soap.get() != 0:
                self.txtarea.insert(
                    END, f"\n Bath Soap\t\t{self.bath_soap.get()}\t\t{self.c_b_p}")
            if self.face_wash.get() != 0:
                self.txtarea.insert(
                    END, f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.body_lotion.get() != 0:
                self.txtarea.insert(
                    END, f"\n Body Lotion\t\t{self.body_lotion.get()}\t\t{self.c_bl_p}")

            # =================Grocery==================
            if self.rice.get() != 0:
                self.txtarea.insert(
                    END, f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.wheat.get() != 0:
                self.txtarea.insert(
                    END, f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.food_oil.get() != 0:
                self.txtarea.insert(
                    END, f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_fo_p}")
            if self.daal.get() != 0:
                self.txtarea.insert(
                    END, f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")
            if self.sugar.get() != 0:
                self.txtarea.insert(
                    END, f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.tea.get() != 0:
                self.txtarea.insert(
                    END, f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")

            # ========================Cold Drinks====================
            if self.spirit.get() != 0:
                self.txtarea.insert(
                    END, f"\n Spirit\t\t{self.spirit.get()}\t\t{self.cd_s_p}")
            if self.pepsi.get() != 0:
                self.txtarea.insert(
                    END, f"\n Pepsi\t\t{self.pepsi.get()}\t\t{self.cd_p_p}")
            if self.limca.get() != 0:
                self.txtarea.insert(
                    END, f"\n Limca\t\t{self.limca.get()}\t\t{self.cd_l_p}")
            if self.fanta.get() != 0:
                self.txtarea.insert(
                    END, f"\n Fanta\t\t{self.fanta.get()}\t\t{self.cd_f_p}")
            if self.thumbsup.get() != 0:
                self.txtarea.insert(
                    END, f"\n Thumps Up\t\t{self.thumbsup.get()}\t\t{self.cd_tp_p}")
            if self.coca_cola.get() != 0:
                self.txtarea.insert(
                    END, f"\n Coca Cola\t\t{self.coca_cola.get()}\t\t{self.cd_cc_p}")

            self.txtarea.insert(
                END, f"\n --------------------------------------")
            if self.cosmetic_tax.get() != "Rs. 0.0":
                self.txtarea.insert(
                    END, f"\n Cosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get() != "Rs. 0.0":
                self.txtarea.insert(
                    END, f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get() != "Rs. 0.0":
                self.txtarea.insert(
                    END, f"\n Cold Drink Tax\t\t\t{self.cold_drink_tax.get()}")

            self.txtarea.insert(
                END, f"\n --------------------------------------")
            self.txtarea.insert(
                END, f"\n Total Bill :\t\t\t Rs. {self.Total_bill}")
            self.save_bill()

           # self.txtarea.insert(END, f"\n --------------------------------------")
    # =============== Saved bill=========================
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the Bill")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo(
                "Saved :", f"Bill No. : {self.bill_no.get()} Saved Successfully")
        else:
            return
    # ================ Find Bill================================

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "yes"
            if present == "no":
                messagebox.showerror("Error :", "Invalid Bill No.")

    # ================= clear Data====================================
    def clear_data(self):
        op = messagebox.askyesno("Clear Data :", "Do you want to clear data?")
        if op > 0:
            # ====================== Cosmetice==========================
            self.lipstick.set(0)
            self.mascare.set(0)
            self.bath_soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.body_lotion.set(0)
            # =============== Grocery==================
            self.rice.set(0)
            self.wheat.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.tea.set(0)
            self.sugar.set(0)
            # =============== cold drinks ===============
            self.spirit.set(0)
            self.pepsi.set(0)
            self.limca.set(0)
            self.fanta.set(0)
            self.coca_cola.set(0)
            self.thumbsup.set(0)
            # ================== Total product price and Tax ===============
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")
            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")
            # ================= Customer ===========================
            self.c_name.set("")
            self.c_phon.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()
    # ===================== Exit App====================

    def exit_app(self):
        op = messagebox.askyesno("Exit :", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()


root = Tk()
obj = BillApp(root)
root.mainloop()
