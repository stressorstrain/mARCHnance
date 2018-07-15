import tkinter as tk
import subprocess


class GUI:
    def __init__(self, master):
        self.path = "/home/guibax/Programs/ARCH_MAINTENANCE/marchnance"
        self.f = "failed"
        self.c = "connect"
        self.log = "logs"
        self.m = Methods

        # Frames
        self.frame = tk.Frame(
                                                master,  bg="black", bd=10,
                                                highlightbackground="royal blue", highlightthickness=1
                                                )
        self.bt_frame = tk.Frame(self.frame, bg="black")
        self.txt_frame = tk.Frame(self.frame, bg="black")

        # Text
        self.txt1 = tk.Text(self.txt_frame, height=25, width=105)

        # Buttons
        self.bt1 = tk.Button(
            self.bt_frame, text="Check Failed Services", bg="black",
            fg="white", width=16, command=lambda: self.commands(self.f),
            highlightbackground="royal blue", highlightthickness=1
            )

        self.bt2 = tk.Button(
            self.bt_frame, text="Check Connection", bg="black", fg="white",
            width=16, command=lambda: self.commands(self.c),
            highlightbackground="royal blue", highlightthickness=1
            )

        self.bt3 = tk.Button(
             self.bt_frame, text="Check Error Logs ", bg="black", fg="white",
             width=16, command=lambda: self.commands(self.log),
             highlightbackground="royal blue", highlightthickness=1
            )

        self.bt4 = tk.Button(
             self.bt_frame, text="Clear ", bg="black", fg="white",
             highlightbackground="royal blue", highlightthickness=1,
             width=16, command=self.clear_text
         )

        self.bt5 = tk.Button(
             self.bt_frame, text="Backup ", bg="black", fg="white",
             width=16, command=self.m,
             highlightbackground="royal blue", highlightthickness=1
            )

        # Placing
        self.frame.grid()
        self.bt_frame.grid(row=0, column=0, pady=10, sticky='N')
        self.txt_frame.grid(row=0, column=1)
        self.txt1.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="E")
        self.bt1.grid(row=0, column=0)
        self.bt2.grid(row=1, column=0, pady=10)
        self.bt3.grid(row=2, column=0)
        self.bt4.grid(row=4, column=0, pady=10)
        self.bt5.grid(row=3, column=0, pady=10)

    def commands(self, command):

        if command == "failed":
            result = subprocess.run(['systemctl', '--failed'], stdout=subprocess.PIPE).stdout.decode('utf-8')
            result_splited = str(result).split("LOAD")[1]
            self.txt1.insert('1.0', result_splited)

        elif command == "connect":
            connect = subprocess.run(['ping', '-c2', 'archlinux.org'], stdout=subprocess.PIPE).stdout.decode('utf-8')
            self.txt1.insert('end', connect)

        elif command == "logs":
            logs = subprocess.run(['journalctl', '-p', '3', '-xb'], stdout=subprocess.PIPE).stdout.decode('utf-8')
            logs_splited = str(logs).split("--")[2]
            self.txt1.insert('end', logs_splited)

    def clear_text(self):
        self.txt1.delete('1.0', 'end')


class Methods:
    def __init__(self):
        self.root2 = tk.Tk()
        self.root2.title("Backuper")

        self.root2.resizable(0, 0)

        self.bp_frame = tk.Frame(self.root2, bg='black')

        self.from_lb = tk.Label(self.bp_frame, text="Folder to Backup:", bg='black', fg='white')
        self.to_lb = tk.Label(self.bp_frame, text="Destination Path: ", bg="black", fg="white")

        self.from_entry = tk.Entry(self.bp_frame)
        self.to_entry = tk.Entry(self.bp_frame)

        self.go_bu = tk.Button(
                                self.bp_frame, text='DO IT!', bg='black', fg='white', width=2, height=1,
                                command=lambda: self.backup(self.from_entry, self.to_entry)
                                                )
        self.from_lb.grid(row=0, column=0, sticky='w')
        self.to_lb.grid(row=0, column=1, sticky='w')
        self.from_entry.grid(row=1, column=0)
        self.to_entry.grid(row=1, column=1)
        self.bp_frame.grid(row=0, column=0)
        self.go_bu.grid(row=1, column=2, padx=(3, 3))
        self.root2.mainloop()

    def backup(self, from_entry, to_entry):
        from_path = from_entry.get()
        to_path = to_entry.get()
        f_st = str(from_path)
        t_st = str(to_path)

        back_up = subprocess.run(
                                ["rsync", "-v",  f_st, t_st],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')
        g.txt1.delete('1.0', 'end')
        g.txt1.insert('1.0', back_up)
        self.root2.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    photo = tk.PhotoImage(file="/home/guibax/Programs/ARCH_MAINTENANCE/marchnance/maintenance.gif")
    root.tk.call('wm', 'iconphoto', root._w, photo)
    root.title('ARCH MAINTENANCE')
    root.resizable(0, 0)
    g = GUI(root)
    root.mainloop()
