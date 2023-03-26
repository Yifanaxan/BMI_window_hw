import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):  #以下四行必打
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        ttkStyle = ttk.Style()
        ttkStyle.theme_use('default') 

        ttkStyle.configure('gridLabel.TLabel',font=('Helvetica', 10,'bold'),foreground='#666666')
        ttkStyle.configure('gridEntry.TEntry',font=('Helvetica', 10,'bold'))
        ttkStyle.configure('gridbtn.TButton',font=('Helvetica', 10,'bold'),foreground='#666666')
        ttkStyle.configure('gridtext.TText',font=('Helvetica', 10,'bold'),foreground='#666666')
        
        mainFrame = ttk.Frame(self)#,style='back.TFrame')        
        mainFrame.pack(expand=True,fill=tk.BOTH,padx=20,pady=20)
        
#第一個pack
        topFrame = ttk.Frame(mainFrame)
        topFrame.pack(fill=tk.X)
        ttk.Label(topFrame,text="快看自己的BMI是否在理想範圍吧!",foreground='#38ACEC',font=('Helvetica', 12,'bold')).pack(pady=20,padx=20)
         
#4x4 grid
        secFrame = ttk.Frame(mainFrame)
        secFrame.pack(expand=True,fill=tk.BOTH)

        secFrame.columnconfigure(0,weight=1) 
        secFrame.columnconfigure(1,weight=1) 
        secFrame.columnconfigure(2,weight=1) 
        secFrame.columnconfigure(3,weight=1)
        secFrame.rowconfigure(1,weight=1,pad=20) 
        secFrame.rowconfigure(3,weight=1,pad=20) 
#Entry輸入身高
        ttk.Label(secFrame,text='身高:',style='gridLabel.TLabel').grid(column=0,row=0,sticky=tk.E)
        self.height_entry=ttk.Entry(secFrame,style='gridEntry.TEntry',width=10)
        self.height_entry.grid(column=1,row=0,sticky=tk.W+tk.E,padx=10)
#Entry輸入體重
        ttk.Label(secFrame,text='體重:',style='gridLabel.TLabel').grid(column=0,row=1,sticky=tk.E)
        self.weight_entry=ttk.Entry(secFrame,style='gridEntry.TEntry',width=10)
        self.weight_entry.grid(column=1,row=1,sticky=tk.W+tk.E,padx=10)

        ttk.Label(secFrame,text='cm',style='gridLabel.TLabel').grid(column=2,row=0,sticky=tk.W)
        ttk.Label(secFrame,text='kg',style='gridLabel.TLabel').grid(column=2,row=1,sticky=tk.W)
#計算按鈕
        calcbtn = ttk.Button(secFrame,text="開始計算",style='gridbtn.TButton',command=self.bmi)
        calcbtn.grid(column=3,row=0,padx=30)
#清除按鈕
        delbtn = ttk.Button(secFrame,text="清除重算",style='gridbtn.TButton',command=self.clear)
        delbtn.grid(column=3,row=1,padx=30)
        
        ttk.Label(secFrame,text="你的BMI為    ",font=('Helvetica', '10','bold'),foreground='#666666').grid(column=1,row=2,padx=10,columnspan=2,sticky=tk.E)
#顯示BMI計算結果
        self.messageText = tk.Text(secFrame,height=1,width=13,state=tk.DISABLED,background="#82CAFF",font=('Helvetica', 13,'bold'),foreground='#666666')
        self.messageText.grid(column=1,row=3,columnspan=2,sticky=tk.E)

