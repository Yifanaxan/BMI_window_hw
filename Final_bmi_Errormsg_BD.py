import tkinter as tk
from tkinter import ttk
import datetime

class Window(tk.Tk): 
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        ttkStyle = ttk.Style()
        ttkStyle.theme_use('default') 
        
        ttkStyle.configure('back.TFrame',background="#AFDCEC")
        ttkStyle.configure('gridLabel.TLabel',font=('Helvetica', 11,'bold'),foreground='#666666',background="#AFDCEC")
        ttkStyle.configure('gridEntry.TEntry',font=('Helvetica', 10,'bold'),background="#82CAFF")
        ttkStyle.configure('gridbtn.TButton',font=('Helvetica', 9,'bold'),foreground='#82CAFF',background="#488AC7")
        ttkStyle.configure('gridtext.TText',font=('Helvetica', 10,'bold'),foreground='#666666')
        ttkStyle.configure('gridex.TLabel',font=('Helvetica', 9,'bold'),foreground='#666666',background="#AFDCEC")
        
        mainFrame = ttk.Frame((self),style='back.TFrame',padding=10)        
        mainFrame.pack(expand=True,fill=tk.BOTH)
        
#第一個pack
        topFrame = ttk.Frame(mainFrame,style='back.TFrame')
        topFrame.pack(fill=tk.X)
        ttk.Label(topFrame,text="快看自己的BMI是否在理想範圍吧!",foreground='#488AC7',style='gridLabel.TLabel').pack(padx=20)

#2*3 grid
        firstFrame = ttk.Frame(mainFrame,style='back.TFrame',padding=10)
        firstFrame.pack(expand=True,fill=tk.BOTH)

        firstFrame.columnconfigure(0,weight=1) 
        firstFrame.columnconfigure(1,weight=1) 
        firstFrame.columnconfigure(2,weight=1) 
        firstFrame.rowconfigure(0,weight=1,pad=20) 
#Entry輸入姓名
        ttk.Label(firstFrame,text='姓名:',style='gridLabel.TLabel').grid(column=0,row=0,sticky=tk.E,padx=(0,0))
        self.name_entry=ttk.Entry(firstFrame,width=15)
        self.name_entry.grid(column=1,row=0,sticky=tk.W,padx=(10,0))
        ttk.Label(firstFrame,text='(ex:  徐大帥)',style='gridex.TLabel').grid(column=2,row=0,sticky=tk.W,padx=(0,100))
#Entry輸入生日
        ttk.Label(firstFrame,text='生日:',style='gridLabel.TLabel').grid(column=0,row=1,sticky=tk.E)
        self.bd_entry=ttk.Entry(firstFrame,width=15)
        self.bd_entry.grid(column=1,row=1,sticky=tk.W,padx=(10,0))
        ttk.Label(firstFrame,text='(ex:  1996/1/16)',style='gridex.TLabel').grid(column=2,row=1,sticky=tk.W,padx=(0,100))

#4x4 grid
        secFrame = ttk.Frame(mainFrame,style='back.TFrame')
        secFrame.pack(expand=True,fill=tk.BOTH)

        secFrame.columnconfigure(0,weight=1) 
        secFrame.columnconfigure(1,weight=1) 
        secFrame.columnconfigure(2,weight=1) 
        secFrame.columnconfigure(3,weight=1)
        secFrame.rowconfigure(1,weight=1,pad=10) 
        secFrame.rowconfigure(3,weight=1,pad=10) 
#Entry輸入身高
        ttk.Label(secFrame,text='身高:',style='gridLabel.TLabel').grid(column=0,row=0,sticky=tk.E,padx=(10,0))
        self.height_entry=ttk.Entry(secFrame,width=10)
        self.height_entry.grid(column=1,row=0,sticky=tk.W,padx=(10,0))
        ttk.Label(secFrame,text='cm   (ex: 188 cm)',style='gridex.TLabel').grid(column=2,row=0,sticky=tk.W,padx=(0,20))
        
#Entry輸入體重
        ttk.Label(secFrame,text='體重:',style='gridLabel.TLabel').grid(column=0,row=1,sticky=tk.E)
        self.weight_entry=ttk.Entry(secFrame,width=10)
        self.weight_entry.grid(column=1,row=1,sticky=tk.W,padx=(10,0))
        ttk.Label(secFrame,text='kg   (ex: 80 kg)',style='gridex.TLabel').grid(column=2,row=1,sticky=tk.W)
#計算按鈕
        calcbtn = ttk.Button(secFrame,text="開始計算",style='gridbtn.TButton',command=self.bmi)
        calcbtn.grid(column=3,row=0,padx=(0,30))
#清除按鈕
        delbtn = ttk.Button(secFrame,text="清除重算",style='gridbtn.TButton',command=self.clear)
        delbtn.grid(column=3,row=1,padx=(0,30))
        
        ttk.Label(secFrame,text="你的BMI為    ",style='gridLabel.TLabel').grid(column=1,row=2,columnspan=2)

#顯示BMI計算結果
        self.messageText = tk.Text(secFrame,height=1,width=45,state=tk.DISABLED,background="#82CAFF",font=('Helvetica', 13,'bold'),foreground='#666666')
        self.messageText.grid(column=0,row=3,columnspan=4)

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
                if height< 0:
                    raise ValueError("Invalid height")
                if weight< 0:
                    raise ValueError("Invalid weight")
                
                date = datetime.datetime.strptime(self.bd_entry.get(), '%Y/%m/%d')
                if date.year < 1900 :
                    raise ValueError("Invalid date1")
                if date.year > datetime.datetime.now().year:
                    raise ValueError("Invalid date2")

        except ValueError as e:
                if "height" in str(e):
                        ERRORmessage = "豬頭! 身高有負的嗎?!"
                elif "weight" in str(e):
                        ERRORmessage = "豬頭! 體重負的? 你住月球阿!?"
                elif "date1" in str(e):
                        ERRORmessage = "請問您是祖先嗎?"
                elif "date2" in str(e):
                        ERRORmessage = "請問您是尚未出生嗎?"
                else:
                        ERRORmessage = "豬頭! 身高or體重or日期的格式有誤!!"
                self.messageText.configure(state=tk.NORMAL)
                self.messageText.delete('1.0', tk.END)
                self.messageText.tag_configure("center", justify='center')
                self.messageText.insert(tk.END, ERRORmessage,"center")
                self.messageText.configure(state=tk.DISABLED)
                return
        
        bmi = weight / ((height/100) ** 2)

        if bmi < 18.5:
             bmi_msg= "你太輕囉! 多吃一點!!"
        elif bmi <24:
             bmi_msg= "恭喜你~~BMI完美!!"
        elif bmi <27:
             bmi_msg= "哇~最近是不是有點放縱了!!"
        elif bmi <30:
             bmi_msg= "嗯~~該忌口囉!!"
        elif bmi <35:
             bmi_msg= "少吃點~~而且該上健身房囉!!"
        else:
             bmi_msg= "健康亮紅燈囉!放下手上那塊雞排!!"
             
        self.messageText.configure(state=tk.NORMAL)
        self.messageText.delete('1.0',tk.END)
        self.messageText.tag_configure("center", justify='center')
        self.messageText.insert(tk.END, f"{bmi:.1f}  {bmi_msg}","center")
        self.messageText.configure(state=tk.DISABLED)

    def clear(self):
        self.name_entry.delete(0, tk.END)
        self.bd_entry.delete(0, tk.END)
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