import numpy as np
import csv
# Q4 a sub 15 line python code to obtain csv with formatting
def format():
    f = open("test.csv", 'r')
    reader = csv.reader(f, delimiter = ',')
    reader = [[0 if x == 'fall' or x =='spring' else x for x in x] for x in reader]
    reader = [[1 if x == 'winter' else x for x in x] for x in reader]
    reader = [[-1 if x == 'summer' else x for x in x] for x in reader]
    return np.matrix(reader)
## 10 lines
# Q4b a one line code to select 2-3, 10-11.
def select():
    print  format()[1:3,9:12]
## 1 line
## main
def main():
    select()
if __name__ == '__main__':
    main()
