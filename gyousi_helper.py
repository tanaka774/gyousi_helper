import winsound
import random
import time

bisuke = ['gyoooou_Trim_m.wav', 'gyoudekiru.wav', 'iikoto_m.wav', 'nanibosa.wav'] 
blank = [10,15,20,25] #10～25秒間隔で再生

count = 0

while True:

    with open(random.choice(bisuke), 'rb') as f: #音声の中からランダムに一つ選ぶ
        data = f.read()
    
    winsound.PlaySound(data, winsound.SND_MEMORY)

    print('== WARNING %s ==' % count)
    time.sleep(random.choice(blank)) #ランダムで間隔を空ける
    count = count+1
    if count == 600:
        break