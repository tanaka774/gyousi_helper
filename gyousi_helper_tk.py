import tkinter
import winsound
import random
import time

start_flag = False

bisuke = ['gyoooou_Trim_m.wav', 'gyoudekiru.wav', 'iikoto_m.wav', 'nanibosa.wav'] 
blank = [10,15,20,25] #10～25秒間隔で再生


#limit = 1000
# タイマー
def timer(count):
    global label, app
    global start_flag

    if start_flag: #and count <= limit
        label.config(text=count)
        app.after(1000, timer, count + 1)
        
def warning():
    
    global bisuke
    if start_flag: # and count <= limit    
        with open(random.choice(bisuke), 'rb') as f: #音声の中からランダムに一つ選ぶ
            data = f.read()

        winsound.PlaySound(data, winsound.SND_MEMORY)
        app.after(random.choice(blank) * 1000, warning)


# スタートボタンが押された時の処理
def start_button_click(event):
    global app
    global start_flag
    start_flag = True

    app.after(1000, timer, 1)
    app.after(random.choice(blank) * 1000, warning)

# ストップボタンが押された時の処理
def stop_button_click(event):
    global start_flag
    start_flag = False

# メインウィンドウを作成
app = tkinter.Tk()
app.title("ギョウシヘルパー")
app.geometry("200x100")

# ボタンの作成と配置
start_button = tkinter.Button(
    app,
    text="スタート",
)
start_button.pack()

stop_button = tkinter.Button(
    app,
    text="ストップ",
)
stop_button.pack()


# ラベルの作成と配置
label = tkinter.Label(
    app,
    width=5,
    height=1,
    text=0,
    font=("", 20)
)
label.pack()

# イベント処理の設定
start_button.bind("<ButtonPress>", start_button_click)
stop_button.bind("<ButtonPress>", stop_button_click)

# メインループ
app.mainloop()