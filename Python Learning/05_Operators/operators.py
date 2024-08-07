#Operators

# Arithmetic Operators:-
print("Arithmetic Operators:-")
print("1 + 2 :- ",1+2)
print("2 - 1 :- ",2-1)
print("20 / 2 :- ",20/2)
print("23 // 2 :- ",23//2)
print("100 % 2 :- ",100%2)
print("2 ** 3 :- ",2 ** 3)
print("\n")


# Assignment Operators:-
print("Assignment Operators:-")
data = 20
print("= :-",data)

a = 10
print("a =", a)
a += 3
print("a += 3 :-", a)

b = 20
print("b =", b)
b -= 5
print("b -= 20 :-", b)

c = 30
print("c =", c)
c *= 4
print("c *= 4 :-", c)

d = 40
print("d =", d)
d /= 4
print("d /= 4 :-", d)
print("\n")
# Comparison Operators
print("Comparison Operators:- ")
value = 10
Value = 20

print(f"{value} == {Value} :- ",value==Value)
print(f"{value} != {Value} :- ",value!=Value)
print(f"{value} > {Value} :- ",value>Value)
print(f"{value} < {Value} :- ",value<Value)
print(f"{value} >= {Value} :- ",value>=Value)
print(f"{value} <= {Value} :- ",value<=Value)

print("\n")

# Logical Operators
print("Logical Operators:- ")
value1 =10
value2 = 20
if value1 == value2 and value1<value2:
    print("AND:- ",True)
else:
    print("AND:- ",False)


if value1 == value2 or value1<value2:
    print("OR:- ",True)
else:
    print("AND:- ",False)

value = False
if not value:
    print("NOT:- ",True)
else:
    print("NOT:- ",False)
print("\n")
# Identity Operators

print("Identity Operators:- ")

dataInfo = 5
ValueInfo = dataInfo
print(f"{dataInfo} IS {ValueInfo}:- ", dataInfo is ValueInfo)

dataInfo = 5
ValueInfo = dataInfo
print(f"{dataInfo} ISNOT {ValueInfo}:- ", dataInfo is not ValueInfo)
print("\n")

# Membership Operators

print("Membership Operators:- ")

list = [1, 2, 3, 4, 5, 6, 7, 8]
value3 = 5
print(f"{value3} IN {list}:- ",value3 in list)
print(f"{value3} NOT IN {list}:- ",value3 not in list)
print("\n")
# Bitwise Operators


print("Bitwise Operators:- ")

result_and = 5 & 3  # Result: 1
print("Bitwise AND:- ",result_and)
result_or = 5 | 3  # Result: 7
print("Bitwise OR:- ",result_or)
result_not = ~5  # Result: -6
print("Bitwise NOT:- ",result_not)
result_xor = 5 ^ 3  # Result: 6
print("Bitwise XOR:- ",result_xor)
result_left_shift = 5 << 1  # Result: 10
print("Bitwise LEFT SHIFT:- ",result_left_shift)