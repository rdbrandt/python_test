data = [1,2,3,4,5]

print 'This change made in "branch 01"'

for i, item in enumerate(data):
    print 'index: ' + str(i) + ',', 'value: ' + str(item)
  
print ''  
print 'number of items in data: ' + str(len(data)) + '\n'
    
data.append(6)

print 'last element in data: ' + str(data[-1])

print 'This was done in "master" branch'
