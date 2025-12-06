# step take value of n then factordb ==> p & q

from Crypto.Util.number import inverse, long_to_bytes

# Subject information
c=2876775888094066277993461252615256240667461320340670686745
n=7306988677162564280743578366101406260426476848173514587356
e=65537

# Decompose p and q onling.
p = 189239861511125143212536989589123569301
q = 386123125371923651191219869811293586459 

phi = (p-1)*(q-1)
d = inverse(e, phi)
m = pow(c, d, n)
print(long_to_bytes(m))