from tkinter import *
import tkinter.messagebox
import frontend

class Firstpage:

    def __init__(self, root):
        self.root=root
        self.root.title('Movie Booking System')
        self.root.geometry('1350x750')
        self.root.config(bg="black")

        #Fraames
        MainFrame = Frame(self.root,bg='black')
        MainFrame.grid()

        HeadFrame = Frame(MainFrame,bd=1,bg='black',relief=RIDGE,padx=50,pady=10)
        HeadFrame.pack(side=TOP)

        self.TFrame=Label(HeadFrame, font=('Arial', 50, 'bold'), text="MOVIE BOOKING SYSTEM", bg="black", fg="red")
        self.TFrame.grid()

        BodyFrame=Frame(MainFrame, bd=2, width=1300, height=500, padx=20, pady=20, bg="black", relief=RIDGE)
        BodyFrame.pack(side=BOTTOM)

        btnbook = Button(BodyFrame,text='Book Tickets',padx=20,pady=20)
        btnbook.grid(row=0,column=0)

        btnadmin = Button(BodyFrame,text='Admin Section',padx=20,pady=20,command=lambda:self.open(MainFrame))
        btnadmin.grid(row=0,column=1)


    def open(self,frame):
        
        frame.grid_forget()
        frontend.Movie(root)


        
        
if __name__=='__main__':
	root=Tk()
	database = Firstpage(root)
	root.mainloop()