#!bin/bash
./lab1
python3 lab2.py
python3 lab3.py
unoconv -f pdf Schet.docx
rm Schet.docx
rm out1.txt
rm out2.txt
echo Успешно, проверьте файл Schet.pdf
