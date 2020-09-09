#Enter your code here...
itxt = input("enter a word to reverse: ")
otxt = ""
for i in range(len(itxt)-1,-1,-1):
    otxt = otxt+itxt(i)
    print("The reversed string is :"+otxt)