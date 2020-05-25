import matplotlib.pyplot as plt
import re
import math
f = open('input.txt', 'r')
f1 = f.read()
f.close()
text = f1.split()
spx = []
spy = []
i=0
tr=0
while text[i]!='Summary:':
	result = re.split(':', text[i])
	if ((result[0]=='192.168.250.3') and (text[i+1]=='->')):
		if text[i+7]=='M':
			text[i+6]=str(math.ceil(float(text[i+6])*1024*1024))	
		ttr=int(text[i+6])		
		tr=tr+ttr
		s = re.split(':', text[i-4])
						
		t = int(s[0])*3600+int(s[1])*60+round(float(s[2]))
		spx.append(t)
		spy.append(ttr)
		
	i=i+1
tr=tr/1024/1024
tr=math.ceil(tr)
print('Согласно тарифу, абонент должен', tr*3, 'руб. (При условии, что плата за неполный мегабайт взимается как за полный)')
spxx=spx
spyy=spy
j=0
while j<len(spxx):
	i=j
	while i<len(spxx):
		if spxx[j]>spxx[i]:
			p=spxx[j]
			spxx[j]=spxx[i]
			spxx[i]=p
			p=spyy[j]
			spyy[j]=spyy[i]
			spyy[i]=p
		i=i+1
		
	j=j+1
i=1

while i<len(spyy):
	spyy[i]=spyy[i-1]+spyy[i]
	spxx[i]=spxx[i]-spxx[0]
	i=i+1
spxx[0]=0
plt.plot(spxx, spyy)
plt.xlabel('Время с первого снятия измерения, с')
plt.ylabel('Объём данных, байты')
plt.show()
