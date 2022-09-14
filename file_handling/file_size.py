myfile=open("abc.txt",'r')
str=" "
size=0
totalsize=0
while str:
    str=myfile.read()
    size+=len(str)
    totalsize+=len(str.strip())
print(f'Size of the file is {size}')
print(f'Total size of the file after strip is {totalsize}')
myfile.close()
