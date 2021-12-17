d=str(input())
count=8
if '1' in d or '8' in d:
  count-=3
if '2' in d or '7' in d:
  count-=2
if 'a' in d or 'h' in d:
  count-=3
if 'b' in d or 'g' in d:
  count-=2
print(count)

'''
처음에 if문을 
if '1' or '8' in d:
이렇게 써서오류가 남. 각각의 조건 사이에 or을 넣어주어야함
'''