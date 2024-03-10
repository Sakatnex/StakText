from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import webbrowser

def redirect(url):
    webbrowser.open(url)

def change_theme(theme):
    text_field['bg'] = view_colors[theme]['text_bg']
    text_field['fg'] = view_colors[theme]['text_fg']
    text_field['insertbackground'] = view_colors[theme]['cursor']
    text_field['selectbackground'] = view_colors[theme]['select_bg']

def change_font(font):
    text_field['font'] = fonts[font]['font']

def notepad_exit():
    answer = messagebox.askokcancel('Выйти?', 'Вы действительно хотите выйти?')
    if answer:
        root.destroy()

def open_file():
    file_path = filedialog.askopenfilename(title='Выбор файла', filetypes=(('Текстовики (*.txt)', '*.txt'), ('Все файлы', '*.*')))
    if file_path:
        text_field.delete('1.0', END)
        text_field.insert('1.0', open(file_path,'r', encoding='utf-8').read())

def save_file():
    file_path = filedialog.asksaveasfilename(title='Выбор файла', filetypes=(('Текстовики (*.txt)', '*.txt'), ('Все файлы', '*.*')))
    f = open(file_path, 'w', encoding='utf-8')
    text = text_field.get('1.0', END)
    f.write(text)
    f.close()

def open_window():
    newwindow = Toplevel(root)
    newwindow.title("О программе")
    newwindow.iconbitmap('icon.ico')
    newwindow.geometry("500x500")
    newwindow.resizable(False, False)
    newwindow.config(bg='#A5A5A5')
    text = Label(newwindow, text='Программа создана в 2024 году.')
    text2 = Label(newwindow, text='Так что блокнот баганутый. Если есть баги - пишите в дс (sakatnex).')
    Button1 = Button(newwindow, text='Сайт!', command=lambda: redirect('https://sakatnex.github.io/'))
    Button2 = Button(newwindow, text='Исходник', command=lambda: redirect('https://github.com/sakatnex/StakText'))
    text.pack()
    text2.pack()
    Button1.pack()
    Button2.pack()


root = Tk()
root.title('StakText')
root.geometry('600x700')
root.iconbitmap('icon.ico')

main_menu = Menu(root)

file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Открыть', command=open_file)
file_menu.add_command(label='Сохранить', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Закрыть', command=notepad_exit)


view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label='Тёмная', command=lambda: change_theme('dark'))
view_menu_sub.add_command(label='Светлая', command=lambda: change_theme('light'))


font_menu_sub.add_command(label='Arial', command=lambda: change_font('Arial'))
font_menu_sub.add_command(label='Comic Sans MS', command=lambda: change_font('CSMS'))
font_menu_sub.add_command(label='Times New Roman', command=lambda: change_font('TNR'))
font_menu_sub.add_command(label='Courier New', command=lambda: change_font('CN'))
font_menu_sub.add_command(label='System', command=lambda: change_font('System'))
font_menu_sub.add_command(label='Terminal', command=lambda: change_font('Terminal'))
font_menu_sub.add_command(label='Modern', command=lambda: change_font('Modern'))
font_menu_sub.add_command(label='Fixedsys', command=lambda: change_font('Fixedsys'))
font_menu_sub.add_command(label='Vladimir Script', command=lambda: change_font('VS'))
font_menu_sub.add_command(label='Script', command=lambda: change_font('Script'))
font_menu_sub.add_command(label='Roman', command=lambda: change_font('Roman'))
font_menu_sub.add_command(label='Serif MS', command=lambda: change_font('SM'))
font_menu_sub.add_command(label='Segoe UI', command=lambda: change_font('SU'))

other_menu = Menu(main_menu, tearoff=0)
other_menu.add_command(label='О программе', command=open_window)

main_menu.add_cascade(label='Файл', menu=file_menu)
main_menu.add_cascade(label='Вид', menu=view_menu)
view_menu.add_cascade(label='Темы', menu=view_menu_sub)
view_menu.add_cascade(label='Шрифты', menu=font_menu_sub)
main_menu.add_cascade(label='Другое', menu=other_menu)

root.config(menu=main_menu)

f_Text = Frame(root)
f_Text.pack(fill=BOTH, expand=1)

view_colors = {
    'dark': {
        'text_bg': 'black', 'text_fg': 'lime', 'cursor': 'brown', 'select_bg': '#8D917A'
    },
    'light': {
        'text_bg': 'white', 'text_fg': 'black', 'cursor': '#A5A5A5', 'select_bg': '#FAEDDD'
    }
}

fonts = {
    'Arial': {
        'font': 'Arial 14 bold'
    },
    'CSMS': {
        'font': ('Comic Sans MS', 14, 'bold')
    },
    'TNR': {
        'font': ('Times New Roman', 14, 'bold')
    },
    'CN': {
        'font': ('Courier New', 14, 'bold')
    },
    'System': {
        'font': 'System 14 bold'
    },
    'Terminal': {
        'font': 'Terminal 14 bold'
    },
    'Modern': {
        'font': 'Modern 14 bold'
    },
    'Fixedsys': {
        'font': 'Fixedsys 14 bold'
    },
    'VS': {
        'font': ('Vladimir Script', 14, 'bold')
    },
    'Script': {
        'font': 'Script 14 bold'
    },
    'Roman': {
        'font': 'Roman 14 bold'
    },
    'SM': {
        'font': ('MS Serif', 14, 'bold')
    },
    'SU': {
        'font': ('Segoe UI', 14, 'bold')
    }
}

text_field = Text(f_Text, bg='black', fg='lime', padx=10, pady=10, wrap=WORD, insertbackground='brown', selectbackground='#8D917A', spacing3=10, width=30, font='Arial 14 bold')
text_field.pack(expand=1, fill=BOTH, side=LEFT)

scroll = Scrollbar(f_Text, command=text_field.yview)
scroll.pack(side=LEFT, fill=Y)
text_field.config(yscrollcommand=scroll.set)

root.mainloop()