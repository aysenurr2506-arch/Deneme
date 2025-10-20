from turtle import *
from colorways import *
tracer(100)

b = "black"
bgcolor(b)
h = 0

for i in range(520):
    # Renk değerini ayarla
    h += 0.0025 
    
    # Kalem rengini, h değerine göre dinamik olarak ayarla
    pencolor(hsv_to_rgb(h, 1, 1))
    
    # Dolgu rengini ayarla (İç şekli hangi renkle dolduracağını belirtir)
    fillcolor(hsv_to_rgb(h, 1, 0.8)) # Parlaklığı biraz düşürdük
    
    begin_fill()
    
    # 5 köşeli bir şekil çiz
    for j in range(5):
        forward(150)
        right(150)
        forward(150)
        left(150)
        right(360/5) # 72 derece dön
        
    end_fill() # Şekli doldurmayı bitir

    right(2) # Bir sonraki şekil için 2 derece dön

hideturtle()
done()
