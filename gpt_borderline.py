import tkinter as tk

# 创建主窗口
root = tk.Tk()

# 创建 Canvas 小部件
canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

# 定义单元格的宽度和高度
cell_width = 100
cell_height = 30

# 绘制所有单元格的框线
for i in range(3):
    for j in range(3):
        x1 = i * cell_width
        y1 = j * cell_height
        x2 = x1 + cell_width
        y2 = y1 + cell_height
        canvas.create_rectangle(x1, y1, x2, y2, outline="black", width=1)

# 在单元格中添加文本
canvas.create_text(cell_width/2, cell_height/2, text="Cell 1,1")
canvas.create_text(cell_width/2 + cell_width, cell_height/2, text="Cell 1,2")
canvas.create_text(cell_width/2 + 2*cell_width, cell_height/2, text="Cell 1,3")

canvas.create_text(cell_width/2, cell_height/2 + cell_height, text="Cell 2,1")
canvas.create_text(cell_width/2 + cell_width, cell_height/2 + cell_height, text="Cell 2,2")
canvas.create_text(cell_width/2 + 2*cell_width, cell_height/2 + cell_height, text="Cell 2,3")

canvas.create_text(cell_width/2, cell_height/2 + 2*cell_height, text="Cell 3,1")
canvas.create_text(cell_width/2 + cell_width, cell_height/2 + 2*cell_height, text="Cell 3,2")
canvas.create_text(cell_width/2 + 2*cell_width, cell_height/2 + 2*cell_height, text="Cell 3,3")

# 启动主事件循环
root.mainloop()