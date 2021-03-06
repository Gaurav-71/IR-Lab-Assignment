import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import random


def pres_rec(rq, aq):
    x = []
    n_rel = 0
    for i in range(1, len(aq)+1):
        term = aq[i-1]
        if(term in rq):
            n_rel = n_rel + 1
            pres = n_rel/i
            rec = n_rel/len(rq)
            pres = round(pres*100, 2)
            rec = round(rec*100, 2)
            x.append([rec, pres])
    return x


def next_grt(i, rec):
    for x in rec:
        if x[0] >= i:
            return x[1]
    return 0


def interp(inp):
    x = list(range(10, (10 * 10)+1, 10))
    x.insert(0, 0)
    rec, pres = zip(*inp)
    res = []
    for i in x:
        pr = next_grt(i, inp)
        res.append([i, pr])
    return res


def average_pres(inp):
    sum = 0
    count = 0
    rec, pres = zip(*inp)
    res = []
    for x in pres:
        sum = sum + x
        count = count + 1
        res.append(round(sum/count, 2))
    return res


def r_pres(rq, aq):
    n_rel = 0
    for i in range(len(rq)):
        if aq[i] in rq:
            n_rel = n_rel + 1
    pres = n_rel/len(rq)
    return pres

rq = [3, 5, 9, 25, 39, 44, 56, 9, 25, 39, 44,
      56, 71, 89, 94, 105, 119, 124, 136, 144]
aq = [123, 84, 56, 6, 8, 9, 511, 129, 187, 25, 38, 48,
      250, 113, 44, 99, 95, 214, 136, 39, 128, 25, 71, 14, 5]

rp = pres_rec(rq, aq)
inp = interp(rp)
avg = average_pres(rp)
r_precission = r_pres(rq, aq)

print("R_Precission : ", r_precission)

x, y = zip(*inp)
plt1.plot(x, y)
plt1.xlabel("Recall")
plt1.ylabel("Precision")
plt1.show()

rq1 = [3, 5, 9, 25, 39, 44, 56, 9, 25, 39, 44,
       56, 71, 89, 94, 105, 119, 124, 136, 144]
aq1 = [123, 84, 56, 6, 8, 9, 511, 129, 187, 25, 38, 48,
       250, 113, 44, 99, 95, 214, 136, 39, 128, 25, 71, 14, 5]
inp1 = interp(pres_rec(rq1, aq1))
rpres1 = r_pres(rq1, aq1)
print("rpres1 : ", rpres1)
x1, y1 = zip(*inp1)

rq2 = [4, 6, 10, 26, 40, 45, 57, 11, 26, 41,
       45, 57, 72, 90, 95, 106, 120, 125, 137, 145]
aq2 = [123, 40, 56, 6, 8, 10, 511, 129, 45, 26, 38, 48,
       250, 113, 44, 90, 95, 214, 136, 145, 128, 25, 72, 14, 5]
inp2 = interp(pres_rec(rq2, aq2))
rpres2 = r_pres(rq2, aq2)
print("rpres2 : ", rpres2)
x2, y2 = zip(*inp2)

diff = rpres1 - rpres2
print("Difference : ", diff)

plt2.plot(x1, y1, color='blue', marker='+')
plt2.plot(x2, y2, color='red', marker='o')
plt2.xlabel("Recall")
plt2.ylabel("Precision")
plt2.show()

# fig = plt3.figure()
# x_axis = ["rpres1", "rpres2", "Difference"]
# y_axis = [rpres1, rpres2, diff]
# plt3.bar([0, 1, 2], y_axis)
# plt3.xticks([0, 1, 2], x_axis)
# plt3.show()

def r_pres_pair(Rq,Aq): # find r_precision for each pair of rq, aq
    r_prec = []
    for rq,aq in zip(Rq,Aq):
        temp = r_pres(rq,aq)
        r_prec.append(temp)
    return r_prec

docs = ["d"+str(i) for i in range(1,21)] #d1 to d20

Rq10, AqA, AqB = [],[],[]

# Generating n relavent documents for a given query
for _ in range(10):
    n = random.randint(6,9) 
    li = random.sample(docs,n) #select n random docs
    Rq10.append(li)
    
# Generating n documents retrieved by Algoritm A for a given query
for _ in range(10):
    n = random.randint(13,18)
    li = random.sample(docs,n)#select n random docs
    AqA.append(li)

# Generating n documents retrieved by Algoritm B for a given query
for _ in range(10):
    n = random.randint(13,18)
    li = random.sample(docs,n) #select n random docs
    AqB.append(li)

RP_A = r_pres_pair(Rq10,AqA)

RP_B = r_pres_pair(Rq10,AqB)

RP_AB = [A-B for A,B in zip(RP_A,RP_B)]


qno = list(range(1,11))

plt3.bar(qno,RP_AB,color="blue",width=0.7)
plt3.xticks(qno)
plt3.axhline(y = 0, color="black",linestyle = '-')
plt3.xlabel("Query Number")
plt3.ylabel("R Precision A-B")
plt3.title("Precision Histogram")
plt3.ylim(-1.5,1.5)
plt3.show()

d56 = rp[0]
r1 = d56[0]/100
p1 = d56[1]/100

hm1 = 2/((1/r1) + (1/p1))
em11 = 1 - hm1  # b = 1
em12 = 1 - ((1 + 0.5**2)/((0.5**2)/r1 + (0.5**2)/p1))
em13 = 1 - ((1 + 2**2)/((2**2)/r1 + (2**2)/p1))

print("\n\n for D56")
print("\nHarmonic Measure : ", hm1, "\nE-Measure (when b=1 ) : ", em11,
      "\nE-Measure (when b>1) : ", em12, "\nE-Measure (when b<1) : ", em13)

d39 = rp[5]
r2 = d39[0]/100
p2 = d39[1]/100

hm2 = 2/((1/r2) + (1/p2))
em21 = 1 - hm2  # b = 1
em22 = 1 - ((1 + 0.5**2)/((0.5**2)/r2 + (0.5**2)/p2))
em23 = 1 - ((1 + 2**2)/((2**2)/r2 + (2**2)/p2))

print("\n\n for D39")
print("\n\nHarmonic Measure : ", hm2, "\nE-Measure (when b=1 ) : ", em21,
      "\nE-Measure (when b>1 ) : ", em22, "\nE-Measure (when b<1 ) : ", em23)
