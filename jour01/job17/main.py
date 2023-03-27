def detect_multiple_of_3_and_5():
    str_returned = ""
    for i in range(1,101,1):
        if i % 3 == 0:
            str_returned += "Fizz"
        if i % 5 == 0:
            str_returned += "Buzz"
        if str_returned == "":
            print(i)
        else:
            print(str_returned)
        str_returned = ""

detect_multiple_of_3_and_5()