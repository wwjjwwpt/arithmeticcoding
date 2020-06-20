from collections import Counter
from decimal import *


strcode=input("PLZ input the original coed:")
clength = len(strcode)
code = [x for x in strcode]
print("original code is:",strcode)
print("The length of code:",clength)

# code = [1,2,3,1,1,2,3,1,2,3,2,1,2,3,1,1,1]

def countfrequency(code):
    """
    compute the original code's frequency
    :param code: The original code
    :return: frequency is a dict adn keyvalue is a list
    """
    length = len(code)
    codesort=sorted(code)
    count = Counter(codesort)
    frequency = {}
    for key in count:
        frequency.update({key:[count[key],Decimal(count[key]/length)]})
    return frequency
def initfrequency(frequency,intervalstart,intervallen):
    """
    compute the original code's interval
    :param frequency: frequency is a dict adn keyvalue is a
    :param bigrange:
    :return:frequency with value append interval
    """

    for key in frequency:
        frequency[key].append(intervalstart)
        intervalstart+=frequency[key][1]*intervallen
        frequency[key].append(intervalstart)
    return frequency

def computeinterval(code):
    lencode = len(code)
    frequency = countfrequency(code)
    frequency = initfrequency(frequency,Decimal(0.0),Decimal(1.0))
    intervalstart = Decimal(0.0)
    intervallen = Decimal(0.0)
    for index,value in enumerate(code):
        if index == 0:
            intervalstart = frequency[value][2]
            intervallen = frequency[value][1]
        else :
            frequency = initfrequency(frequency,intervalstart,intervallen)
            intervalstart = frequency[value][2+index*2]
            intervallen = frequency[value][1]*intervallen
    return frequency[value][2+(lencode-1)*2],frequency[value][3+(lencode-1)*2]

def dec2bin(x):
  x = Decimal(x)
  x -= int(x)
  bins = []
  i=10000
  while x and i:
    i-=1
    x *= 2
    bins.append(1 if int(x)>=1. else 0)
    x -= int(x)
  return bins

def cshort(x,y):
    flag = 0
    z=[]
    for i in range(min(len(x),len(y))):
        if x[i] !=y[i]:
            if flag == 0:
                z.append(1)
                return z
            else:
                z.append(1)
                return z
        else:
            flag = 1
            z.append(x[i])
    return z

def bin2dec(b):

  d = Decimal(0.0)
  for i, x in enumerate(b):
    d += 2**(-Decimal(i)-1)*x
  return d


def decode(code,frequency,codelen):
    code = [int(x) for x in code]
    orcode = []
    intervalstart = Decimal(0.0)
    intervallen = Decimal(1.0)
    interval = initfrequency(frequency, intervalstart, intervallen)
    c=bin2dec(code)
    for index in range(codelen):
        for value in interval:
            if interval[value][2+index*2]<=c and interval[value][3+index*2]>=c:
                orcode.append(value)
                intervalstart = interval[value][2+index*2]
                intervallen = frequency[value][1] * intervallen
                break
        interval = initfrequency(frequency,intervalstart,intervallen)
    return orcode


frequency = countfrequency(code)
intervalstart,intervalstartend = computeinterval(code)
print(intervalstart,intervalstartend)
binstart,binend = dec2bin(intervalstart),dec2bin(intervalstartend)
print(binstart,binend)
encode = cshort(binstart,binend)
strcode = ''.join([str(x) for x in encode])
print('encoding:',strcode)
orcode = decode(strcode,frequency,clength)
orcode = ''.join([str(x) for x in orcode])
print('decoding:',orcode)













