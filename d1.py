from tqdm import tqdm


num_list = ['0','0','0','0','0','0']
def func(numlist):
    #默认even length
    mid = int(len(numlist)/2)
    left = numlist[0:mid]
    right = numlist[mid:]
    for i in left:
        if i in right:
            return True
    return False
res = 0
for i in tqdm(range(1000000)):
    tmp_num = list(str(i))
    if i>9 and i<100:
        num_list[-1] = tmp_num[-1]
        num_list[-2] = tmp_num[-2]
    if i>99 and i<999:
        num_list[-1] = tmp_num[-1]
        num_list[-2] = tmp_num[-2]
        num_list[-3] = tmp_num[-3]
    if i>999 and i<9999:
        num_list[-1] = tmp_num[-1]
        num_list[-2] = tmp_num[-2]
        num_list[-3] = tmp_num[-3]
        num_list[-4] = tmp_num[-4]
    if i>9999 and i<99999:
        num_list[-1] = tmp_num[-1]
        num_list[-2] = tmp_num[-2]
        num_list[-3] = tmp_num[-3]
        num_list[-4] = tmp_num[-4]
        num_list[-5] = tmp_num[-5]
    if i>99999 and i<999999:
        num_list[-1] = tmp_num[-1]
        num_list[-2] = tmp_num[-2]
        num_list[-3] = tmp_num[-3]
        num_list[-4] = tmp_num[-4]
        num_list[-5] = tmp_num[-5]
        num_list[-6] = tmp_num[-6]
    else:
        num_list[-1] = tmp_num[-1]
    if func(num_list):
        res=res+1
print("res=",res)
