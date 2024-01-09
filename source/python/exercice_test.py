# Test 1
a,b = 2,3
if a == 2 and b == 3:
    print('tests ok')
else:
    print('tests failed')

# Test 2
a,b = 2,3
if a == 1 or b == 3:
    print('tests ok')
else:
    print('tests failed')

# Test 3
a,b = 2,3
if a == 1 or not(b == 3):
    print('tests ok')
else:
    print('tests failed')

# Test 4
a,b = 2,3
if a == 2 and not(b == 3):
    print('tests ok')
else:
    print('tests failed')

# Test 5
a,b = 2,3
if not(a == 3) and not(b == 2):
    print('tests ok')
else:
    print('tests failed')
    
# Test 6
a,b = 2,3
if not(a == 3 and b == 2):
    print('tests ok')
else:
    print('tests failed')
    
# Test 7
a,b = 2,3
if not(a == 2) or not(b == 3):
    print('tests ok')
else:
    print('tests failed')
    
# Test 8
a,b = 2,3
if not(a == 3 or b == 2):
    print('tests ok')
else:
    print('tests failed')