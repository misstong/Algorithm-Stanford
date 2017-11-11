import math

def size_base10(num):
    return int(math.log10(num))+1

def split_at(num,m):
    shift=long(math.pow(10,m))
    high=num/shift
    low=num-high*shift
    return high,low

def karatsuba(num1,num2):
    if(num1<10)or(num2<10):
        return num1*num2
    
    m=max(size_base10(num1),size_base10(num2))
    m2=m/2
    
    high1,low1=split_at(num1,m2)
    high2,low2=split_at(num2,m2)

    z0 = karatsuba(low1,low2)
    z1 = karatsuba((low1+high1),(low2+high2))
    z2 = karatsuba(high1,high2)
    return (z2*long(math.pow(10,2*m2)))+((z1-z2-z0)*long(math.pow(10,m2)))+(z0)

def karatsuba1(x,y):
	"""Function to multiply 2 numbers in a more efficient manner than the grade school algorithm"""
	if len(str(x)) == 1 or len(str(y)) == 1:
		return x*y
	else:
		n = max(len(str(x)),len(str(y)))
		nby2 = n / 2
		
		a = x / 10**(nby2)
		b = x % 10**(nby2)
		c = y / 10**(nby2)
		d = y % 10**(nby2)
		
		ac = karatsuba(a,c)
		bd = karatsuba(b,d)
		ad_plus_bc = karatsuba(a+b,c+d) - ac - bd
        
        	# this little trick, writing n as 2*nby2 takes care of both even and odd n
		prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd

		return prod
	    
def integerMultiply(x,y,n):
    if n==1:
        return x*y
    shift=long(math.pow(10,(int)(n/2)))
    xl=x/shift
    xr=x-xl*shift
    yl=y/shift
    yr=y-yl*shift
    
    m=int(n/2)
    p1=integerMultiply(xl,yl,m)
    p2=integerMultiply(xr,yr,m)
    p3=integerMultiply(xl+xr,yl+yr,m)
    return p1*long(math.pow(10,2*m))+(p3-p1-p2)*long(math.pow(10,m))+p2

#print integerMultiply(29,18,2)
#print 29*18

#print integerMultiply(18362688,87234988,8)
#print 18362688*87234988

#print integerMultiply(3141592653589793238462643383279502884197169399375105820974944592,
 #                     2718281828459045235360287471352662497757247093699959574966967627,64)
#print 2718281828459045235360287471352662497757247093699959574966967627*3141592653589793238462643383279502884197169399375105820974944592

#print integerMultiply(123,234,3)
#print 123*234

#print integerMultiply(12335,2344,5)
#print 12335*2344

#print split_at(2686,2)

print karatsuba(29,13)
print 29*13

print karatsuba1(3141592653589793238462643383279502884197169399375105820974944592,
                     2718281828459045235360287471352662497757247093699959574966967627)
print 2718281828459045235360287471352662497757247093699959574966967627*3141592653589793238462643383279502884197169399375105820974944592

print karatsuba(12345787824568,686862406346)
print 12345787824568*686862406346
