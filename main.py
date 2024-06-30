import os
import tkinter as tk
from tkinter import messagebox , simpledialog
from playsound import playsound
from sympy import simplify, Rational, I, symbols, solve, sympify, sqrt
import numpy as np
import matplotlib.pyplot as plt
import sys



sound_enabled = True
state = 0
script_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
close_path = os.path.join(script_dir,'sound/close.wav')
ciallo_path = os.path.join(script_dir, 'sound/ciallo.wav')
open_path = os.path.join(script_dir, 'sound/open.wav')
bg_path = os.path.join(script_dir, 'image/bg_1.png')


def ciallo():
    if sound_enabled == True:
        playsound(ciallo_path)




def save_sound_state():
    global sound_enabled
    with open('sound_settings.txt', 'w') as f:
        if sound_enabled == True:
            state = 0
        else:
            state = 1
        f.write(str(state))



def load_sound_state():
    global sound_enabled
    try:
        with open('sound_settings.txt', 'r') as f:
            for line in  f:
                if line == '0':
                    sound_enabled = True
                elif line == '1':
                    sound_enabled = False
                else:
                    sound_enabled = True
    except FileNotFoundError:
        sound_enabled = True



def close():
    root.destroy()
    if sound_enabled == True:
        playsound(close_path)







load_sound_state()


