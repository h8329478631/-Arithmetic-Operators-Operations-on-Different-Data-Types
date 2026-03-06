
# we have six arthemetic operators in python
#  +  -  *  /  //  %

# here we do opertaions on all datatypes:-

# Fundamental Datatypes --> int float bool complex string

# operations on Integer
''' 
Int1 = 5
Int2 = 2

print(Int1 + Int2)   # 7
print(Int1 - Int2)   # 3
print(Int1 * Int2)   # 10
print(Int1 / Int2)   # 2.5
print(Int1 // Int2)  # 2
print(Int1 % Int2)   # 1

# Value change

Int1 = 2
Int2 = 5

print(Int1 + Int2)   # 7
print(Int1 - Int2)   # -3
print(Int1 * Int2)   # 10
print(Int1 / Int2)   # 0.4
print(Int1 // Int2)  # 0
print(Int1 % Int2)   # 2
'''


# operations on Boolean
'''
bool1 = True
bool2 = True

print(bool1 + bool2)   # 2
print(bool1 - bool2)   # 0
print(bool1 * bool2)   # 1
print(bool1 / bool2)   # 1.0
print(bool1 // bool2)  # 1
print(bool1 % bool2)   # 0


bool1 = True
bool2 = False

print(bool1 + bool2)   # 1
print(bool1 - bool2)   # 1
print(bool1 * bool2)   # 0
# print(bool1 / bool2)   # ZeroDivisionError: division by zero
# print(bool1 // bool2)  # ZeroDivisionError: division by zero
# print(bool1 % bool2)   # ZeroDivisionError: division by zero


bool1 = False
bool2 = True

print(bool1 + bool2)   # 1
print(bool1 - bool2)   # -1
print(bool1 * bool2)   # 0
print(bool1 / bool2)   # 0.0
print(bool1 // bool2)  # 0
print(bool1 % bool2)   # 0


bool1 = False
bool2 = False

print(bool1 + bool2)   # 0
print(bool1 - bool2)   # 0
print(bool1 * bool2)   # 0
# print(bool1 / bool2)   # ZeroDivisionError: division by zero
# print(bool1 // bool2)  # ZeroDivisionError: division by zero
# print(bool1 % bool2)   # ZeroDivisionError: division by zero

'''

# operations on String

'''
Str1 = "harshal"
Str2 = "warke"

print(Str1 + Str2)   # harshalwarke
# print(Str1 - Str2)   # TypeError: unsupported operand type(s) for -: 'str' and 'str'
# print(Str1 * Str2)   # TypeError: can't multiply sequence by non-int of type 'str'
# print(Str1 / Str2)   # TypeError: unsupported operand type(s) for /: 'str' and 'str'
# print(Str1 // Str2)  # TypeError: unsupported operand type(s) for //: 'str' and 'str'
# print(Str1 % Str2)   # TypeError: not all arguments converted during string formatting

'''

# operations on Float

'''
Float1 = 4.0
Float2 = 5.0

print(Float1 + Float2)   # 9.0
print(Float1 - Float2)   # -1.0
print(Float1 * Float2)   # 20.5
print(Float1 / Float2)   # 0.8
print(Float1 // Float2)  # 0.0
print(Float1 % Float2)   # 4.0


# Value change

Float1 = 5.0
Float2 = 4.0

print(Float1 + Float2)   # 9.0
print(Float1 - Float2)   # 1.0
print(Float1 * Float2)   # 20.5
print(Float1 / Float2)   # 1.25
print(Float1 // Float2)  # 1.0
print(Float1 % Float2)   # 1.0

'''


# operations on Complex

'''
Comp1 = 5+10j
Comp2 = 3+8j

print(Comp1 + Comp2)   # (8+18j)
print(Comp1 - Comp2)   # (2+2j)
print(Comp1 * Comp2)   # (-65+70j)
print(Comp1 / Comp2)   # (1.3013698630136987-0.136986301369863j)
# print(Comp1 // Comp2)  # TypeError: unsupported operand type(s) for //: 'complex' and 'complex'
# print(Comp1 % Comp2)   # TypeError: unsupported operand type(s) for %: 'complex' and 'complex'

'''


