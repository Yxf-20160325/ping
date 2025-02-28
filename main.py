import tkinter as tk
import subprocess as sp
root = tk.Tk()
root.title("ping工具")
root.geometry("600x600")
label = tk.Label(root, text="ip:")
label.pack()
entry = tk.Entry(root)
entry.pack()
label2 = tk.Label(root,text="参数:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()
def kill_python():
 # 关闭 python.exe 窗口的命令
 command = "taskkill /f /im python.exe"
 sp.Popen(command, shell=True)

def ping():
	if entry2.get() == "":
		sp.Popen("ping "+entry.get())
	else:
         sp.Popen("ping "+entry.get() + " " + entry2.get())
buuton = tk.Button(root,text="ping",command=ping)
buuton.pack()
button2 = tk.Button(root,text="关闭",command=lambda:root.destroy())
button2.pack()
root.mainloop()
