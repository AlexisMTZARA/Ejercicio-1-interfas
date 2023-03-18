from tkinter import*
from tkinter import ttk

raiz = Tk()
raiz.title("EJERCIO 1:) BRANDOM")
raiz.geometry("600x450")

pag = ttk.Notebook(raiz)
pag.pack()



frame1 = ttk.Frame(pag, width=500, height=500)
frame1.pack(fill='both', expand='1')


frame2 = ttk.Frame(pag, width=500, height=500)
frame2.pack(fill='both', expand='1')


frame3 = ttk.Frame(pag, width=20, height=20)
frame3.pack(fill='both', expand='1')


frame4 = ttk.Frame(pag, width=500, height=500)
frame4.pack(fill='both', expand='1')


frame5 = ttk.Frame(pag, width=500, height=500)
frame5.pack(fill='both', expand='1')

frame6 = ttk.Frame(frame1, padding="150 5 251 5", borderwidth=2, relief="raised")
frame6.grid(column=0, row=0)

frame7 = ttk.Frame(frame1, padding="33 10 126 10", borderwidth=2, relief="raised")
frame7.grid(column=0, row=1)

frame8 = ttk.Frame(frame1, padding="12 10 148 10", borderwidth=2, relief="raised")
frame8.grid(column=0, row=2)

frame9 = ttk.Frame(frame1, padding="20 10 136 10", borderwidth=2, relief="raised")
frame9.grid(column=0, row=3)

frame10 = ttk.Frame(frame1, padding="112 10 213 35", borderwidth=3, relief="raised")
frame10.grid(column=0, row=4)

pag.add(frame1, text="         ADD          " )
pag.add(frame2, text="         DELETE          ")
pag.add(frame3, text="         SEARCH         ")
pag.add(frame4, text="           SERVICES          ")
pag.add(frame5, text="           HELP        ")


'''----------------------------------------------'''
firstnameLabel = ttk.Label(frame7, text="FIRST NAME: ")
firstnameLabel.grid(column=0, row=0)

firstnameEntry = ttk.Entry(frame7, width=12)
firstnameEntry.grid(column=1, row=0)

lastnameLabel = ttk.Label(frame7, text="LAST NAME: " )
lastnameLabel.grid(column=2, row=0, padx=3)

lastnameEntry = ttk.Entry(frame7, width=17)
lastnameEntry.grid(column=3, row=0)

cumpleLabel = ttk.Label(frame7, text="BITRH DATE:" )
cumpleLabel.grid(column=0, row=1, pady=20)

diaEntry = ttk.Entry(frame7, width=2)
diaEntry.grid(column=1,row=1, sticky=W)

mesEntry = ttk.Entry(frame7, width=2)
mesEntry.grid(column=1,row=1)

añoEntry = ttk.Entry(frame7, width=2)
añoEntry.grid(column=1,row=1, sticky=E)

ciudadLabel = ttk.Label(frame7, text="COUNTRY:" )
ciudadLabel.grid(column=2, row=1, pady=20)

countryEntry = ttk.Entry(frame7, width=18)
countryEntry.grid(column=3,row=1, sticky=W)
'''----------------------------------------------------------'''

cardLabel = ttk.Label(frame8, text="Credit Card (if any) :")
cardLabel.grid(column=0, row=0)

cardEntry = ttk.Entry(frame8, width=20)
cardEntry.grid(column=1, row=0)

creditcardLabel = ttk.Label(frame8, text="Credit Card Type(if any):")
creditcardLabel.grid(column=0, row=1, pady=20)

visa = Radiobutton(frame8, text="Visa")
visa.grid(column=1, row=1)

mastercard = Radiobutton(frame8, text="Mastercard")
mastercard.grid(column=2, row=1)
'''------------------------------------------------------'''

roomtypeLabel = ttk.Label(frame9, text="Room Type:")
roomtypeLabel.grid(column=0, row=0)

normal = Radiobutton(frame9, text="Normal")
normal.grid(column=1, row=0)

familiar = Radiobutton(frame9, text="Familiar")
familiar.grid(column=1, row=1)

special = Radiobutton(frame9, text="Special")
special.grid(column=1, row=2)

totalLabel = ttk.Label(frame9, text="Total Staying Time(days):")
totalLabel.grid(column=2, row=0, padx=20)

totalEntry = ttk.Entry(frame9, width=5)
totalEntry.grid(column=3, row=0)

'''-------------------------------------------------------'''

button = ttk.Button(frame10, text="Submit",).grid(column=1, row=0)

frame4xd = ttk.Label(frame6, text="")
frame4xd.grid(column=0, row=0, padx=50)

frame4xd= ttk.Label(frame10, text="")
frame4xd.grid(column=0, row=0, padx=50)    
  
raiz.mainloop()

