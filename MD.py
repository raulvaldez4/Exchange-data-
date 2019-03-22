import pandas as pd
import os

exchange_input = ''
exchange_list = []
complete_flag = 'Complete'
remove_flag = 'Remove'
rootdir = '.'
fileendswith = '-4.csv'

while exchange_input.title() != complete_flag:
    if len(exchange_list) == 0:
        exchange_input = input('Add an exchange. Enter in Complete when finished: ')
        exchange_list.append(exchange_input)
        print('\nCurrent List: ', exchange_list)
    else:
        exchange_input = input('Add an exchange. Enter in Complete when finished.\nTo remove previous entry, Enter Remove: ')
        if exchange_input.title() == remove_flag:
            exchange_list.pop()
            print('\nCurrent List:',exchange_list)
        elif exchange_input.title() == complete_flag:
            print('Final List: ', exchange_list)
            break
        else:
            exchange_list.append(exchange_input)
            print('\nCurrent List:', exchange_list)

filepaths = [os.path.join(dirpath,name) for dirpath, dirnames, files in os.walk(rootdir)
        for name in files if name.endswith(fileendswith)]

#df = pd.read_csv(r"C:\Users\User\PycharmProjects\Market_Data_Script\247360-4.csv")

for i in filepaths:
    df = pd.read_csv(i)
    exchange_params = df[df['Exchange'].isin(exchange_list)]
    sorted_exchange_params = exchange_params.sort_values(exchange_params.columns[2])
    #print(exchange_params.to_string())
    sorted_exchange_params.to_csv('Exchange data.csv',sep='\t')




