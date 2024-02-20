from tkinter import *
from browseServices import searchAlbumList

window = Tk()
window.title("Search Playlist on Spotify")
window.geometry("800x600")

# Global variables
artistNameVar = StringVar()
artist = ""

# Global functions
def search():
    artist = artistNameVar.get()
    print("Artist name: " + artist)
    artistNameVar.set("")
    playList = searchAlbumList(artist)
    if (playList == None):
        print("No artist with this name exists.....")

    total_rows = len(playList)
    total_columns = len(playList[0])
    for i in range(total_rows):
        for j in range(total_columns):
            match j:
                case 0:
                    columnWidth = 5
                case 1:
                    columnWidth = 40
                case 2:
                    columnWidth = 60    
            e = Entry(albumFrame, width=columnWidth, font=("Arial", 10, "bold"))
            e.grid(row=i, column=j, pady=2)
            e.insert(END, playList[i][j])

def closeApp():
    window.destroy()

# Heading lable
headingLable = Label(window, text="Search Playlist on Spotify", font=("times new roman", 30, "bold"), background="gray20", foreground="gold", border=2, relief=GROOVE)
# Display Heading lable
headingLable.pack(fill=X)

# Search frame
searchFrame = LabelFrame(window, font=("times new roman", 20, "bold"), background="cadetblue2",relief=GROOVE)
artistNameLable = Label(searchFrame, text= "Enter Artist Name", font=("times new roman", 10, "bold"), background="cadetblue2", foreground="black", border=2, relief=GROOVE)
artistNameEntry = Entry(searchFrame, font=("arial", 10), textvariable=artistNameVar)
searchButton = Button(searchFrame, text="Search", font=("times new roman", 10, "bold"), command=search)
closeAppButton = Button(searchFrame, text="Close", font=("times new roman", 10, "bold"), command=closeApp)
# Dislay Search frame
searchFrame.pack(pady=25, fill=X)
artistNameLable.grid(row=0, column=0, padx=260, pady=5, sticky=W)
artistNameEntry.grid(row=1, column=0, padx=260, sticky=W)
searchButton.grid(row=3, column=0, padx= 10, pady=20)
closeAppButton.grid(row=4, column=0, padx= 10, pady=10)

# Album frame
albumFrame = LabelFrame(window, text="", font=("times new roman", 20, "bold"), background="white", foreground="black", border=2, relief=GROOVE)
# Display Album frame
albumFrame.pack(fill=X, padx= 5)


window.mainloop()