import re
a = 'charlie chcha.'
email = 'mitesh123@gmail.com'
rendom_series = 'xyz,xxyxyz,xxyxx,xyzxyz,xyzz,xxyyzz,zyz,xzyz'

re_1 = re.search(r'\.',a)
print(a[re_1.span()[0]:re_1.span()[1]])

re_2 = re.findall(r'[@]+[a-z]{5}',email)
print(re_2)

re_3 = re.findall(r'^cha',a)
print(re_3)

re_4 = re.findall(r'cha.$',a)
print("$",re_4)

re_5 = re.findall(r'c.a',a)
print(re_5)

re_6 = re.findall(r'xy|xx',rendom_series)
print(re_6)

re_7 = re.findall(r'ch?a',a)
print(re_7)
# not understanded to much

re_8 = re.findall(r'ch*a',a)
print(re_8)

re_9 = re.findall(r'xy+z',rendom_series)
print(re_9)

re_10 = re.findall(r'x{2,4}',rendom_series)
print(re_10)

re_11 = re.findall(r'(x|z)yz',rendom_series)
print(re_11)

# Special Sequences in RegEx

name = "Harry Potter"
ss_1 = re.findall(r'\AHarr',name) # return staring match char
print(ss_1)

ss_2 = re.findall(r'arry\b',name) # first char not count and also last not count
print(ss_2)

ss_3 = re.findall(r'\Botter',name) # same oppsite of \b
print(ss_3)

decimal_value ="mitesh01"
ss_4 = re.findall(r'\d',decimal_value)
print(ss_4)

ss_5 = re.findall(r'\D',decimal_value)
print(ss_5)

ss_6 = re.findall(r'\s',name)
print(ss_6)

ss_7 = re.findall(r'\S',name)
print(ss_7)

ss_8 = re.findall(r'\w',name)
print(ss_8)

ss_9 = re.findall(r'\W',name)
print(ss_9)

ss_10 = re.findall(r'r\Z',name)
print(ss_10)


# RegEx Sets

name = "mitesh amin hash"

rs_1 = re.findall(r'[ha]',name)
print(rs_1)

rs_2 = re.findall(r'[a-k]',name)
print(rs_2)

rs_3 = re.findall(r'[^mh]',name)
print(rs_3)

rs_4 = re.findall(r'[01]',decimal_value)
print(rs_4)

rs_5 = re.findall(r'[0-9]',decimal_value)
print(rs_5)

rs_6 = re.findall(r'[0-9][0-9]',decimal_value) #this check an 2 digite value
print(rs_6)

new_str = "Mitesh Amin"
rs_7 = re.findall(r'[a-zA-Z]',new_str)
print(rs_7)


# Function in RegEx

# findall
# search
str_new = 'John has Scored 90 marks. lisa has Scored 80 marks. David has Scored 70 marks.'

print(re.findall(r'\d+',str_new))
print(re.findall(r'[A-Z][a-z]+',str_new))

# Compile Function

compile_value = re.compile('[a-f]')
print(re.findall(compile_value,str_new))

# Split

print(re.split(r'\d+',str_new)) # this split by number

print(re.sub(r'\s+', '',str_new))
print(re.subn(r'\s+', '',str_new)) # given data in tuple format and also given a number of time changed value

print(re.escape(str_new))
search = re.search(r'\d+',str_new)
print(str_new[search.span()[0]:search.span()[1]])


# match object in RegEx

a = 'John has scored 90 marks'
mo_1 = re.search('\d+',a)
print(mo_1)
print(mo_1.re)
print(mo_1.string)
print(mo_1.start())
print(mo_1.end())
print(mo_1.group())
print(mo_1.start())

