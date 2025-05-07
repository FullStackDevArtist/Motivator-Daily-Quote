from  tkinter import*
from PIL import Image, ImageTk
import random

# List of inspiring quotes
inspiringQuotes = [
    "Believe you can and you're halfway there.",
    "The only way to do great work is to love what you do.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Your time is limited, don't waste it living someone else's life.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "Don't watch the clock; do what it does. Keep going.",
    "Everything you've ever wanted is on the other side of fear.",
    "The best way to predict the future is to create it.",
    "You are never too old to set another goal or to dream a new dream.",
    "The only limit to our realization of tomorrow is our doubts of today."
]

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
def openSecondWindow():
    #add title to window
    top = Toplevel(firstWindow)
    top.title("Daily Quote")
    top.geometry("300x400")  # Made window taller to fit image
    
    # Add header label to second window
    header2 = Label(
        top,
        text="Find Motivation \nWhen You Need It!",
        font=("Helvetica", 16, "bold"),
        fg="darkblue"
    )
    header2.pack(pady=10)
    
    # Function to update quote
    def updateQuote():
        newQuote = random.choice(inspiringQuotes)
        quoteLabel.config(text=newQuote)
    
    # Function to clear quote
    def clearQuote():
        quoteLabel.config(text="")
    
    # Function to exit second window
    def exitWindow():
        top.destroy()
    
    #Add label to window
    quoteLabel = Label(top, text="When You Need It!", font=("Helvetica", 12), wraplength=250)
    quoteLabel.pack(pady=20)
    
    # Add image to second window
    img2 = Image.open("flowers.jpg")
    img2 = img2.resize((200, 200))  # Resize image
    photo2 = ImageTk.PhotoImage(img2)
    
    # Create and pack image label
    imgLabel = Label(top, image=photo2)
    imgLabel.pack(pady=20)
    imgLabel.image = photo2  # Keep reference

    # Create button frame for better layout
    buttonFrame = Frame(top)
    buttonFrame.pack(pady=10)

    # Add Inspire Me button
    inspireButton = Button(
        buttonFrame,
        text="Inspire Me",
        font=("Helvetica", 12),
        bg="lightblue",
        fg="darkblue",
        command=updateQuote
    )
    inspireButton.pack(side=LEFT, padx=10)

    # Add Clear button
    clearButton = Button(
        buttonFrame,
        text="Clear",
        font=("Helvetica", 12),
        bg="lightblue",
        fg="darkblue",
        command=clearQuote
    )
    clearButton.pack(side=LEFT, padx=10)

    # Add Exit button
    exitButton = Button(
        buttonFrame,
        text="Exit",
        font=("Helvetica", 12),
        bg="lightblue",
        fg="darkblue",
        command=exitWindow
    )
    exitButton.pack(side=LEFT, padx=10)

#make button to launch window
getQuoteButton = Button(
    firstWindow,
    text="Get Daily Quote",
    font=("Helvetica", 12),
    command=openSecondWindow
)
getQuoteButton.grid(row=2, column=0, pady=20, padx=10, sticky="n")

#add image to window
img = Image.open("flowers.jpg")
#resize image
img = img.resize((200, 200))
photo = ImageTk.PhotoImage(img)

#add image to screen
picLabel = Label(firstWindow, image=photo)
picLabel.grid(row=20, column=10)
picLabel.image = photo   

firstWindow.mainloop() 