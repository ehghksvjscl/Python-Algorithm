a,b,c=map(int,input().split())
d=int(input())

 

tmp_h = d // 3600
tmp_hm = d % 3600
tmp_m = tmp_hm // 60
tmp_s = tmp_hm % 60

 

a += tmp_h
b += tmp_m
c += tmp_s

 


if c >= 60:
    b=(b+(c//60))
    c = c % 60
  

 

if b >=60:
    a +=(b//60)
    b = b % 60
    

 

if a >= 24:
    a = a % 24

 

 

print("%s %s %s"%(int(a),int(b),int(c)))