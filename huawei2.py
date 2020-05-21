book = int((input().split(" "))[0])
person = int((input().split(" "))[0])
look = []
for i in range(person):
    look.append(sorted(list(map(int,input().split(" ")))))
print(look)
count =1
sets=set(look[0])
for i in range(1,len(look)):
    for j in range(len(look[i])):
        if look[i][j] not in sets:
            count+=1
            # sets.add(look[i][j])
            for mi in look[i][j:]:
                sets.add(mi)
            break
        else:
            for mi2 in look[i][j:]:
                sets.add(mi2)
            break
print(count)
