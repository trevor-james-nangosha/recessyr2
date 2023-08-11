#integers, floats, complex
w = 10 # int
e= 3.8 # float
r = 2j # complex

print(w)
print(type(w))
print(e)
print(type(e))
print(r)
print(type(r))

#floats
g = 2.89
z = -3.3
print(type(z))
print(type(g))

#complex numbers
p = 6 + 10j
t = 4j
u = -2j
print(type(p))
print(type(t))
print(type(u))

# type conversions
# convert from int to complex
z = complex(w)
print(z)
print(type(z))

#convert from int to float
w = 10
d = float(w)
print(d)
print(type(d))

#convert from float to complex
g = 2.89
f = complex(g)
print(f)
print(type(f))

#convert from complex to float
h =2j
k = float(h)
print(k)
print(type(k))