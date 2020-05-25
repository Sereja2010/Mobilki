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

tr = tr * 3
f = open('out2.txt', 'w')
f.write(str(tr))
