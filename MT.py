def Multi_Table(Dan_num):
    for i in range(1,10):
        print("%d X %d = %d" % (Dan_num, i, Dan_num*i))

Dan_num = input("몇단을 출력 하시겠습니까? : ")
Multi_Table(int(Dan_num))
