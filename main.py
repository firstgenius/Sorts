from experiment_gener import random_generator_lst, increase_generator_lst, decrease_generator_lst, repeated_generator_lst, main_genertor
from sorts import insertion_sort, selection_sort, merge_sort, shell_sort
import time
from matplotlib import pyplot as plt

x = ['2^7', '2^8', '2^9', '2^10', '2^11', '2^12', '2^13', '2^14', '2^15']

all_data = {
    "insertion_sort" : {0: {'y_oper': [], 'y_time': []}, 1: {'y_oper': [], 'y_time': []}, 2: {'y_oper': [], 'y_time': []}, 3: {'y_oper': [], 'y_time': []}},
    "selection_sort" : {0: {'y_oper': [], 'y_time': []}, 1: {'y_oper': [], 'y_time': []}, 2: {'y_oper': [], 'y_time': []}, 3: {'y_oper': [], 'y_time': []}},
    "merge_sort" : {0: {'y_oper': [], 'y_time': []}, 1: {'y_oper': [], 'y_time': []}, 2: {'y_oper': [], 'y_time': []}, 3: {'y_oper': [], 'y_time': []}},
    "shell_sort" : {0: {'y_oper': [], 'y_time': []}, 1: {'y_oper': [], 'y_time': []}, 2: {'y_oper': [], 'y_time': []}, 3: {'y_oper': [], 'y_time': []}}
}

all_lsts = []

for i in range(4):
    number = 2**6
    for _ in range(9):
        number *= 2
        new_lst = main_genertor(i, number)
        var_lst = new_lst.copy()


        start = time.time()
        operations = insertion_sort(var_lst)
        end = time.time()

        all_data["insertion_sort"][i]['y_oper'].append(operations)
        all_data["insertion_sort"][i]['y_time'].append(end - start)


        var_lst = new_lst.copy()

        start = time.time()
        operations = selection_sort(var_lst)
        end = time.time()

        all_data["selection_sort"][i]['y_oper'].append(operations)
        all_data["selection_sort"][i]['y_time'].append(end - start)


        var_lst = new_lst.copy()

        start = time.time()
        operations = merge_sort(var_lst)
        end = time.time()

        all_data["merge_sort"][i]['y_oper'].append(operations)
        all_data["merge_sort"][i]['y_time'].append(end - start)


        var_lst = new_lst.copy()

        start = time.time()
        operations = shell_sort(var_lst)
        end = time.time()

        all_data["shell_sort"][i]['y_oper'].append(operations)
        all_data["shell_sort"][i]['y_time'].append(end - start)

        print(all_data)
        print('\n\n')

    for j in range(2):
        if i == 0:
            plt.title('Randomly Generated Array')
        elif i == 1:
            plt.title('Values of the Array are Sorted in Ascending Order')
        elif i == 2:
            plt.title('Values of the Array are Sorted in Descending Order')
        else:
            plt.title('The Array contains Only Elements From the Set {1, 2, 3}')

    
        if j == 1:
            plt.plot(x, all_data["insertion_sort"][i]['y_oper'], label='Insertion sort')
            plt.plot(x, all_data["selection_sort"][i]['y_oper'], label='Selection sort')
            plt.plot(x, all_data["merge_sort"][i]['y_oper'], label='Merge sort')
            plt.plot(x, all_data["shell_sort"][i]['y_oper'], label='Shell sort')
            plt.ylabel('Number of Operations')
        else:
            plt.plot(x, all_data["insertion_sort"][i]['y_time'], label='Insertion sort')
            plt.plot(x, all_data["selection_sort"][i]['y_time'], label='Selection sort')
            plt.plot(x, all_data["merge_sort"][i]['y_time'], label='Merge sort')
            plt.plot(x, all_data["shell_sort"][i]['y_time'], label='Shell sort')
            plt.ylabel('Spent Time')

        plt.xlabel('Array Size')
        plt.legend()
        plt.yscale('log')
        plt.savefig(f'{i}{j}.png')

        plt.clf()
