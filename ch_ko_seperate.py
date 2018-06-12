#-*- coding: utf-8 -*

f= open('lyric.txt', 'r')
# str_all = f.read()
# print(str_all)
count = 0
str_ch = ""
str_ko = ""
for i in f.readlines():
    if count % 2 == 1:
        str_ch += i
    else:
        str_ko += i
        # print(i)
    count += 1
print(str_ko)
f.close()
f = open('lyric.ko.txt', 'w')
f.write(str_ko)
f.close()

f = open('lyric.ch.txt', 'w')
f.write(str_ch)
f.close()
