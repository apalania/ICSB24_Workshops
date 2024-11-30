import re
#Regex How-to:
'''
text pattern
construct the regex pattern
process the text / perform the task'''

'''
TAT repeats in the genomic sequence
find all such repeats with their location
determine the longest repeat
'''

'''
re.search
re.match
re.finditer
re.findall -- options for greedy matching?
re.compile -- compiled regex object
re.sub, re.subn
'''

text = 'hello world, Hello Python programming'
sequence = input("Enter genome:\t")
patt1 = 'h|Hello'
patt2 = '[Hh]ello'
biopatt = '(TAT)+'
biopatt2 = '(GC){1,}'
biopatt3 = '((TAT)+).*?((GC)+)'
rgx_biopatt2 = re.compile(biopatt2)
rgx_biopatt3 = re.compile(biopatt3)

patt_email = '[a-zA-Z0-9]+@\w[.]\w' #can be refined
patt_email = '^From: (\S+@\S+)' #better; capturing email address alone as group(1)
patt_curr = '$\S.\S'
patt_curr = '\$\d+.\d+'
#'$\d+(.\d)*' : 11.1.2
#$15.89
patt_curr = '\$[0-9.]+' #covers wide use-cases

#Assignment: Find the largest CpG island in a genomic sequence.
matches = rgx_biopatt3.findall(sequence)
print(matches)

mos = rgx_biopatt3.finditer(sequence)
repeats=[]
locations = []
for mo in mos:
    print(mo.span())
    sp = mo.span()
    repeatLength = int(sp[1] - sp[0])
    repeats.append(repeatLength)
    locations.append(sp[0])   #mo.start() == sp[0]
    #print(mo.group(1))
    print(mo.group())
    print(mo.groups())
    print(mo.group(1))
    print(mo.group(2))
    print(mo.group(3))
    print(mo.group(4))

print("no further matches")

max_repeatLength =0
i=0
#print(max(repeats))

for repLen in repeats:
    if repLen > max_repeatLength:
        max_repeatLength = repLen
        location = locations[i]
    i+=1

print("Maximum repeat length:\t"+str(max_repeatLength)+'\t at Location:\t'+ str(location))

D = dict(zip(locations, repeats))
print(D)

for item in D.items():
    print('Location:\t'+str(item[0])+ '\t with repeat Length:\t'+ str(item[1]))

#newseq = re.sub(biopatt2,biopatt, sequence,count=2)
#identical to:
#newseq = re.sub(biopatt2,biopatt,sequence, 2)
#For global replacement, use sub method, with default count.
#print(newseq)

'''
PROSITE database
sequence motifs

R-[LVAI]-[LVAI]-R-[LVAI](2)-x(3)-R-[YWF]
Python regex for this motif:
R[LVAI]{2}R[LVAI]{2}.{3}R[YWF]
'''

'''
try to explore multiple groups within the regex pattern
to access them, use:
.group(num)
'''
