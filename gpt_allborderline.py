import tkinter as tk

# 创建主窗口
root = tk.Tk()

# 创建表格小部件
table = tk.Frame(root, bg="white", bd=1, relief="solid")
table.pack(side="top", fill="both", expand=True)

# 定义表格的大小
rows = 4
cols = 4

# 创建所有单元格
cells = []
for i in range(rows):
    row_cells = []
    for j in range(cols):
        cell = tk.Label(table, text=f"Row {i+1}, Col {j+1}", bg="white", bd=1, relief="solid")
        cell.grid(row=i, column=j, sticky="nsew")
        row_cells.append(cell)
    cells.append(row_cells)

# 绘制所有单元格的边框
for i in range(rows):
    for j in range(cols):
        # 绘制左边框
        if j == 0:
            cells[i][j].config(bd=1, relief="solid")
        # 绘制上边框
        if i == 0:
            cells[i][j].config(bd=1, relief="solid")

# 设置所有单元格的权重
for i in range(rows):
    table.rowconfigure(i, weight=1)
for j in range(cols):
    table.columnconfigure(j, weight=1)

# 启动主事件循环
root.mainloop()