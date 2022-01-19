data=input()
result=[]
s=''
sum=0
for d in data:
  if d.isalpha():
    result.append(d)
  else:
    sum+=int(d)

result.sort()
for r in result:
  s+=r
sum=str(sum)

print(s+sum)