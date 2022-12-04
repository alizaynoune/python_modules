from vector import Vector


print('+++++++++++ SUCCESS TESTS ++++++++++++++')
print('+++++++++++ INIT VECTORS TESTS ++++++++++++++\n')
v1 = Vector(10)
print(v1.values)
v2 = Vector([[0.9, 1.0, 0.2, 3.0]])
print(v2.values)
v3 = Vector([[10.9], [2.0], [.2], [2.3]])
print(v3.values)
v4 = Vector((0, 20))
v2 = Vector(10)
print(v4.values)
print('+++++++++++ ARITHMETIC VECTORS TESTS ++++++++++++++\n')
print(v1.values, '\n+\n', v2.values, '\n=\n', (v1 + v2).values)
print(v1.values, '\n-\n', v2.values, '\n=\n', (v1 - v2).values)

print('+++++++++++ ARITHMETIC SCALAR TESTS ++++++++++++++\n')
print("10*", v1.values, '-10', '\n=\n', (10*v1).values)
print(v1.values, '*10', '\n=\n', (v1 * 10).values)
print(v1.values, '/ 10', '\n=\n', (v1 / 10).values)

print('+++++++++++ DOT TESTS ++++++++++++++\n')
print(v1.values, 'dot => ', v2.values, '\n=\n', (v1.dot(v2)))

print('+++++++++++ TRANPOSE VECTORS TESTS ++++++++++++++\n')
vt = v1.T()
print(v1.values, '\ntranspose\n', vt.values)
print(vt.values, '\ntranspose\n', vt.T().values)


print('+++++++++++ FAILED TESTS ++++++++++++++')
try:
    Vector(-1)
except Exception as e:
    print(e)
try:
    Vector((10, 2))
except Exception as e:
    print(e)
try:
    Vector('fjjj')
except Exception as e:
    print(e)
try:
    v1 / v1
except Exception as e:
    print(e)
try:
    v1 / 0
except Exception as e:
    print(e)

try:
    10 / v1
except Exception as e:
    print(e)
