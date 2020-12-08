NUMBER = 2020
with open("01_input.txt", "r") as f:
    s = f.read()
s = s.split('\n')[:-1]
s = [int(i) for i in s]
n = len(s)
print(n)
found = False
for i in range(n):
    if found:
        break
    for j in range(i+1,n):
        if s[i] + s[j] == NUMBER:
            i_1, i_2 = s[i],s[j]
            found = True
            break
print(i_1 * i_2)
