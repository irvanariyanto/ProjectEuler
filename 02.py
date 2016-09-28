num1 = 1;
num2 = 1;
result = 1;
total = 0;
while (result < 4000000):
    print result
    if ((result % 2) == 0):
        total += result;
    result = num1 + num2;
    num2 = num1;
    num1 = result;
print total
