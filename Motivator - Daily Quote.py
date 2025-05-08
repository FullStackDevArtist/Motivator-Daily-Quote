# Import required libraries for GUI
from tkinter import *          # For creating the graphical user interface
from PIL import Image, ImageTk # For handling and displaying images
import random                  # For selecting random quotes

#  Data Module 
# This module manages the collection of motivational quotes
def getInspiringQuotes():
    # Returns a list of motivational quotes for the application
    return [
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

#  Utility Module
# This module handles image and display
def loadAndResizeImage(path, size):
    # Loads an image and resizes it to the specified dimensions
    img = Image.open(path)     # Open the image file
    img = img.resize(size)     # Resize the image to size
    return ImageTk.PhotoImage(img)  # Convert to Tkinter-image format

#   Check Module 
# This module check the quotes for the first window
def checkQuotes():
    # Displays the number of available quotes and a random quote
    print("\nChecking Quotes...")
    
    quotes = getInspiringQuotes()  # Get the list of quotes
    print(f"Total quotes: {len(quotes)}")  # Show total number of quotes
    
    quote = random.choice(quotes)  # Select a random quote
    print(f"Random quote: {quote}")  # Display the selected quote
    
    print("Check complete!")

#  UI Module 
# This module creates and manages the quote display window
def openSecondWindow(parent):
    # Create a new window for displaying quotes
    top = Toplevel(parent)     # Create a new window on top of the main window
    top.title("Daily Quote")   # Window title
    top.geometry("500x600")    # Window size

    # Create Background image
    bgPhoto = loadAndResizeImage("3.jpg", (500, 600))  # Load and resize background
    bgLabel = Label(top, image=bgPhoto)  # Create label for background
    bgLabel.place(x=0, y=0, relwidth=1, relheight=1)  # Position image for background
    bgLabel.image = bgPhoto  # Keep reference to prevent garbage collection

    # Create and display the header
    header2 = Label(top, text="Find Motivation \nWhen You Need It!", 
                   font=("Helvetica", 16, "bold"), fg="darkblue", bg=None)
    header2.pack(pady=10)

    # Create the quote display 
    quoteLabel = Label(top, text="When You Need It!", 
                      font=("Helvetica", 12), wraplength=250, bg=None)
    quoteLabel.pack(pady=20)

    # Add the image #2 for second window
    img2Photo = loadAndResizeImage("2.jpg", (200, 200))  # Load and resize image
    imgLabel = Label(top, image=img2Photo, bg=None)  # Create label for image
    imgLabel.pack(pady=20)
    imgLabel.image = img2Photo  # Keep reference to prevent garbage collection

    # Function to update the quote for second window
    def updateQuote():
        quoteLabel.config(text=random.choice(getInspiringQuotes()))

    # Function to clear the quote for second window
    def clearQuote():
        quoteLabel.config(text="")

    # Function to close the window for second window
    def exitWindow():
        top.destroy()

    # Frame for the buttons for second window
    buttonFrame = Frame(top, bg=None)
    buttonFrame.pack(pady=10)

    # Add the buttons for second window
    Button(buttonFrame, text="Inspire Me", font=("Helvetica", 12), 
           bg="lightblue", fg="darkblue", command=updateQuote).pack(side=LEFT, padx=10)
    Button(buttonFrame, text="Clear", font=("Helvetica", 12), 
           bg="lightblue", fg="darkblue", command=clearQuote).pack(side=LEFT, padx=10)
    Button(buttonFrame, text="Exit", font=("Helvetica", 12), 
           bg="lightblue", fg="darkblue", command=exitWindow).pack(side=LEFT, padx=10)

#  Main Window Module 
# Creates the main application 
def launchMainWindow():
    # Create the main application window
    firstWindow = Tk()  # Create the main window
    firstWindow.geometry("500x600")  #Window size

    # Set up the background image for first window
    bgPhoto = loadAndResizeImage("3.jpg", (500, 600))  # Load and resize background
    bgLabel = Label(firstWindow, image=bgPhoto)  # Create label for background
    bgLabel.place(x=0, y=0, relwidth=1, relheight=1)  # Position background
    bgLabel.image = bgPhoto  # Keep reference to prevent garbage collection

    # Configure window properties for first window
    firstWindow.title("Motivator - Daily Quote")  # Set window title
    firstWindow.columnconfigure(0, weight=1)  # Grid layout

    # Create and display the main header for first window
    header = Label(firstWindow, text="Motivator-Daily Quote", 
                  font=("Helvetica", 16, "bold"), fg="darkblue", bg=None)
    header.grid(row=0, column=0, pady=10, sticky="ew")

    # Add the welcome message for first window
    welcomeMsg = Label(
        firstWindow,
        text="Welcome to the Motivator Daily Quote App!\nGet ready to be inspired and start your day with a positive mindset.",
        font=("Helvetica", 12),
        fg="black",
        justify="center",
        wraplength=400,
        bg=None
    )
    welcomeMsg.grid(row=1, column=0, columnspan=10, pady=(0, 20))

    # Add the image for first window
    imgPhoto = loadAndResizeImage("1.jpg", (200, 200))  # Load and resize image
    picLabel = Label(firstWindow, image=imgPhoto, bg=None)  #Label for image
    picLabel.grid(row=2, column=0, pady=20)
    picLabel.image = imgPhoto  # Keep reference to prevent garbage collection

    # Add the button for first window
    getQuoteButton = Button(
        firstWindow,
        text="Get Daily Quote",
        font=("Helvetica", 12),
        command=lambda: openSecondWindow(firstWindow)
    )
    getQuoteButton.grid(row=3, column=0, pady=20, padx=10, sticky="n")

    # Add the check button for first window
    checkButton = Button(
        firstWindow,
        text="Check Quotes",
        font=("Helvetica", 12),
        command=checkQuotes
    )
    checkButton.grid(row=4, column=0, pady=10, padx=10, sticky="n")

    # Start the main loop for first window that will always run in background
    firstWindow.mainloop()

# Start the application
launchMainWindow() 