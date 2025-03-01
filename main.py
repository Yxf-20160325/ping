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
 command2 = "taskkill /f /im ping.exe"
 sp.Popen(command, shell=True)
 sp.Popen(command2, shell=True)

def ping():
	if entry2.get() == "":
		sp.Popen("ping "+entry.get())
	else:
         sp.Popen("ping "+entry.get() + " " + entry2.get())
def kill_ping():
	command3 = "taskkill /f /im ping.exe"
	sp.Popen(command3, shell=True)
buuton = tk.Button(root,text="ping",command=ping)
buuton.pack()
button2 = tk.Button(root,text="停止ping",command=lambda:kill_ping())
button2.pack()
button3 = tk.Button(root,text="关闭并停止ping",command=lambda:kill_python())
button3.pack()
root.mainloop()
