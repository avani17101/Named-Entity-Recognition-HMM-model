import re
import itertools 
import json


  
def findsubsets(s, n): 
    return list(itertools.combinations(s, n))
ft = open('tags.txt', 'r')

w = ""
t = ""
wp = []
wl =[]
wr = []
wd =[]
wy = []
wt = []
wn = []
wo = []
word = ""
tags = ['l','r','p','d','t','n','o']
wdic={}
e = {}

'''def wordpresent(word, list):
	flag =0
	for ele in list:
		ele = ele.split('/')
		if(ele[0]==word):
			flag=1
	#print(flag)
	return flag'''
def replace(tag,list):
	flag =0
	for ele in list:
		ele = ele.split('/')
		if(ele[0]==word):
			flag=1
	#print(flag)
	return flag



for line in ft:
	if('Article' not in line):
		if('p' in line):

			wp.append(line)


		if('l' in line):
			wl.append(line)

		if('r' in line):
			wr.append(line)

		if('d' in line):
			wd.append(line)

		if('y' in line):
			wy.append(line)

		if('t' in line):
			wt.append(line)

		if('n' in line):
			wn.append(line)

		if('o' in line):
			wo.append(line)
wgrand = []
wgrand = wp+wl+wr+wd+wy+wt+wo
wdic['p']= wp
wdic['l'] = wl
wdic['r'] = wr
wdic['d']= wd
wdic['y'] = wy
wdic['t'] = wt
wdic['n'] = wn
wdic['o'] = wo
#print(wgrand)
ft.close()
content= open('articles.txt', 'r').read()
	
newcontent = (content+ '.')[:-1]
for word in wgrand:
	e[word]= {}
	for tag in tags:
		e[word][tag]= wgrand.count(word)/len(wdic[tag])
# as requested in comment
fe = open('emission.txt','w')
k = ""
printable =""
for i in e:
	k = i.split('/')
	printable += k[0]
	printable += " "
	#fe.write(k[0])
	for j in e[i]:
		printable +=j
		printable += " "
		printable += str(e[i][j])
		#fe.write[(j, e[i][j])]
	printable += '\n'
	fe.write(printable)
print(e)
'''for word in wgrand:
	if(wordpresent(word,wp)):
		newcontent = newcontent.replace(word,'p')
	if(wordpresent(word,wl)):
		#print("hi there")
		newcontent= newcontent.replace(word,'l')
	if(wordpresent(word,wr)):
		newcontent= newcontent.replace(word,'r')
	if(wordpresent(word,wd)):
		newcontent= newcontent.replace(word,'d')
	if(wordpresent(word,wy)):
		newcontent= newcontent.replace(word,'y')
	if(wordpresent(word,wt)):
		newcontent= newcontent.replace(word,'t')
	if(wordpresent(word,wn)):
		newcontent= newcontent.replace(word,'n')
	if(wordpresent(word,wo)):
		newcontent= newcontent.replace(word,'o')'''
#print(wy)
contents = content.split()
"""c = {}
for word in contents:
	c[word] = content.count(word)
	
print(c)"""
"""for key in e
print(" {}  {}\n".format(key, e[key]))"""



for word in wp:
	word = word.split('/')
	#print(word[0])
	newcontent = newcontent.replace(word[0],'p')
	
for word in wl:
	word = word.split('/')
	newcontent = newcontent.replace(word[0],'l')
	
for word in wr:
	word = word.split('/')
	newcontent = newcontent.replace(word[0],'r')
	
for word in wd:
	word = word.split('/')
	newcontent = newcontent.replace(word[0],'d')
	
for word in wy:
	word = word.split('/')
	newcontent = newcontent.replace(word[0],'y')

	#print(word)
for word in wt:
	word = word.split('/')
	newcontent = newcontent.replace(word[0],'t')

for word in wn:
	word = word.split('/')
	newcontent = newcontent.replace(word[0],'n')

for word in wo:
	word = word.split('/')
	newcontent = newcontent.replace(word[0],'o')
	
newcontents = newcontent.split()
for word in newcontent:
	if (word not in ['p','l','r','d','y','t','n','o','।']):
		newcontent = newcontent.replace(word,'')




with open('new_file.txt','w+') as f:
	f.write(newcontent)

'''print("yp\t  {}    \t{}".format(newcontent.count('yp'), newcontent.count('yp')/11))
print("yr\t  {}    \t{}".format(newcontent.count('yr'), newcontent.count('yr')/11))
print("yl\t  {}    \t{}".format(newcontent.count('yl'), newcontent.count('yl')/11))
print("yd\t  {}    \t{}".format(newcontent.count('yd'), newcontent.count('yd')/11))
print("yo\t  {}    \t{}".format(newcontent.count('yo'), newcontent.count('yo')/11))
print("yt\t  {}    \t{}".format(newcontent.count('yt'), newcontent.count('yt')/11))
print("yn\t  {}    \t{}".format(newcontent.count('yn'), newcontent.count('yn')/11))
print("yy\t  {}    \t{}".format(newcontent.count('yy'), newcontent.count('yy')/11))'''

s = {'p','l','r','d','y','t','n','o'}
#subset = findsubsets(s, i)
subset = []
'''for i in range(2):
	#print("sequence{}  number{} ".format(findsubsets(s, i))
	subset.append(findsubsets(s, i))
print(subset)	
for s in subset:
	#print(s)
	for seq in s:
		#print(seq)
		st_seq = ''.join(map(str, seq))
		n = newcontent.count(st_seq)
		if(n>0):
			zz = newcontent.count(st_seq)
			oc = newcontent.count(st_seq.charAt(0)
			  = zzoc
			print("{}\t  {}\t  {}".format(st_seq,zz,t_prob))
			print("\n")'''



	
			
				






