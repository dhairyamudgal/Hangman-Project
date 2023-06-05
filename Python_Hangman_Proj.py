import tkinter  # importing libraries
import random
from PIL import ImageTk, Image

# setting up gui interface
root = tkinter.Tk()
root.title("Hangman")
root.configure(bg="grey")


class Hang:
    # __init__ function to initialize self. variables
    def __init__(self):
        self.wordbank = ["beach", "mouse", "array"]
        self.turn = 0
        self.name = ""
        self.guesses = ""
        self.guessword = random.choice(self.wordbank)
        self.image1 = Image.open("/Users/dhairyamudgal/Desktop/Python_Hangman_Tkinter/img1.jpeg")
        self.image1 = self.image1.resize((400, 400), Image.ANTIALIAS)

        self.img = ImageTk.PhotoImage(self.image1)
        self.images = tkinter.Label(root, width="400", height="400", image=self.img)

    # setting up hangman gui and storing name in self.name
    def button_name(self):
        self.name = entry.get("1.0", "end-1c")

        progstr.set(("Hello", self.name, "!", "Let's", "Play"))
        # forgeting home gui
        entry.grid_forget()
        myButton.grid_forget()
        Label_welcome.grid_forget()
        Label_name.grid_forget()
        # setting up hangman gui
        Label_1.grid(row=0, columnspan=3)  # First Line
        Label_start.grid(row=1, columnspan=3)  # Second Line
        Label_US.grid(row=2, columnspan=3)  # _ _ _ _ _
        Label_Guess.grid(row=3, column=0, pady=5, columnspan=2)  # Guess Character
        text.grid(row=3, column=2)
        guess_button.grid(row=4, column=0, pady=2, padx=2)
        self.images.grid(row=5, columnspan=3)

    # checking if guess character exist or not , and accordingly display  images
    def button_guess(self):
        self.images.destroy()
        Label_result.pack_forget()
        # checking if all 7 tries are done or not
        if self.turn < 6:
            guess = text.get("1.0", "end-1c")
            self.guesses = self.guesses + guess
            progress = ""
            failed = 0
            # updating all guessed words till now
            for char in self.guessword:
                if char in self.guesses:
                    progress = progress + char + " "
                else:
                    progress = progress + "_ "

                    failed = failed + 1
            word.set(progress)
            if not (guess in progress):
                self.turn = self.turn + 1
            if self.turn == 0:
                self.image1 = Image.open("/Users/dhairyamudgal/Desktop/Python_Hangman_Tkinter/img1.jpeg")
            elif self.turn == 1:
                self.image1 = Image.open("/Users/dhairyamudgal/Desktop/Python_Hangman_Tkinter/img2.jpeg")
            elif self.turn == 2:
                self.image1 = Image.open("/Users/dhairyamudgal/Desktop/Python_Hangman_Tkinter/img3.jpeg")
            elif self.turn == 3:
                self.image1 = Image.open("/Users/dhairyamudgal/Desktop/Python_Hangman_Tkinter/img4.jpeg")
            elif self.turn == 4:
                self.image1 = Image.open("/Users/dhairyamudgal/Desktop/Python_Hangman_Tkinter/img5.jpeg")
            elif self.turn == 5:
                self.image1 = Image.open("/Users/dhairyamudgal/Desktop/Python_Hangman_Tkinter/img6.jpeg")
            elif self.turn == 6:
                self.image1 = Image.open("/Users/dhairyamudgal/Desktop/Python_Hangman_Tkinter/img7.jpeg")

            if self.turn < 6:
                result.set(("You", "have", 6 - self.turn, "tries", "Left"))

            else:
                self.image1 = Image.open("/Users/dhairyamudgal/Desktop/Python_Hangman_Tkinter/img.lose.jpeg")
                result.set("You Lose")

            if failed == 0:
                self.image1 = Image.open("/Users/dhairyamudgal/Desktop/Python_Hangman_Tkinter/img.win.jpeg")
                result.set("You Win")
            text.delete("1.0", "end")
        else:
            result.set("You Lose")

        self.image1 = self.image1.resize((400, 400), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.image1)
        self.images = tkinter.Label(root, width="380", height="380", image=self.img)
        self.images.grid(row=5, columnspan=3)
        # updating result
        Label_result.grid(row=4, column=1, columnspan=2, padx=8, pady=8)


m = Hang()
# tkinter textvariables
result = tkinter.StringVar()
progstr = tkinter.StringVar()
word = tkinter.StringVar()
word.set("_ _ _ _ _ ")

# gui widgets
Label_welcome = tkinter.Label(root, text="Welcome to HANGMAN !", width=20, font=("Comic Sans MS", 37), bg="teal",fg="white")
Label_name = tkinter.Label(root, text="Enter your name :", width=17, font=("Comic Sans MS", 20), bg="green", fg="white")
entry = tkinter.Text(root, height=1, width=17, font=("Comic Sans MS", 20))
myButton = tkinter.Button(root, text="Enter !", width=50, height=1, font=("Comic Sans MS", 15), fg="black",
                          command=m.button_name)
Label_1 = tkinter.Label(root, text="H A N G M A N", font=("Comic Sans MS", 40), bg="teal", fg=("white"),
                        width=13)  # First Line
Label_start = tkinter.Label(root, textvariable=progstr, font=("Comic Sans MS", 20), bg="green", fg="white",
                            width=26)  # Second Line
Label_US = tkinter.Label(root, textvariable=word, font=("Comic Sans MS", 40), bg="green", fg="white", width=13)
Label_Guess = tkinter.Label(root, text=" Start Guessing", font=("Comic Sans MS", 20), bg="light green", width=20)
text = tkinter.Text(root, width=5, height=1, font=("Comic Sans MS", 20))
guess_button = tkinter.Button(root, text="Guess", command=lambda: m.button_guess(), font=("Comic Sans MS", 13),
                              width=10)
Label_result = tkinter.Label(root, textvariable=result, font=("Comic Sans MS", 20))

Label_welcome.grid(row=0, columnspan=2)
Label_name.grid(row=1, column=0, pady=5)
entry.grid(row=1, column=1)
myButton.grid(row=2, columnspan=2)

root.mainloop()