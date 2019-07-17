sum = int(input())
if(sum%4 == 0) and ((sum%100 != 0) or (sum%400 == 0))):
    print("yes")
else:
    print("no")
