CSI = '\x1b['
RESET = f'{CSI}0m'

def make_diagram():
    correct_positive = [] # список для чисел от 5 до 10
    correct_negative = [] # список для чисел от -10 до -5
    with open('sequence.txt') as f:
        all_numbers = [float(i) for i in f]
        for number in all_numbers:
            if (number >= 5 and number <= 10):
                correct_positive.append(number)
            elif number >= -10 and number <= -5:
                correct_negative.append(number)
    count = len(correct_negative) + len(correct_positive) # количество всех нужных чисел
    correct_pos_perc = int(round((len(correct_positive) / count), 2) * 100) # процент чисел от 5 до 10
    correct_neg_perc = int(round((len(correct_negative) / count), 2) * 100) # процент чисел от -10 до -5

    print(f'Числа от 5 до 10:   {CSI}45m{" "*(correct_pos_perc//2)}{RESET}{correct_pos_perc}%')
    print(f'Числа от -10 до -5: {CSI}46m{" "*(correct_neg_perc//2)}{RESET}{correct_neg_perc}%')

    


if __name__ == '__main__':
    make_diagram()