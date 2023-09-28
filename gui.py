import PySimpleGUI as sg
from main import find
import time

array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
array2 = ["+", "-", "*", "/"]

output = ""

buttonsize = ("15", "2")
buttoncolor1 = ("#2da6f7")
bhc = ()
buttoncolor2 = ("#146eff")
bhc = ()
bg = ("#d9d9d9")
bg2 = ("#828282")
textcolor = ("#424242")

out = False

layout = [
    [sg.Text(text="enter a number", size=("42", "1"), text_color=textcolor, font=(
        "source code pro", 26), justification="center", relief="sunken", key="dis", background_color=bg2)],
    [sg.Button(button_text="1", size=buttonsize, border_width="4", font=("source code pro", 15), button_color=buttoncolor1, mouseover_colors=textcolor), sg.Button(button_text="2", size=buttonsize, border_width="4", font=("source code pro", 15), button_color=buttoncolor1), sg.Button(
        button_text="3", size=buttonsize, border_width="4", font=("source code pro", 15), button_color=buttoncolor1), sg.Button(button_text="+", size=buttonsize, border_width="4", font=("source code pro", 15), button_color=buttoncolor2)],

    [sg.Button(button_text="4", size=buttonsize, border_width="4", font=("source code pro", 15), button_color=buttoncolor1), sg.Button(button_text="5", size=buttonsize, border_width="4", font=("source code pro", 15), button_color=buttoncolor1), sg.Button(
        button_text="6", size=buttonsize, border_width="4", font=("source code pro", 15), button_color=buttoncolor1), sg.Button(button_text="-", size=buttonsize, border_width="4", font=("source code pro", 15), button_color=buttoncolor2)],

    [sg.Button(button_text="7", size=buttonsize, border_width="4", font=("source code pro", 15), button_color=buttoncolor1), sg.Button(button_text="8", size=buttonsize, border_width="4", font=("source code pro", 15), button_color=buttoncolor1), sg.Button(
        button_text="9", size=buttonsize, border_width="4", font=("source code pro", 15), button_color=buttoncolor1), sg.Button(button_text="*", size=buttonsize, border_width="4", font=("source code pro", 15), button_color=buttoncolor2)],

    [sg.Button(button_text="enter", size=buttonsize, border_width="4", font=("source code pro", 15), focus=True, button_color=("#e84e3c")), sg.Button(button_text="clear", size=buttonsize, border_width="4", font=("source code pro", 15), button_color=buttoncolor1), sg.Button(button_text="0", size=buttonsize, button_color=buttoncolor1, border_width="4", font=("source code pro", 15)), sg.Button(button_text="/", size=buttonsize, button_color=buttoncolor2, border_width="4", font=("source code pro", 15))]]

window = sg.Window(title="Hello World", layout=[
    layout], margins=(50, 50), background_color=bg)

while True:
    event, num = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    try:

        if int(str(event)) in array1:
            if out:
                output = ""
                out = False
            output = output + str(event)

    except:
        if str(event) in ["+", "-", "*", "/"]:
            if out:
                output = ""
                out = False
            output = output + str(event)
    if event == "clear":
        output = ""
    print(event)

    window["dis"].update(value=str(output))
    try:
        if event == "enter":
            i = find(output)
            output = ""
            for j in i:
                output = output + str(j)
            window["dis"].update(value=str(output))
            out = True
    except:
        output = "please enter a valid input"
        window["dis"].update(value=str(output))
        out = True


window.close()
