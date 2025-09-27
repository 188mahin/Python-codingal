from tkinter import *
window=Tk()
window.title("Event handler")
window.geometry("100x100")
def handle_keys(event):
    print(event.char)
window.bind("<Key>",handle_keys)
def handle_click(event):
    print("\n button was clicked")
button=Button(text="click me")
button.pack()
button.bind("<Button-1>",handle_click)
window.mainloop()

    