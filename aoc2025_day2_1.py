in_txt = '1188511880-1188511890'

start, stop = in_txt.split('-')
print(start, stop)

r = range(int(start), int(stop)+1)
print(list(r))

res = 0

for id in range(int(start), int(stop)+1):
    print(id, len(str(id)), str(id)[:5], str(id)[5:])
    if str(id)[:5] == str(id)[5:]:
        res += id

print(res)

