NUMBER = 2020
with open("01_input.txt", "r") as f:
    s = f.read()
s = s.split('\n')[:-1]
s = [int(i) for i in s]
n = len(s)
found = False
for i in range(n):
    if found:
        break
    for j in range(i+1,n):
        for k in range(j+1,n):
            if s[i] + s[j] + s[k] == NUMBER:
                i_1, i_2, i_3 = s[i],s[j],s[k]
                found = True
                break
print(i_1 * i_2 * i_3)
