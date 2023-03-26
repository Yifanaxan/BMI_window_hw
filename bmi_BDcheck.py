import tkinter as tk
from tkinter import ttk
import datetime

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        ttkStyle = ttk.Style()
        ttkStyle.theme_use('default')
        ttkStyle.configure('top.TFrame',background='#659EC7')
        ttkStyle.configure('bot.TFrame',background='black')
        ttkStyle.configure('gridLabel.TLabel',font=('Helvetica', 16),foreground='#666666')
        ttkStyle.configure('gridEntry.TEntry',font=('Helvetica', 16))
        
        mainFrame = ttk.Frame(self,style='top.TFrame',padding=10)        
        mainFrame.pack(expand=True,fill=tk.BOTH)
        
        topFrame = ttk.Frame(mainFrame,height=100)
        topFrame.pack(fill=tk.X)

        ttk.Label(topFrame,text="BMI試算",font=('Helvetica', '20')).pack(pady=20)

        bottomFrame = ttk.Frame(mainFrame)
        bottomFrame.pack(expand=True,fill=tk.BOTH)

        bottomFrame.columnconfigure(0,weight=1,pad=20) #第0欄，比重1
        bottomFrame.columnconfigure(1,weight=2,pad=20) #第1欄，比重2
        bottomFrame.rowconfigure(0,weight=1,pad=20) #第0行，比重1
        bottomFrame.rowconfigure(3,weight=1,pad=20) #第3行，比重1
        bottomFrame.rowconfigure(4,weight=1,pad=20) #第4行，比重1
        bottomFrame.rowconfigure(5,weight=1,pad=20) #第5行，比重1
        bottomFrame.rowconfigure(6,weight=1,pad=20) #第6行，比重1

        ttk.Label(bottomFrame,text='姓名:',style='gridLabel.TLabel').grid(column=0,row=0,sticky=tk.E)
        nameEnrty=ttk.Entry(bottomFrame,style='gridEntry.TEntry')
        nameEnrty.grid(column=1,row=0,sticky=tk.W,padx=10)

        ttk.Label(bottomFrame,text='出生年月日:',style='gridLabel.TLabel').grid(column=0,row=1,sticky=tk.E)
        ttk.Label(bottomFrame,text='(2000/03/01):',style='gridLabel.TLabel').grid(column=0,row=2,sticky=tk.E)
        self.bdEntry=ttk.Entry(bottomFrame,style='gridEntry.TEntry')
        self.bdEntry.grid(column=1,row=1,sticky=tk.W,rowspan=2,padx=10) 

        ttk.Label(bottomFrame,text='身高(cm):',style='gridLabel.TLabel').grid(column=0,row=3,sticky=tk.E)
        self.height_entry=ttk.Entry(bottomFrame,style='gridEntry.TEntry')
        self.height_entry.grid(column=1,row=3,sticky=tk.W,padx=10)

        ttk.Label(bottomFrame,text='體重(kg):',style='gridLabel.TLabel').grid(column=0,row=4,sticky=tk.E)
        self.weight_entry=ttk.Entry(bottomFrame,style='gridEntry.TEntry')
        self.weight_entry.grid(column=1,row=4,sticky=tk.W,padx=10)

        self.messageText = tk.Text(bottomFrame,height=5,width=35,state=tk.DISABLED)
        self.messageText.grid(column=0,row=5,sticky=tk.N+tk.S,columnspan=2)

        calcbtn = ttk.Button(bottomFrame,text="計算",command=self.bmi)
        calcbtn.grid(column=1,row=6,sticky=tk.W)

    def bmi(self):
        try:
                height = float(self.height_entry.get())
                weight = float(self.weight_entry.get())
                if height < 0 or weight < 0:
                    raise ValueError
                date = datetime.datetime.strptime(self.bdEntry.get(), '%Y/%m/%d')
                if date.year < 1900 or date.year > datetime.datetime.now().year:
                    raise ValueError('Invalid year')
        except ValueError:
                self.messageText.configure(state=tk.NORMAL)
                self.messageText.delete('1.0', tk.END)
                self.messageText.tag_configure("center", justify='center')
                self.messageText.insert(tk.END, "Invalid input","center")
                self.messageText.configure(state=tk.DISABLED)
                return
        
        bmi = weight / ((height/100) ** 2)
        self.messageText.configure(state=tk.NORMAL)
        self.messageText.delete('1.0',tk.END)
        self.messageText.tag_configure("center", justify='center')
        self.messageText.insert(tk.END, f"{bmi:.2f}","center")
        self.messageText.configure(state=tk.DISABLED)


def main():
    '''
    這是程式的執行點
    '''
    window = Window()
    window.title("BMI計算")
    #window.geometry("400x500")
    window.mainloop()

if __name__ == "__main__":
    main()