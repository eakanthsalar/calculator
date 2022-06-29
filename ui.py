from tkinter import *
from tkinter import messagebox

BG_COLOR = '#FFC4C4'


class Gui:
    def __init__(self):
        """
        class is used for all graphical user interface of Calculator.
        From all buttons ,entry of ui is defined here
        """
        # ---------UI Window------------
        self.final_content = ""
        # self.number_list = []
        self.window = Tk()
        self.window.config(width=500, height=500, pady=5, padx=5)
        self.window.title("Calculator")

        # ---------ANS and type print label----------

        self.text = Entry(width=15, font=('Arial', 24))
        self.text.focus()
        self.text.grid(row=0, columnspan=5, column=0)

        # -----------Number Buttons----------

        self.num_button1 = Button(padx=5, pady=5, bg=BG_COLOR, text="1", height=5, width=5, command=self.number_one)
        self.num_button1.grid(row=1, column=0)

        self.num_button2 = Button(padx=5, pady=5, bg=BG_COLOR, text="2", height=5, width=5, command=self.number_two)
        self.num_button2.grid(row=1, column=1)

        self.num_button3 = Button(padx=5, pady=5, bg=BG_COLOR, text="3", height=5, width=5, command=self.number_three)
        self.num_button3.grid(row=1, column=2)

        self.num_button4 = Button(padx=5, pady=5, bg=BG_COLOR, text="4", height=5, width=5, command=self.number_four)
        self.num_button4.grid(row=2, column=0)

        self.num_button5 = Button(padx=5, pady=5, bg=BG_COLOR, text="5", height=5, width=5, command=self.number_five)
        self.num_button5.grid(row=2, column=1)

        self.num_button6 = Button(padx=5, pady=5, bg=BG_COLOR, text="6", height=5, width=5, command=self.number_six)
        self.num_button6.grid(row=2, column=2)

        self.num_button7 = Button(padx=5, pady=5, bg=BG_COLOR, text="7", height=5, width=5, command=self.number_seven)
        self.num_button7.grid(row=3, column=0)

        self.num_button8 = Button(padx=5, pady=5, bg=BG_COLOR, text="8", height=5, width=5, command=self.number_eight)
        self.num_button8.grid(row=3, column=1)

        self.num_button9 = Button(padx=5, pady=5, bg=BG_COLOR, text="9", height=5, width=5, command=self.number_nine)
        self.num_button9.grid(row=3, column=2)

        self.num_button0 = Button(padx=5, pady=5, bg=BG_COLOR, text="0", height=5, width=5, command=self.number_zero)
        self.num_button0.grid(row=4, column=0)

        self.num_button_dot = Button(padx=5, pady=5, bg=BG_COLOR, text="•", height=5, width=5, command=self.number_dot)
        self.num_button_dot.grid(row=4, column=1)

        self.num_button_equal_to = Button(padx=5, pady=5, bg=BG_COLOR, text="=", height=5, width=5,
                                          command=self.equal_to)
        self.num_button_equal_to.grid(row=4, column=2)
        # ----------------Operators button-------------
        self.num_button_add = Button(padx=5, pady=5, bg=BG_COLOR, text="+", height=5, width=5, command=self.add)
        self.num_button_add.grid(row=1, column=3)

        self.num_button_sub = Button(padx=5, pady=5, bg=BG_COLOR, text="-", height=5, width=5, command=self.subtract)
        self.num_button_sub.grid(row=2, column=3)

        self.num_button_mul = Button(padx=5, pady=5, bg=BG_COLOR, text="×", height=5, width=5, command=self.multiply)
        self.num_button_mul.grid(row=3, column=3)

        self.num_button_div = Button(padx=5, pady=5, bg=BG_COLOR, text="÷", height=5, width=5, command=self.divide)
        self.num_button_div.grid(row=4, column=3)
        # ------------------clear button---------------
        self.num_button_AC = Button(padx=5, pady=5, bg=BG_COLOR, text="AC", height=11, width=5, command=self.clear)
        self.num_button_AC.grid(row=1, column=4, rowspan=2)

        # ---------clear term by term------------
        photo = PhotoImage(file="images/false.png")
        self.num_button_x = Button(borderwidth=0, image=photo, width=50, height=185, bg=BG_COLOR,
                                   command=self.clear_single)
        self.num_button_x.grid(row=3, column=4, rowspan=2)

        self.window.mainloop()

    # all the text inputs in UI are printed in entry as a text
    def number_one(self):
        self.text.insert(END, "1")

    def number_two(self):
        self.text.insert(END, "2")

    def number_three(self):
        self.text.insert(END, "3")

    def number_four(self):
        self.text.insert(END, "4")

    def number_five(self):
        self.text.insert(END, "5")

    def number_six(self):
        self.text.insert(END, "6")

    def number_seven(self):
        self.text.insert(END, "7")

    def number_eight(self):
        self.text.insert(END, "8")

    def number_nine(self):
        self.text.insert(END, "9")

    def number_zero(self):
        self.text.insert(END, "0")

    def number_dot(self):
        self.text.insert(END, ".")

    def add(self):
        self.text.insert(END, "+")

    def subtract(self):
        self.text.insert(END, "-")

    # inputs are checked for wrong format of operators each time and if is in right format,include the text
    def multiply(self):
        self.text.insert(END, "*")
        self.check_input()

    def divide(self):
        self.text.insert(END, "/")
        self.check_input()

    def clear(self):
        """Clears all text in entry"""
        self.text.delete(0, END)

    def clear_single(self):
        """
        clears input text as one at a time from end of the text
        """
        contents = self.text.get()
        contents = contents[:-1]
        self.text.delete(0, END)
        self.text.insert(0, contents)

    def equal_to(self):
        """
        At the end of inputs all text in entry is stored and cleared
        text is processed for mathematical operations
        """
        # self.text.insert(END,"=")
        self.final_content = str(self.text.get())
        if len(self.final_content) == 0:
            pass
        else:
            while self.final_content[len(self.final_content) - 1] in ["+", "-", "*",
                                                                      "/"]:  # if any operators present at the end of input text,delete that operator and process the data
                self.text.delete(len(self.final_content) - 1)
                self.final_content = self.text.get()

        self.text.delete(0, END)

        self.final_answer()

    def check_input(self):
        """
        checks for any wrong format of input everytime operator is triggered since there are limitations for order of operators in an Arithmetic expression
        """
        current_input = str(self.text.get())
        if len(current_input) == 0:
            pass
        elif len(
                current_input) == 1:  # if there is only one input and if it is a * or / symbol than it is not acceptable so delete symbol
            if current_input in ["*", "/"]:
                self.text.delete(0, END)
        elif current_input[len(current_input) - 2] in ["-", "+"] and current_input[len(current_input) - 1] in ["*",
                                                                                                               "/"]:  # if in between expressions has + or - sign followed by * or / operators is unacceptable
            self.text.delete(len(current_input) - 1)
        else:
            if current_input[len(current_input) - 1] in ["*", "/"] and current_input[len(current_input) - 2] in ["*",
                                                                                                                 "/"]:  # if in between expressions of recently typed has both symbols * and / is or ** or // is unacceptable
                self.text.delete(len(current_input) - 2)

    def final_answer(self):
        """
        final contents of entry text is obtained and string is converted into python expression and executed
        final answer is updated to entry as a string
        """
        try:
            expression = self.final_content
            ans = eval(expression)
        except ZeroDivisionError:  # if there is divide by zero error then show messagebox and delete all input
            messagebox.showinfo(title="zero division error", message="cannot divide by zero")
            self.text.delete(0, END)

        except SyntaxError:
            messagebox.showinfo(title="no input", message="please give some valid input")

        else:
            ans = str(ans)
            self.text.insert(0, ans)
            #  hii
