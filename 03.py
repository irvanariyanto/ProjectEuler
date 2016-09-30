number=600851475143
devider=2
list=[]
while(True):
    if(number%devider==0):
        if(number==devider):
            list.append(devider)
            break;
        number=number/devider
        list.append(devider)
        devider=2
    else:
        devider+=1
print list
