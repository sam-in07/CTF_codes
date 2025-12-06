from Cryptodome.Util.number import inverse


p = 61
q = 53
m = int(input("Enter value of m : "))
n = p * q 

phi =(p-1)*(q-1)
e = 17 
d = inverse(e,phi)
print("value of d :"+ str(d))
c = pow(m,e,n)
print("value of c :"+ str(c))

m =pow(c,d,n)
print("vlaue of m : "+ str(m))
