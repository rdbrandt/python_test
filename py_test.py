data = [1,2,3,4,5]

print 'Now changed something in "branch 02" \
        plus another new line'

for i, item in enumerate(data):
    print 'index: ' + str(i) + ',', 'value: ' + str(item)
  
print ''  
print 'number of items in data: ' + str(len(data)) + '\n'
    
data.append(6)


print 'plus another change from "master"'
print 'last element in data: ' + str(data[-1])

print 'This was changed from master in branch 03'
