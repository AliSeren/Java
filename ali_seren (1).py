from tkinter import *
class Ali_0:
    def __init__(self):
        self.ali_1 = Tk()
        self.ali_1.title('TÜRKİYE - ŞEHİRLER')
        
        self.ali_2=open("sehirler.txt",'r')
        self.ali_4={ali_3.split(',')[1].rstrip()  for ali_3 in self.ali_2}
        self.ali_2.close()
        
        self.ali_5=list(self.ali_4)
        self.ali_5.sort()
        
        Label(self.ali_1, text="Kısaltma").grid(row=0, column=0)
        
        self.ali_6 = StringVar()
        self.ali_7 = Listbox(self.ali_1,width=20,height=len(self.ali_5),listvariable=self.ali_6)
        self.ali_7.grid(row=1,column=0)
        self.ali_6.set(tuple(self.ali_5))
        
        
        Label(self.ali_1, text="Şehir Adı:").grid(row=0, column=1)
        self.ali_7 = StringVar()
        self.ali_8 = Entry(self.ali_1, textvariable=self.ali_7, state="disabled")
        self.ali_8.grid(row=1, column=1)
        
        
        Label(self.ali_1, text="Nesi Meşhur:").grid(row=2, column=1)
        self.ali_9 = StringVar()
        self.ali_10 = Entry(self.ali_1, textvariable=self.ali_9, state="disabled")
        self.ali_10.grid(row=3, column=1)
        
        
        Label(self.ali_1, text="Bölgesi:").grid(row=4, column=0)
        self.ali_11 = StringVar()
        self.ali_12 = Entry(self.ali_1, textvariable=self.ali_11, state="disabled")
        self.ali_12.grid(row=4, column=1)
        
        Label(self.ali_1, text="Plaka Kodu:").grid(row=5, column=0)
        self.ali_13 = StringVar()
        self.ali_14 = Entry(self.ali_1, textvariable=self.ali_13, state="disabled", width=4)
        self.ali_14.grid(row=5, column=1)
        
        
        
        
        self.ali_1.mainloop()
        
    def ali_11(self,e):
            ali_12=self.ali_7.get(self.ali_7.curselection())
            ali_13=open("sehirler.txt","r")
            
            ali_14 = []
            for ali_15 in ali_13:
                ali_15 = ali_15.split(',')
                if ali_12 == ali_15[1]:
                    ali_14 = ali_15 
                    break
            
            self.ali_7.set(ali_14[0])
            self.ali_9(ali_14[3])
            self.ali_11(ali_14[2])
            self.ali_13(ali_14[4])
        
        
Ali_0()