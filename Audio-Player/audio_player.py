import ttkbootstrap as tb
from tkinter import messagebox
import threading
from audio_config import version_number
from audio_class import Audio
from tkinter import filedialog

def play_music():
    def new_thread():
        e_msg.config(text="")

        try:
            file = entry.get()
            p.start()
            w.update_idletasks()
            play_button.config(text="Playing")

            Audio(file_path=file).play()
            p.stop()
            p["value"] = 100
            w.update_idletasks()
            play_button.config(text="Finished")
            play_button.config(text="Play audio")
        except Exception as err:
            e_msg.config(text=str(err))
            play_button.config(text="Play audio")
            p.stop()
            p["value"] = 0
            w.update_idletasks()
            messagebox.showerror(title="Audio Player", message=str(err))

    thread = threading.Thread(target=new_thread, name="audio_player", daemon=True)
    thread.start()

def play_music2():
    def new_thread():
        e_msg.config(text="")

        try:
            file = filedialog.askopenfilename(filetypes=(("Mp3 files", "*.mp3"), ("All files", "*.*")))
            p.start()
            w.update_idletasks()
            play_b.config(text="Playing from open file")

            Audio(file_path=file).play()
            p.stop()
            p["value"] = 100
            w.update_idletasks()
            play_b.config(text="Finished")
            play_b.config(text="Open mp3 file and play")
        except Exception as err:
            e_msg.config(text=str(err))
            play_b.config(text="Open mp3 file and play")
            p.stop()
            p["value"] = 0
            w.update_idletasks()
            messagebox.showerror(title="Audio Player", message=str(err))

    thread = threading.Thread(target=new_thread, name="audio_player2", daemon=True)
    thread.start()


w = tb.Window(themename="superhero")
w.title("Audio Player")
w.resizable(False, False)

#CENTER WINDOW
win_width = 800
win_height = 500
screen_width = w.winfo_screenwidth()
ycreen_height = w.winfo_screenheight()
x = int((screen_width / 2)-(win_width / 2))
y = int((ycreen_height / 2)-(win_height / 2))
w.geometry("{}x{}+{}+{}".format(win_width, win_height, x, y))


ver_num = tb.Label(w, text=version_number,
                 bootstyle="success",
                 font=("Aerial", 18))
ver_num.place(x=8, y=5)

title = tb.Label(w, text="Audio Player",
                 foreground="yellow",
                 font=("Impact", 28))
title.pack()

e = tb.Label(w, text="Enter the full path of the mp3 file",
             bootstyle="warning",font=("Impact", 28))
e.pack(pady=35)

msg = tb.Label(w, text="Make sure the path is \\\\ not / or just 1 single slash",
             bootstyle="white",font=("Impact", 13))
msg.pack()

entry = tb.Entry(w,
                 width=58,
                 bootstyle="primary",
                 font=("Aerial", 15),
                 foreground="yellow")
entry.pack()

e_msg = tb.Label(w, bootstyle="danger",font=("Impact", 13))
e_msg.pack()

s = tb.Style()
s.configure("success.TButton", font=("Impact", 15))

play_button = tb.Button(w, text="Play audio", command=play_music,
                        width=20,
                        style="success.TButton",
                        bootstyle="success")
play_button.pack(pady=18)

msg_or = tb.Label(w, text="Or", foreground="yellow",font=("Impact", 17))
msg_or.pack()

play_b = tb.Button(w, text="Open mp3 file and play", command=play_music2,
                        width=20,
                        style="success.TButton",
                        bootstyle="success")
play_b.pack(pady=18)

p = tb.Progressbar(w, value=0, maximum=100, bootstyle="success", length=600)
p.place(x=100, y=450)

w.mainloop()