# Collective Datatypes --> list tuple set frozenset dict 

# operations on List

'''
list1 = [1,2,3]
list2 = [4,5,6]

print(list1 + list2)   # [1, 2, 3, 4, 5, 6] --->  In Python, the + operator for lists is defined as concatenation, not addition.
# print(list1 - list2)   # TypeError: unsupported operand type(s) for -: 'list' and 'list'
# print(list1 * list2)   # TypeError: can't multiply sequence by non-int of type 'list'
# print(list1 / list2)   # TypeError: unsupported operand type(s) for /: 'list' and 'list'
# print(list1 // list2)  # TypeError: unsupported operand type(s) for //: 'list' and 'list'
# print(list1 % list2)   # TypeError: unsupported operand type(s) for %: 'list' and 'list'

'''

# operations on Tuple

'''
Tuple1 = (1,2,3)
Tuple2 = (4,5,6)

print(Tuple1 + Tuple2)   # (1, 2, 3, 4, 5, 6)
# print(Tuple1 - Tuple2)   # TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'
# print(Tuple1 * Tuple2)   # TypeError: can't multiply sequence by non-int of type 'tuple'
# print(Tuple1 / Tuple2)   # TypeError: unsupported operand type(s) for /: 'tuple' and 'tuple'
# print(Tuple1 // Tuple2)  # TypeError: unsupported operand type(s) for //: 'tuple' and 'tuple'
# print(Tuple1 % Tuple2)   # TypeError: unsupported operand type(s) for %: 'tuple' and 'tuple'

'''

# operations on Set

'''
Set1 = {1,2,3}
Set2 = {4,5,6}

# print(Set1 + Set2)   # TypeError: unsupported operand type(s) for +: 'set' and 'set'
# print(Set1 - Set2)   # TypeError: unsupported operand type(s) for *: 'set' and 'set'
# print(Set1 * Set2)   # TypeError: unsupported operand type(s) for *: 'set' and 'set'
# print(Set1 / Set2)   # TypeError: unsupported operand type(s) for /: 'set' and 'set'
# print(Set1 // Set2)  # TypeError: unsupported operand type(s) for //: 'set' and 'set'
# print(Set1 % Set2)   # TypeError: unsupported operand type(s) for %: 'set' and 'set'

'''

# operations on Frozenset

'''
Set1 = {1,2,3}
Set2 = {4,5,6}

Fset1 = frozenset(Set1)
Fset2 = frozenset(Set2)


# print(Fset1 + Fset2)   # TypeError: unsupported operand type(s) for +: 'frozenset' and 'frozenset'
# print(Fset1 - Fset2)   # TypeError: unsupported operand type(s) for -: 'frozenset' and 'frozenset'
# print(Fset1 * Fset2)   # TypeError: unsupported operand type(s) for *: 'frozenset' and 'frozenset'
# print(Fset1 / Fset2)   # TypeError: unsupported operand type(s) for /: 'frozenset' and 'frozenset'
# print(Fset1 // Fset2)  # TypeError: unsupported operand type(s) for //: 'frozenset' and 'frozenset'
# print(Fset1 % Fset2)   # TypeError: unsupported operand type(s) for *% 'frozenset' and 'frozenset'

'''

# operations on Dictionary

'''
Dict1 = {1:100,2:"shyam",3:20.5}
Dict2 = {1:50,2:"Sahane",3:10.5}

# print(Dict1 + Dict2)   # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# print(Dict1 - Dict2)   # TypeError: unsupported operand type(s) for -: 'dict' and 'dict'
# print(Dict1 * Dict2)   # TypeError: unsupported operand type(s) for *: 'dict' and 'dict'
# print(Dict1 / Dict2)   # TypeError: unsupported operand type(s) for /: 'dict' and 'dict'
# print(Dict1 // Dict2)  # TypeError: unsupported operand type(s) for //: 'dict' and 'dict'
# print(Dict1 % Dict2)   # TypeError: unsupported operand type(s) for %: 'dict' and 'dict'

'''



