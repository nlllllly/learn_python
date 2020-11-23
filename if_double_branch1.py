# score の値によって、85点以上であれば、「ok_list」に。以下であれば、「ng_list」に割り振られる。
score = 75
ok_list = []
ng_list = []

if score >= 80:
    ok_list.append(score)
else:
    ng_list.append(score)

print(ok_list)
print(ng_list)