def Multi_Table(reverse_order_flag):
    for i in range(1,10):
        for j in range(1,10):
            if reverse_order_flag:
                print("%d X %d = %d" % ((10-i), (10-j), (10-i)*(10-j)))
            else:
                print("%d X %d = %d" % (i, j, i*j))
    print(reverse_order_flag)

reverse_order_flag = input("거꾸로 출력 하시겠습니까?")
Multi_Table(reverse_order_flag)
