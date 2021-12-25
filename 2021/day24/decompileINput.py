z = int(c)
x = 0
x += z
x %= 26
z /= 1
x += 11
x = (x != w)
y = 25
y *= x
y += 1
z *= y
y = 0
y += w
y += 14
y *= x
z += y


z = int(c)
x = 0
x += z
x %= 26
z /= zDiv
x += xAdd
x = (x != w)
y = 25
y *= x
y += 1
z *= y
y = 0
y += w
y += yAdd
y *= x
z += y


w = int(c)
z /= zDiv
x = ((z % 26) + xAdd != w)
y = (25 * x) + 1
z *= y
z += (w + yAdd) * x

w = int(x)


from program
w = a
x *= 0
x += z
x %= 26
z /= 1
x += 11
x === w
x === 0
y *= 0
y += 25
y *= x
y += 1
z *= y
y *= 0
y += w
y += 14
y *= x
z += y

w = a
x = ((z % 26) + xAdd) != w
z /= zDiv
z *= (x * 25) + 1
z += x(w + yAdd)


w = a
z /= zDiv
if ((z % 26) + xAdd) != w:
    z *= 26
    z += w + yAdd


(z/zDiv)*0+25*0+z%26+xAdd==a==0+1+0+a+yAdd*0+z%26+xAdd==a==0

((z // zDiv) * (25*(((z%26)+xAdd) != a) + 1) + (a+yAdd)*(((z % 26) + xAdd) != a)


(z/zDiv)*(25*(((z%26)+xAdd)!=a)+1)+(a+yAdd)*(((z%26)+xAdd)!=a)


check = ((x % 26) + xAdd) != a
(z / zDiv) * ((25 * check) + 1) + ((a + yAdd) * check)

if ((x % 26) + xAdd) != a
    z = ((z / zDiv) * (26)) + (a + yAdd)
else:
    z //= zDiv 

w = a

x = ((z % 26) + xAdd) != w
z /= zDiv
y = (x * 25) + 1
z *= y
y = (w + yAdd) * x
z += y