path='attack.csv'
date = [line.strip() for line in open(path, 'r') if line.strip()]
ips = set(date)
#print(ips)
dict = {}
for i in date:
    dict[i] += 1
else:
    dict[i] = 1
    #print(dict)
    sort_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    print(sort_dict)