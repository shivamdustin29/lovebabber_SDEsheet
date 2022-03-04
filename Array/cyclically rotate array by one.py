def rightRotate(lists, num):
    output_list = []
    for item in range(len(lists) - 1, len(lists)):
        output_list.append(lists[item])
        #output_list.append(lists[item])
    for item in range(0, len(lists) - 1):
        output_list.append(lists[item])
 
    return output_list
rotate_num = 1
list_1 = [1, 2, 3, 4, 5, 6]
 
print(rightRotate(list_1, rotate_num))
