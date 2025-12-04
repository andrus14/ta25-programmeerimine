f = open('example.txt')
# lines = [line.strip() for line in f.readlines()]

start = 50
password = 0

for line in f.readlines():
    
    line = line.strip()
    direction = line[0]
    distance = int(line[1:])

    # print(line + ':', direction, '/', distance)

    if direction == 'L':
        start = (start - distance) % 100
    else:
        start += distance

    print(line + ':', start)