def Multi_Table(reverse_order_flag=False):
    for i in range(1,10):
        for j in range(1,10):
            if reverse_order_flag:
                print("%d X %d = %d" % ((10-i), (10-j), (10-i)*(10-j)))
            else:
                print("%d X %d = %d" % (i, j, i*j))


reverse_order_flag = input("거꾸로 출력 하시겠습니까?")

if reverse_order_flag:
    Multi_Table(reverse_order_flag)
else:
    Multi_Table()

#Multi_Table(reverse_order_flag)
#try:
#    Multi_Table(reverse_order_flag)
#except ValueError:
#    print("정수 값을 입력해주세요")
