from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
count=5
number = random.randint(0,100)

# -----------WORD MANAGER------------

data_format_panda = pandas.read_csv("data/french_words.csv")
data_dic= data_format_panda.to_dict()

def change_ui(new_image,cuv,lang):
    canvas.itemconfig(canvas_image,image=new_image)
    canvas.itemconfig(language,text=lang)
    canvas.itemconfig(word,text=cuv)

def next_word():
    global number
    number = random.randint(0, 100)
    new_french_word = data_dic["French"][number]
    change_ui(front_image,new_french_word,"french")
    count_down(count,number)

def count_down(count_sec,number):

    if count_sec > 0:
        canvas.itemconfig(counter, text=f"{count_sec}")
        timer = window.after(1000,count_down,count_sec-1,number)
    else:
        canvas.itemconfig(counter, text=f"Got the word?", font = ("ariel", 30, "bold"))
        change_ui(back_image,data_dic["English"][number], "english")



#-------------------UI-----------------
window = Tk()
window.title("Flashy")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

canvas = Canvas(width=800, height= 526, highlightthickness=0, bg = BACKGROUND_COLOR)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400,270,image=front_image)
language = canvas.create_text(400,150,text = "French", fill="black", font=("Ariel",40,"italic"))
counter = canvas.create_text(400,50,fill="black", font=("Ariel", 60, "bold"))
french_word = data_dic["French"][number]
word = canvas.create_text(400,263, text =french_word, fill ="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, columnspan=2, row=0)

check_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

check_button = Button(image=check_image, highlightthickness=0,command=next_word)
check_button.grid(column=1, row = 1)


wrong_button = Button(image=wrong_image, highlightthickness=0,command=next_word)
wrong_button.grid(column=0, row=1)

count_down(count,number)





window.mainloop()



