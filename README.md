# arithmeticcoding
算法描述：  
第一步：输入一个字符串用于压缩字符测试并导入所需要的库：
```
from collections import Counter
from decimal import *
```  
第二步：需要统计所有字符出现的频率
```
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
```
第三步：依据算术编码的原理,利用第二步统计的每个字符的频率，并且计算他每一次字符串迭代而更新的每个字符的区域的初始化。
```
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
```
第四步：依据算术编码的原理,利用第二步统计的每个字符的频率，并且计算他每一次字符串迭代而更新的每个字符的区域
```
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
```
第五步：为了将算术编码的结果，找到最短的二进制串
```
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
```
第六步：找到最小串
```
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
```
第7步：将二进制字符串转为二进制数
```
def bin2dec(b):

  d = Decimal(0.0)
  for i, x in enumerate(b):
    d += 2**(-Decimal(i)-1)*x
  return d

```
第8步：将编码的压缩结果转为原码
```
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
```
