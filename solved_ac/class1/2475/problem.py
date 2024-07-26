a = input().split(' ')
checksum = 0
for i in a:
    checksum = checksum + int(i)**2

print(checksum%10)
