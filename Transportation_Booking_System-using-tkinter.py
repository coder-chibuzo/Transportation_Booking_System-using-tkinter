
#By Coder_Chibuzo (John Chibuzo Iyioke)

from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import datetime


from tkinter import *



def init(top, gui):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def start_gui():
    
    global w, root
    root = Tk()
    
    top = main_level(root)
    init(root, top)
    root.mainloop()
    w = None


def new_top(root):
    global w, rt
    rt = root
    w = Toplevel(root)
    top = main_level(w)
    init(w, top)
    return w, top


def exit():
    qExit=messagebox.askyesno(" Quit System ", " Do you really want to Exit ? ")
    if qExit > 0:
        root.destroy()
    return

bus_stops = {"Enugu": ["Abuja", "Kaduna", "Porthacourt", "Lagos"],
                "Abuja": ["Enugu", "Kaduna", "Porthacourt", "Lagos"],
                "Kaduna": ["Enugu","Abuja", "Porthacourt", "Lagos"],
                "Porthacourt": ["Enugu","Abuja", "Kaduna", "Lagos"],
                "Lagos": ["Enugu","Abuja", "Kaduna", "Porthacourt"]}


class main_level:

    def bus_Stops(self, top=None):
        self.des_Combo['values'] = bus_stops[self.boarding_Combo.get()]

    def booked(self):
        qPrint = messagebox.askyesno("Confirmation", "Ticket Booked!\n\n Print Ticket ?")
        if qPrint > 0:
            messagebox.showinfo("Booked", "Printing Ticket\n\n " + self.boarding_Combo.get() + "   To   " + self.des_Combo.get() + "\n\n" + " For  " + self.no_of_Adult.get() + " Adult(s)" + "  and  " + self.no_of_Child.get() + " Child(s)")

        self.from2.configure(text="")
        self.to2.configure(text="")
        self.no_of_Adults2.configure(text="")
        self.no_of_Child2.configure(text="")
        self.no_of_Adult.set("Select Adult(s)")
        self.no_of_Child.set("Select Child(s)")
        self.boarding_Combo.set("Select Boarding")
        self.des_Combo.set("Select Destination")

        Date1 = StringVar()
        now = datetime.datetime.now()
        Date1.set(now.strftime("%d-%m-%Y  %I:%M:%S:%p"))
        self.lbltiming2.configure(textvariable=Date1)

        ticket_num = 1
        ticket_nu = str(ticket_num)
        f = open("Tickets.txt", "a")
        f.write(ticket_nu)
        f.close()
        with open('Tickets.txt') as infile:
            characters = 0
            for lineno, line in enumerate(infile, 1):
                wordslist = line.split()
                characters += sum(len(word) for word in wordslist)
        ticketno = StringVar()
        ticket_number = characters
        ticketno.set(ticket_number)
        self.tno.configure(textvariable=ticketno)

    def reset(self):
        self.from2.configure(text="")
        self.to2.configure(text="")
        self.no_of_Adults2.configure(text="")
        self.no_of_Child2.configure(text="")
        self.no_of_Adult.set("Select Adult(s)")
        self.no_of_Child.set("Select Child(s)")
        self.boarding_Combo.set("Select Boarding")
        self.des_Combo.set("Select Destination")

        Date1 = StringVar()
        now = datetime.datetime.now()
        Date1.set(now.strftime("%d-%m-%Y  %I:%M:%S:%p"))
        self.lbltiming2.configure(textvariable=Date1)

    def travel_Cost(self):
        self.from2.configure(text="" + self.boarding_Combo.get())
        self.to2.configure(text="" + self.des_Combo.get())
        self.no_of_Adults2.configure(text="" + self.no_of_Adult.get())
        self.no_of_Child2.configure(text="" + self.no_of_Child.get())
             
        cost=0
        if (self.no_of_Adult.get() == "0") :            
            calculated_cost=cost+0
        elif (self.no_of_Adult.get() == "1"):
            calculated_cost=cost+1
        elif (self.no_of_Adult.get() == "2"):
            calculated_cost=cost+2
        elif (self.no_of_Adult.get() == "3"):
            calculated_cost=cost+3
            aticket=calculated_cost  
        
            child_cost=0
        if (self.no_of_Child.get()=="0") :
            c_cost=child_cost+0
        elif (self.no_of_Child.get()=="1") :
            c_cost=child_cost+1/2
        elif (self.no_of_Child.get()=="2") :
            c_cost=child_cost+2/2
        elif (self.no_of_Child.get()=="3") :
            c_cost=child_cost+3/2
            cticket=c_cost
        
            passenger=cticket+aticket
        
            fare=0
        if (self.boarding_Combo.get() == "Enugu ") and (self.des_Combo.get() == "Abuja"):
            t_fare=fare+5000
        elif (self.boarding_Combo.get() == "Enugu") and (self.des_Combo.get() == "Kaduna"):
            t_fare=fare+6000
        elif (self.boarding_Combo.get() == "Enugu") and (self.des_Combo.get() == "Porthacourt"):
            t_fare=fare+6000
        elif (self.boarding_Combo.get() == "Enugu") and (self.des_Combo.get() == "Lagos"):
            t_fare=fare+6000

        elif (self.boarding_Combo.get() == "Abuja ") and (self.des_Combo.get() == "Enugu"):
            t_fare=fare+5000
        elif (self.boarding_Combo.get() == "Abuja") and (self.des_Combo.get() == "Kaduna"):
            t_fare=fare+1500
        elif (self.boarding_Combo.get() == "Abuja") and (self.des_Combo.get() == "Porthacourt"):
            t_fare=fare+6000
        elif (self.boarding_Combo.get() == "Abuja") and (self.des_Combo.get() == "Lagos"):
            t_fare=fare+7000


        elif (self.boarding_Combo.get() == "Kaduna ") and (self.des_Combo.get() == "Enugu"):
            t_fare=fare+6000
        elif (self.boarding_Combo.get() == "Kaduna") and (self.des_Combo.get() == "Abuja"):
            t_fare=fare+1500
        elif (self.boarding_Combo.get() == "Kaduna") and (self.des_Combo.get() == "Porthacourt"):
            t_fare=fare+7000
        elif (self.boarding_Combo.get() == "Kaduna") and (self.des_Combo.get() == "Lagos"):
            t_fare=fare+9000

        elif (self.boarding_Combo.get() == "Porthacourt ") and (self.des_Combo.get() == "Enugu"):
            t_fare=fare+6000
        elif (self.boarding_Combo.get() == "Porthacourt") and (self.des_Combo.get() == "Abuja"):
            t_fare=fare+1500
        elif (self.boarding_Combo.get() == "Porthacourt") and (self.des_Combo.get() == "Kaduna"):
            t_fare=fare+7000
        elif (self.boarding_Combo.get() == "Porthacourt") and (self.des_Combo.get() == "Lagos"):
            t_fare=fare+9000
        
        elif (self.boarding_Combo.get() == "Lagos") and (self.des_Combo.get() == "Enugu"):
            t_fare=fare+6000
        elif (self.boarding_Combo.get() == "Lagos") and (self.des_Combo.get() == "Abuja"):
            t_fare=fare+1500
        elif (self.boarding_Combo.get() == "Lagos ") and (self.des_Combo.get() == "Kaduna"):
            t_fare=fare+7000
        elif (self.boarding_Combo.get() == "Lagos") and (self.des_Combo.get() == "Porthacourt"):
            t_fare=fare+9000
            total_fare=t_fare
        
            final_price=(total_fare*passenger)
        
        
        
        
            self.tCost2.configure(text=final_price)
            
            
        
        
            return

    def __init__(self, top=None):
        top.geometry("732x443")#+327+147")
        top.title("Bus Ticketing System")
        self.style = ttk.Style()

        font10 = "-family {Wide Latin} -size 10 -weight bold -slant "  \
                 "roman -underline 0 -overstrike 0"
        font15 = "-family {Snap ITC} -size 20 -weight bold -slant "  \
                 "roman -underline 1 -overstrike 0"
        font17 = "-family {Segoe UI} -size 10 -weight bold -slant "  \
                 "roman -underline 0 -overstrike 0"
        font18 = "-family {Segoe UI} -size 11 -weight bold -slant "  \
                 "roman -underline 0 -overstrike 0"

        Date1 = StringVar()
        now = datetime.datetime.now()
        Date1.set(now.strftime("%d-%m-%Y  %I:%M:%S:%p"))

        with open('Tickets.txt') as infile:
            characters = 0
            for lineno, line in enumerate(infile, 1):
                wordslist = line.split()
                characters += sum(len(word) for word in wordslist)
        ticketno = StringVar()
        ticket_number = characters
        ticketno.set(ticket_number)

        self.frame_Booking_Panel = Frame(top)
        self.frame_Booking_Panel.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.frame_Booking_Panel.configure(background="white", relief=GROOVE, borderwidth="5")


        self.bus_Service = Label(self.frame_Booking_Panel)
        self.bus_Service.place(relx=0.14, rely=0.05, height=21, width=544)
        self.bus_Service.configure(text="TRANSPORT BOOKING SERVICE", background="white", font=font18)
        


        self.ticket_No = Label(self.frame_Booking_Panel)
        self.ticket_No.place(relx=0.04, rely=0.18, height=21, width=84)
        self.ticket_No.configure(text="Ticket No. : ", background="white", font=font18)


        self.tno = Label(self.frame_Booking_Panel)
        self.tno.place(relx=0.15, rely=0.18, height=21, width=30)
        self.tno.configure(background="white", font=font18, textvariable=ticketno)


        self.bus_id = Label(self.frame_Booking_Panel)
        self.bus_id.place(relx=0.75, rely=0.16, height=21, width=119)
        self.bus_id.configure(background="white", font=font18, text="Bus : GKC001")


        self.boarding_lbl = Label(self.frame_Booking_Panel)
        self.boarding_lbl.place(relx=0.04, rely=0.32, height=23, width=84)
        self.boarding_lbl.configure(text="Boarding :", background="white",font=font17)


        self.destination_lbl = Label(self.frame_Booking_Panel)
        self.destination_lbl.place(relx=0.52, rely=0.32, height=21, width=134)
        self.destination_lbl.configure(text="Destination :", background="white", font=font18)


        self.boarding_Combo = ttk.Combobox(self.frame_Booking_Panel, state='readonly', values=list(bus_stops.keys()))
        self.boarding_Combo.place(relx=0.19, rely=0.32, relheight=0.05, relwidth=0.2)
        self.boarding_Combo.set("Select Boarding")
        self.boarding_Combo.bind('<<ComboboxSelected>>', self.bus_Stops)

        self.des_Combo = ttk.Combobox(self.frame_Booking_Panel, state='readonly')
        self.des_Combo.place(relx=0.74, rely=0.32, relheight=0.05, relwidth=0.2)
        self.des_Combo.bind('<<ComboboxSelected>>')
        self.des_Combo.set("Select Destination")

        self.passengers_lbl = Label(self.frame_Booking_Panel)
        self.passengers_lbl.place(relx=0.04, rely=0.47, height=21, width=114)
        self.passengers_lbl.configure(text="Passenger(s) :", background="#FFFFFF", font=font18)

        self.no_of_Adult = ttk.Combobox(self.frame_Booking_Panel, state='readonly')
        self.no_of_Adult.place(relx=0.16, rely=0.56, relheight=0.05, relwidth=0.15)
        self.no_of_Adult['values'] = ("0", "1", "2", "3")                                     #here
        self.no_of_Adult.set("Select Adult(s)")
        self.no_of_Adult.bind('<<ComboboxSelected>>')

        self.no_of_Child = ttk.Combobox(self.frame_Booking_Panel, state='readonly')
        self.no_of_Child.place(relx=0.16, rely=0.65, relheight=0.05, relwidth=0.15)
        self.no_of_Child['values'] = ("0", "1", "2", "3")
        self.no_of_Child.set("Select Child(s)")
        self.no_of_Child.bind('<<ComboboxSelected>>')

        self.book_Button = Button(self.frame_Booking_Panel)
        self.book_Button.place(relx=0.78, rely=0.62, height=24, width=107)
        self.book_Button.configure(text="Book", background="white", font=font18, command=self.booked)

        self.exit_Button = Button(self.frame_Booking_Panel)
        self.exit_Button.place(relx=0.78, rely=0.92, height=24, width=107)
        self.exit_Button.configure(text="Exit", background="white", font=font18, command=exit)

        self.reset_Button = Button(self.frame_Booking_Panel)
        self.reset_Button.place(relx=0.78, rely=0.77, height=24, width=107)
        self.reset_Button.configure(text="Reset", background="white", font=font18, command=self.reset)


        self.total_Button = Button(self.frame_Booking_Panel)
        self.total_Button.place(relx=0.78, rely=0.47, height=24, width=107)
        self.total_Button.configure(text="Total", background="white", font=font18, command=self.travel_Cost)

        self.lblAdultno = Label(self.frame_Booking_Panel)
        self.lblAdultno.place(relx=0.05, rely=0.56, height=21, width=64)
        self.lblAdultno.configure(background="white", text="Adult")
        

        self.lblChildno = Label(self.frame_Booking_Panel)
        self.lblChildno.place(relx=0.05, rely=0.65, height=21, width=64)
        self.lblChildno.configure(background="white", text="Child")
        

        self.total_Frame = Frame(self.frame_Booking_Panel)
        self.total_Frame.place(relx=0.36, rely=0.47, relheight=0.44, relwidth=0.36)
        self.total_Frame.configure(background="green", relief=GROOVE, borderwidth="1")


        self.from1 = Label(self.total_Frame)
        self.from1.place(relx=0.08, rely=0.05, height=21, width=54)
        self.from1.configure(text="From :")

        self.from2 = Label(self.total_Frame)
        self.from2.place(relx=0.40, rely=0.05, height=21, width=121)
        self.from2.configure(highlightcolor="black")

        self.to1 = Label(self.total_Frame)
        self.to1.place(relx=0.08, rely=0.21, height=21, width=49)
        self.to1.configure(text="To :")

        self.to2 = Label(self.total_Frame)
        self.to2.place(relx=0.40, rely=0.21, height=21, width=121)
        

        self.no_of_Adults1 = Label(self.total_Frame)
        self.no_of_Adults1.place(relx=0.08, rely=0.36, height=21, width=55)
        self.no_of_Adults1.configure(text="Adult :")

        self.no_of_Adults2 = Label(self.total_Frame)
        self.no_of_Adults2.place(relx=0.40, rely=0.36, height=21, width=121)
        

        self.no_of_Child1 = Label(self.total_Frame)
        self.no_of_Child1.place(relx=0.08, rely=0.51, height=21, width=46)
        self.no_of_Child1.configure(text="Child :")
        self.no_of_Child2 = Label(self.total_Frame)
        self.no_of_Child2.place(relx=0.40, rely=0.51, height=21, width=121)
        

        self.tCost1 = Label(self.total_Frame)
        self.tCost1.place(relx=0.08, rely=0.67, height=21, width=74)
        self.tCost1.configure(text="Total Cost :")
        #cost box
        self.tCost2 = Label(self.total_Frame)
        self.tCost2.place(relx=0.40, rely=0.67, height=21, width=121)
               
        
        
        
        self.lbltiming1 = Label(self.total_Frame)
        self.lbltiming1.place(relx=0.08, rely=0.82, height=21, width=74)
        self.lbltiming1.configure(text="Booking at :")

        self.lbltiming2 = Label(self.total_Frame)
        self.lbltiming2.place(relx=0.40, rely=0.82, height=21, width=135)
        self.lbltiming2.configure(textvariable=Date1)


start_gui()

