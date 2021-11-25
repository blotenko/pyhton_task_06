def task_01_a():
    people = [
        {'name': "Tom", 'age': 10},
        {'name': "Mark", 'age': 5},
        {'name': "Pam", 'age': 7}]
    for j in people:
        max = j['age']
        break

    for j in people:
        if j['age']  < max:
            max = j['age']

    print max

def task_01_b():
    people = [
        {'name': "Tom", 'age': 10},
        {'name': "Mark", 'age': 5},
        {'name': "Pamff", 'age': 7}]

    for j in people:
        max = j['name']
        break

    for j in people:
        if len(j['name']) > len(max):
            max = j['name']

    print max

def task_01_v():
    people = [
        {'name': "Tom", 'age': 10},
        {'name': "Mark", 'age': 5},
        {'name': "Pamff", 'age': 7}]
    count=0
    average = 0
    for j in people:
        average = average+j['age']
        count+=1
    print average/count
    return average/count

def task_02_a():
    dict1 = {'a': 1, 'b': 2,'c' : 3 }
    dict2 = {'a': 1, 'f': 2, 'c': 3}
    list = []
    for i in dict1.keys():
        for j in dict2.keys():
            if i == j :
                list.append(i)
    print list

def task_02_b():
    dict1 = {'a': 1, 'b': 2,'z' : 3, 'x' : 4 }
    dict2 = {'a': 1, 'f': 2, 'c': 3}
    list = []
    for i in dict1.keys():
        count = 0
        for j in dict2.keys():
            count+=1
            if j == i:
                break
            if j != i :
                if count == len(dict2):
                    list.append(i)
                    break
    print list


def task_02_c():
    dict1 = {1:1, 2:2}
    dict2 = {11:11, 2:22}
    dict3 = {}

    for i in dict1.keys():
        count = 0
        for j in dict2.keys():
            count+=1
            if j == i:
                break
            if j != i :
                if count == len(dict2):
                    dict3[i]=dict1[i]
                    break
    print dict3

def task_02_g():
    dict1 = {1:1, 2:2}
    dict2 = {11:11, 2:22}
    dict3 = {}

    for i in dict1.keys():
        count = 0
        for j in dict2.keys():
            count+=1
            if j == i:
                dict3[i] = [dict1[i],dict2[i]]
                break
            if j != i :
                if count == len(dict2):
                    dict3[i]=dict1[i]
                    dict3[j] = dict2[j]
                    break
    print dict3




if __name__ == '__main__':
    task_01_a()
    task_01_b()
    task_01_v()
    task_02_a()
    task_02_b()
    task_02_c()
    task_02_g()



