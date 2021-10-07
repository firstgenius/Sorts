from random import randint

def random_generator_lst(n):
    gen_lst = []
    for i in range(n):
        gen_lst.append(randint(-100000, 100000))
    return gen_lst

def increase_generator_lst(n):
    gen_lst = []
    for i in range(n):
        gen_lst.append(i)
    return gen_lst

def decrease_generator_lst(n):
    gen_lst = []
    for i in range(n, 0, -1):
        gen_lst.append(i)
    return gen_lst

def repeated_generator_lst(n):
    gen_lst = []
    for i in range(n):
        gen_lst.append(randint(1, 3))
    return gen_lst

def main_genertor(index, number):
    if index == 0:
        return random_generator_lst(number)
    elif index == 1:
        return increase_generator_lst(number)
    elif index == 2:
        return decrease_generator_lst(number)
    else:
        return repeated_generator_lst(number)

if __name__ == '__main__':
    print(repeated_generator_lst(2**3))
