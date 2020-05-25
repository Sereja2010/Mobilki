from docxtpl import DocxTemplate
from num2words import num2words

f = open('out1.txt', 'r')
f1=f.read()
tel=int(f1)
f.close()
f = open('out2.txt', 'r')
f1=f.read()
inet=int(f1)
f.close()

doc = DocxTemplate("Shablon.docx")
All = tel+inet
NDS = All/5
if ((All%10) == 1):
	Slovo = " рубль"
elif ((All%10) == 2 or (All%10) == 3 or (All%10) == 4):
	Slovo = " рубля"
else:
	Slovo = " рублей"
Slova = num2words(All, lang='ru') + Slovo +" 00 копеек"
All=str(All)+" руб."
NDS=str(NDS)+" руб."
context = { 'Slova' : (Slova), 'Inet' : (str(inet)), 'Tel' : (str(tel)), 'All' : (All), 'NDS' : (NDS)}


doc.render(context)
doc.save("Schet.docx")

