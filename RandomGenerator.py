
# Lists A, B, C

A = ['creamy','buttery','green','perfect','apple','cookie','slow-cooker','chunky','garlicky','brown']

B = ['pumpkin','mashed','bean','roast','cider','crust','smashed','apple-walnut','almond','butter']

C = ['pie','potatoes','casserole','turkey','gravy','cheesecake','potatoes','cake','breadcrumbs','yams']

import random 
# first number of the list = 0
a = random.randint(0,9)
b = random.randint(0,9)
c = random.randint(0,9)
print (A[a],B[b],C[c])
#we delete them so they do not reappear
del(A[a],B[b],C[c])

d = random.randint(0,8)
e = random.randint(0,8)
f = random.randint(0,8)
print(A[d],B[e],C[f])
del(A[d],B[e],C[f])

g = random.randint(0,7)
h = random.randint(0,7)
i = random.randint(0,7)
print(A[g],B[h],C[i])
del(A[g],B[h],C[i])

j = random.randint(0,6)
k = random.randint(0,6)
l = random.randint(0,6)
print(A[j],B[k],C[l])
del(A[j],B[k],C[l])

m = random.randint(0,5)
n = random.randint(0,5)
o = random.randint(0,5)
print(A[m],B[n],C[o])
del(A[m],B[n],C[o])

p = random.randint(0,4)
q = random.randint(0,4)
r = random.randint(0,4)
print(A[p],B[q],C[r])
del(A[p],B[q],C[r])

s = random.randint(0,3)
t = random.randint(0,3)
u = random.randint(0,3)
print(A[s],B[t],C[u])
del(A[s],B[t],C[u])

v = random.randint(0,2)
w = random.randint(0,2)
x = random.randint(0,2)
print(A[v],B[w],C[x])
del(A[s],B[t],C[u])
