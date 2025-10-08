CSI = '\x1b['
RESET = f'{CSI}0m'

def draw_finland_flag():
    block = " " # для отрисовки флага
    for i in range(4):
        print(f'{CSI}47m{block*10}{CSI}44m{block*6}{CSI}47m{block*25}{RESET}')
    for i in range(3):
        print(f'{CSI}44m{block*41}{RESET}')
    for i in range(4):
        print(f'{CSI}47m{block*10}{CSI}44m{block*6}{CSI}47m{block*25}{RESET}')

        
if __name__ == "__main__":
    draw_finland_flag()