#8x3 grid BMI參照表
        ttkStyle.configure('thdFrame.TFrame',borderwidth=1, relief='solid')
        thdFrame = ttk.Frame(mainFrame,style='thdFrame.TFrame')
        thdFrame.pack(expand=True,fill=tk.BOTH)

        thdFrame.columnconfigure(0,weight=1,pad=20) 
        thdFrame.columnconfigure(1,weight=1,pad=20) 
        thdFrame.columnconfigure(2,weight=1,pad=20) 
        thdFrame.rowconfigure(0,weight=1,pad=10) 
        thdFrame.rowconfigure(1,weight=1,pad=10) 
        thdFrame.rowconfigure(2,weight=1,pad=10) 
        thdFrame.rowconfigure(3,weight=1,pad=10) 
        thdFrame.rowconfigure(4,weight=1,pad=10) 
        thdFrame.rowconfigure(5,weight=1,pad=10) 
        thdFrame.rowconfigure(6,weight=1,pad=10) 
        thdFrame.rowconfigure(7,weight=1,pad=10) 

        ttkStyle.configure('gridLabelR1.TLabel',font=('Helvetica', 10,'bold'),anchor='center',background='#66cdaa',foreground='#666666')
        ttkStyle.configure('gridLabelR2.TLabel',font=('Helvetica', 10,'bold'),anchor='center',background='#e0ffff',foreground='#666666')
        ttkStyle.configure('gridLabelR3.TLabel',font=('Helvetica', 10,'bold'),anchor='center',background='#87cefa',foreground='#666666')
        ttkStyle.configure('gridLabelR4.TLabel',font=('Helvetica', 10,'bold'),anchor='center',background='#ffb6c1',foreground='#666666')
        ttkStyle.configure('gridLabelfont.TLabel',font=('Helvetica', 10,'bold'),anchor='center',foreground='#ffffff',wrap='word', wraplength=150)
        
        ttk.Label(thdFrame,style='gridLabelR1.TLabel').grid(row=0,column=0,sticky="NSEW")
        ttk.Label(thdFrame,style='gridLabelR1.TLabel').grid(row=1,column=0,sticky="NSEW")
        ttk.Label(thdFrame,text='身體質量指數(BMI)',style='gridLabelR1.TLabel').grid(row=0,column=1,sticky="NSEW")
        ttk.Label(thdFrame,text='腰圍',style='gridLabelR1.TLabel').grid(row=0,column=2,sticky="NSEW")
        ttk.Label(thdFrame,text='(kg/m2)',style='gridLabelR1.TLabel').grid(row=1,column=1,sticky="NSEW")
        ttk.Label(thdFrame,text='(cm)',style='gridLabelR1.TLabel').grid(row=1,column=2,sticky="NSEW")

        ttk.Label(thdFrame,text='(體重過輕)',style='gridLabelR2.TLabel').grid(row=2,column=0,sticky="NSEW")
        ttk.Label(thdFrame,text='(BMI < 18.5)',style='gridLabelR2.TLabel').grid(row=2,column=1,sticky="NSEW")
        ttk.Label(thdFrame,text='--',style='gridLabelR2.TLabel').grid(row=2,column=2,sticky="NSEW")

        ttk.Label(thdFrame,text='(正常範圍)',style='gridLabelR3.TLabel').grid(row=3,column=0,sticky="NSEW")
        ttk.Label(thdFrame,text='(18.5<=BMI<24)',style='gridLabelR3.TLabel').grid(row=3,column=1,sticky="NSEW")
        ttk.Label(thdFrame,text='--',style='gridLabelR3.TLabel').grid(row=3,column=2,sticky="NSEW")

        ttk.Label(thdFrame,text='(異常範圍)',style='gridLabelR4.TLabel').grid(row=4,column=0,rowspan=4,sticky="NSEW")
        ttk.Label(thdFrame,text='(過重 : 24<=BMI<27)',style='gridLabelfont.TLabel',background='#F98B88').grid(row=4,column=1,sticky="NSEW")
        ttk.Label(thdFrame,text='(輕度肥胖 : 27<=BMI<30)',style='gridLabelfont.TLabel',background='#F08080').grid(row=5,column=1,sticky="NSEW")
        ttk.Label(thdFrame,text='(中度肥胖 : 30<=BMI<35)',style='gridLabelfont.TLabel',background='#F67280').grid(row=6,column=1,sticky="NSEW")
        ttk.Label(thdFrame,text='(重度肥胖 : BMI>=35)',style='gridLabelfont.TLabel',background='#F75D59').grid(row=7,column=1,sticky="NSEW")
        ttk.Label(thdFrame,style='gridLabelR4.TLabel').grid(row=4,column=2,sticky="NSEW")
        ttk.Label(thdFrame,text='(男性 : >= 90公分)',style='gridLabelR4.TLabel').grid(row=5,column=2,sticky="NSEW")
        ttk.Label(thdFrame,text='(女性 : >= 80公分)',style='gridLabelR4.TLabel').grid(row=6,column=2,sticky="NSEW")
        ttk.Label(thdFrame,style='gridLabelR4.TLabel').grid(row=7,column=2,sticky="NSEW")

    def bmi(self):
        try:
                height = float(self.height_entry.get())
                weight = float(self.weight_entry.get())
                if height < 0 or weight < 0:
                     raise ValueError
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

    def clear(self):
        self.height_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.messageText.configure(state=tk.NORMAL)
        self.messageText.delete('1.0', tk.END)
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