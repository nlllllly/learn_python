scores = [ 91, 45, 74, 50, 37, 68, 84, 70]

a_list = []
b_list = []
c_list = []
d_list = []

for score in scores:
    if score >= 80:
        a_list.append(score)
    elif score >= 60:
        b_list.append(score)
    elif score >= 40:
        c_list.append(score)
    else:
        d_list.append(score)

print(a_list)
print(b_list)
print(c_list)
print(d_list)