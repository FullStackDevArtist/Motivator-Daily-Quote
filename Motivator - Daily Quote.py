from  tkinter import*
#from PIL import Image, ImageTk 

#Create Window
firstWindow = Tk()

#give window a title
firstWindow.title("Motivator - Daily Quote")
firstWindow.columnconfigure(0, weight=1)

#Header for Label
header = Label(
 firstWindow,
 text="Motivator-Daily Quote",
 font=("Helvetica", 16, "bold"),
 fg="darkblue")
header.grid(row=0, column=0, pady=10, sticky="ew")





#Create Welcome message Label 
welcomeMsg = Label(
    firstWindow,
    text="Welcome to the Motivator Daily Quote App!\nGet ready to be inspired and start your day with a positive mindset.",
    font=("Helvetica", 12),
    fg="black",
    justify="center",
    wraplength=400
)
welcomeMsg.grid(row=1, column=0, columnspan=10, pady=(0, 20))











# create another window
def open_second_window():

#add title to window
    top = Toplevel(firstWindow)
    top.title("Daily Quote")
    top.geometry("300x200")
    
#Add label to window
    quote_label = Label(top, text="You are capable of amazing things!", font=("Helvetica", 12), wraplength=250)
    quote_label.pack(pady=40)
    
#make button to launch window
get_quote_button = Button(
    firstWindow,
    text="Get Daily Quote",
    font=("Helvetica", 12),
    command=open_second_window
)
get_quote_button.grid(row=2, column=0, pady=20, padx=10, sticky="n")

#add image to window
#img = Image.open("flowers.jpg")
#photo = ImageTk.PhotoImage(img)



#add image to screen
#picLabel = Label (firstWindow, image = photo)
#picLabel.grid (row = 20, column = 10)
#picLabel.image = photo   



               

firstWindow.mainloop()
