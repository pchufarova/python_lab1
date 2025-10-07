import time
CSI = '\x1b['
RESET = f'{CSI}0m'
RED = f'{CSI}41m'
BROWN = f'{CSI}48:5:52m'
BLACK = f'{CSI}40m'

def draw_heart():
    color1 = color2 = color3 = RED # переменные для смены цветов сердца
    block = "  " # для нормального изображения сердечка
    text = '' # переменная для вывода game over в конце
    counter = 0 
    while True: #ниже отрисовка сердечка, переменные color меняют цвет взависимиости от значения counter
        print(f'{2*block}{CSI}{BROWN}{4*block}{RESET}{3*block}{CSI}{BROWN}{4*block}{RESET}', flush=True)
        print(f'{block}{BROWN}{block}{color1}{4*block}{BROWN}{block}{RESET}{block}{BROWN}{block}{color1}{4*block}{BROWN}{block}{RESET}', flush=True)
        print(f'{BROWN}{block}{color1}{6*block}{BROWN}{block}{color1}{6*block}{BROWN}{block}{RESET}', flush=True)
        for i in range(2):
            print(f'{BROWN}{block}{color2}{13*block}{BROWN}{block}{RESET}', flush=True)
        for i in range(2):
            print(f'{block}{BROWN}{block}{color2}{11*block}{BROWN}{block}{RESET}', flush=True)
        for i in range(5):
            print(f'{(2+i)*block}{BROWN}{block}{color3}{block*(9-2*i)}{BROWN}{block}{RESET}', flush=True)
        print(f'{block*7}{BROWN}{block}{RESET}\n{text}{RESET}', flush=True)
        print(f"{CSI}14A", end="")
        print(f"{CSI}30D", end="")
        time.sleep(0.9)
        if counter == 0:
            color1 = BLACK
            counter += 1
        elif counter == 1:
            color2 = BLACK
            counter += 1
        elif counter == 2:
            color3 = BLACK
            text = 'G A M E  O V E R' # выводится когда сердце становится пустым
            counter += 1
        elif counter == 3:
            color1 = RED
            color2 = RED
            color3 = RED
            text = ' '*30
            counter = 0


if __name__ == '__main__':
    draw_heart()
