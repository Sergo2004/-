from tkinter import *
from random import randint

root = Tk()

root.title('Игра "Угадай число"')
root.resizable(False, False)
root.geometry('500x300')

welcome = Label(text='Добро пожаловать в игру !\n', font='50')
welcome.pack()

enter_num = Label(text='Загадано число от 1 до 100, отгадайте и введите его ниже:\n', font='20')
enter_num.pack()


def getNumEnter():
    num = numEnter_field.get()
    if num.isdigit() and 0 < int(num) < 100:
        return int(num)
    else:
        result.config(text='Введено недопустимое значение, нужно целое число от 1 до 100!')


numEnter_field = Entry(root, font='50', justify=CENTER)
numEnter_field.pack()

result = Label(root, font='50', justify=CENTER, fg='red')
result.pack()

def game():
    global try_count

    num = getNumEnter()
    if num is None:
        return

    if num < rand_num and try_count<10:
        result.config(text='Загаданное число больше')
        numEnter_field.delete(0, END)
        try_count += 1
    elif num > rand_num and try_count<10:
        result.config(text='Загаданное число меньше')
        numEnter_field.delete(0, END)
        try_count += 1
    elif num == rand_num and try_count<10:
        result.config(text=f'Вы угадали! Количество ваших попыток: {try_count}')
    if try_count == 10:
        result.config(text=f'Вы проиграли! Количество ваших попыток: {try_count}')


btnRead = Button(root, height=1, width=10, text="Угадать", command=game)
btnRead.pack()

try_count = 1
rand_num = randint(1, 100)

root.mainloop()


