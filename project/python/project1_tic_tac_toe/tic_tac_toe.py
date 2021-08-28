def display_board (row1,row2,row3):
    print (row1)
    print (row2)
    print (row3)

def input_from_user():
    ans = "temp"
    accept_range = range(0,10)
    in_range = False
    while (ans.isdigit() == False or in_range == False):
        ans = input("Please choose a number from 0 to 9: ")
        if ans.isdigit() == False:
            print("It is not a digit")
        else:
            if int(ans) in accept_range:
                in_range = True
            else:
                in_range = False
    return int(ans)

if __name__ == '__main__':
    input_from_user()
    