class ComplexCalculatorApp:
    def __init__(self, master):


        self.master = master
        master.title('更好的计算器 v_2.00')
        self.show_warning()


        self.label = tk.Label(master, text='请选择要使用的功能：')
        self.label.pack()

        self.simplify_nested_sqrt_button = tk.Button(master, text='化简嵌套根式', bg='black', fg='pink', activebackground='light blue', command=self.simplify_nested_sqrt)
        self.simplify_nested_sqrt_button.pack()

        self.sqrt_complex_button = tk.Button(master, text='计算虚数的平方根', bg='black', fg='pink', activebackground='light blue', command=self.sqrt_complex_number)
        self.sqrt_complex_button.pack()



        self.solve_linear_equation_button = tk.Button(master, text='解一元一次方程（虚数系数）', bg='black', fg='pink', activebackground='light blue', command=self.solve_complex_linear_equation)
        self.solve_linear_equation_button.pack()

        self.solve_quadratic_equation_button = tk.Button(master, text='解二元一次方程（虚数系数）', bg='black', fg='pink', activebackground='light blue', command=self.solve_complex_quadratic_equation)
        self.solve_quadratic_equation_button.pack()

        self.solve_quadratic_equation_button = tk.Button(master, text='绘制二元一次函数图像', bg='black', fg='pink', activebackground='light blue',command=self.plot_quadratic_function)
        self.solve_quadratic_equation_button.pack()

        self.solve_quadratic_equation_button = tk.Button(master, text='绘制正弦函数图像', bg='black', fg='pink', activebackground='light blue',command=self.plot_custom_sine_function)
        self.solve_quadratic_equation_button.pack()

        self.solve_quadratic_equation_button = tk.Button(master, text='绘制余弦函数图像', bg='black', fg='pink', activebackground='light blue', command=self.plot_custom_cosine_function)
        self.solve_quadratic_equation_button.pack()



        self.solve_quadratic_equation_button = tk.Button(master, text='关于', bg='black', fg='pink', activebackground='light blue', command=self.about)
        self.solve_quadratic_equation_button.pack()


        self.sound_button = tk.Button(master, text='静音', bg='black', fg='pink', activebackground='light blue', command=self.toggle_sound)
        self.sound_button.pack()




    def simplify_nested_sqrt(self):
        ciallo()
        a = Rational(tk.simpledialog.askstring('输入', '请输入a (sqrt(a +/- sqrt(b))):'))
        b = Rational(tk.simpledialog.askstring('输入', '请输入b (sqrt(a +/- sqrt(b))):'))
        c = Rational(tk.simpledialog.askstring('输入', "请输入运算符 ('+'为1,'-'为2):"))
        if a is None or b is None or c is None:
            return
        if c == 1:
            messagebox.showinfo('化简结果', str(sqrt((a+sqrt(a ** 2 - b)) / 2) + sqrt((a-sqrt(a ** 2 - b)) / 2)))
        elif c == 2:
            messagebox.showinfo('化简结果', str(sqrt((a+sqrt(a ** 2 - b)) / 2) - sqrt((a-sqrt(a ** 2 - b)) / 2)))
        else:
            messagebox.showerror("错误", "只能输入1('+')或2('-')。")


    def sqrt_complex_number(self):
        ciallo()
        real_part = tk.simpledialog.askfloat("输入", "请输入虚数的实部：")
        if real_part is None:
            return
        imag_part = tk.simpledialog.askfloat("输入", "请输入虚数的虚部：")
        if imag_part is None:
            return
        complex_number = complex(real_part, imag_part)
        result = complex_number ** 0.5
        messagebox.showinfo("结果", str(result))


    def simplify_complex_fraction(self):
        ciallo()
        real_numerator = Rational(tk.simpledialog.askstring("输入", "请输入分数的分子的实部："))
        if real_numerator is None:
            return
        imag_numerator = Rational(tk.simpledialog.askstring("输入", "请输入分数的分子的虚部："))
        if imag_numerator is None:
            return
        real_denominator = Rational(tk.simpledialog.askstring("输入", "请输入分数的分母的实部："))
        if real_denominator is None:
            return
        imag_denominator = Rational(tk.simpledialog.askstring("输入", "请输入分数的分母的虚部："))
        if imag_denominator is None:
            return
        numerator = real_numerator + imag_numerator * I
        denominator = real_denominator + imag_denominator * I
        fraction = numerator / denominator
        simplified_fraction = simplify(fraction)
        messagebox.showinfo("结果", str(simplified_fraction))

    def solve_complex_linear_equation(self):
        ciallo()
        x = symbols('x')
        real_coefficient_str = tk.simpledialog.askstring("输入", "请输入系数的实部：")
        if real_coefficient_str is None:
            return
        imag_coefficient_str = tk.simpledialog.askstring("输入", "请输入系数的虚部：")
        if imag_coefficient_str is None:
            return
        constant_str = tk.simpledialog.askstring("输入", "请输入常数项：")
        if constant_str is None:
            return
        real_coefficient = Rational(sympify(real_coefficient_str).evalf())
        imag_coefficient = Rational(sympify(imag_coefficient_str).evalf())
        constant = Rational(sympify(constant_str).evalf())
        equation = real_coefficient * x + imag_coefficient * I * x - constant
        solutions = solve(equation, x)
        messagebox.showinfo("结果", "\n".join(str(solution) for solution in solutions))

    def solve_complex_quadratic_equation(self):
        ciallo()
        x = symbols('x')
        real_coefficient_2 = tk.simpledialog.askfloat("输入", "请输入二次项系数的实部：")
        if real_coefficient_2 is None:
            return
        imag_coefficient_2_str = tk.simpledialog.askstring("输入", "请输入二次项系数的虚部：")
        if imag_coefficient_2_str is None:
            return
        imag_coefficient_2 = sympify(imag_coefficient_2_str).evalf()
        real_coefficient_1 = tk.simpledialog.askfloat("输入", "请输入一次项系数的实部：")
        if real_coefficient_1 is None:
            return
        imag_coefficient_1_str = tk.simpledialog.askstring("输入", "请输入一次项系数的虚部：")
        if imag_coefficient_1_str is None:
            return
        imag_coefficient_1 = sympify(imag_coefficient_1_str).evalf()
        constant = tk.simpledialog.askfloat("输入", "请输入常数项的实部：")
        if constant is None:
            return
        imag_constant_str = tk.simpledialog.askstring("输入", "请输入常数项的虚部：")
        if imag_constant_str is None:
            return
        imag_constant = sympify(imag_constant_str).evalf()
        if real_coefficient_2 == 0 and imag_coefficient_2 == 0:
            messagebox.showerror("错误", "二次项系数不能同时为零。")
            return
        equation = (real_coefficient_2 + imag_coefficient_2 * I) * x**2 + \
                   (real_coefficient_1 + imag_coefficient_1 * I) * x + \
                   (constant + imag_constant * I)
        solutions = solve(equation, x)
        messagebox.showinfo("结果", "\n".join(str(solution) for solution in solutions))





    def plot_quadratic_function(self):
        ciallo()
        a = Rational(tk.simpledialog.askstring('输入', '请输入a:'))
        b = Rational(tk.simpledialog.askstring('输入', '请输入b:'))
        c = Rational(tk.simpledialog.askstring('输入', '请输入c:'))
        if a is None or b is None or c is None:
            return
        if a == 0:
            messagebox.showerror('a不为0')
        derta = (b * -1) / (2 * a)
        x = np.linspace(derta - 10, derta + 10, 400)  # 从 -10 到 10 生成 400 个点
        y = a * x**2 + b * x + c
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label=f'$f(x) = {a}x^2 + {b}x + {c}$')
        plt.title('二次函数图像')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.legend()
        plt.show()


    def plot_custom_sine_function(self):
        ciallo()
        amplitude = Rational(tk.simpledialog.askstring('输入', '请输入振幅A:'))
        frequency = Rational(tk.simpledialog.askstring('输入', '请输入频率f:'))
        phase = Rational(tk.simpledialog.askstring('输入', '请输入初始相位（请填pi的系数）:'))
        if amplitude is None or frequency is None or phase is None:
            return

        try:
            amplitude = float(amplitude)
            frequency = float(frequency)
            phase_coefficient = float(phase)
        except ValueError:
            messagebox.showerror('错误', '请输入有效的数值！')
            return

        if amplitude == 0:
            messagebox.showerror('振幅不能为0')

        if frequency == 0:
            messagebox.showerror('频率不能为0')


        phase = phase_coefficient * np.pi
        x = np.linspace(-2 * np.pi, 2 * np.pi, 400)  # 从 -2π 到 2π 生成 400 个点
        y = amplitude * np.sin(frequency * x + phase)
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label=f'$y = {amplitude} \sin({frequency}x + {phase})$', color='blue')
        plt.title('定制的正弦函数图像')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.legend()
        plt.show()



    def plot_custom_cosine_function(self):
        ciallo()
        # 获取用户输入
        amplitude_str = tk.simpledialog.askstring('输入', '请输入振幅A:')
        frequency_str = tk.simpledialog.askstring('输入', '请输入频率f:')
        phase_str = tk.simpledialog.askstring('输入', '请输入初始相位（请填pi的系数）:')

        try:
            amplitude = float(amplitude_str)
            frequency = float(frequency_str)
            phase_coefficient = float(phase_str)
        except ValueError:
            messagebox.showerror('错误', '请输入有效的数值！')
            return

        phase = phase_coefficient * np.pi

        if amplitude == 0:
            messagebox.showerror('错误', '振幅不能为0')
            return

        if frequency == 0:
            messagebox.showerror('错误', '频率不能为0')
            return

        x = np.linspace(-2 * np.pi, 2 * np.pi, 400)  # 从 -2π 到 2π 生成 400 个点
        y = amplitude * np.cos(frequency * x + phase)
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label=f'$y = {amplitude} \cos({frequency}x + {phase})$', color='blue')
        plt.title('定制的余弦函数图像')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.legend()
        plt.show()



    def toggle_sound(self):
        global sound_enabled
        sound_enabled = not sound_enabled
        save_sound_state()


    def show_warning(self):
        result = messagebox.showwarning("警告", "本应用为课题作业,仅供学习参考,请勿用于商业用途!")
        if result == 'ok' and sound_enabled == True:
            playsound(open_path)


    def about(self):
        messagebox.showinfo('关于', '作者:wzl;github:')







root = tk.Tk()
root.geometry("354x302+480+270")
image = tk.PhotoImage(file=bg_path)
label = tk.Label(root, image=image)
label.place(x=0, y=0, relwidth=1, relheight=1)
frame = tk.Frame(root, bd=2, relief=tk.SUNKEN)
app = ComplexCalculatorApp(root)
root.protocol("WM_DELETE_WINDOW", close)
root.mainloop()

