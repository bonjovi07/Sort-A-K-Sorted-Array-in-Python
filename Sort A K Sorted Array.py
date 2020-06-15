def bracketing(n_list,k):
    double_list = []
    for i in range(len(n_list)):
        my_list = []
        for j in range(len(n_list)):
            x, y = j, j
            for k in range(k + 1):
                if x == i or y == i:
                    my_list.append(n_list[j])
                x += 1
                y -= 1
        double_list.append(my_list)
    return double_list

def list_computation(double_list):
    final_list = []
    for i in range(len(double_list)):
        user_num = min(double_list[i])
        final_list.append(user_num)
        for j in range(len(double_list)):
            if user_num in double_list[j]:
                del double_list[j][double_list[j].index(user_num)]
    print(final_list)


n_list = [3,2,6,5,4]
k = 2
print(f"list: {n_list}\nk: {k}")
two_d_list = bracketing(n_list,k)
print("output: ",end="")
list_computation(two_d_list)




