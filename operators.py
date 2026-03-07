
# we have six arthemetic operators in python
#  +  -  *  /  //  %

# here we do opertaions on all datatypes:-


# Fundamental Datatypes --> int float bool complex string

# operations on Integer

Int1 = 5
Int2 = 2
'''
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

'''

bool1 = True
bool2 = False

'''
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


Str1 = "harshal"
Str2 = "warke"

'''
print(Str1 + Str2)   # harshalwarke
# print(Str1 - Str2)   # TypeError: unsupported operand type(s) for -: 'str' and 'str'
# print(Str1 * Str2)   # TypeError: can't multiply sequence by non-int of type 'str'
# print(Str1 / Str2)   # TypeError: unsupported operand type(s) for /: 'str' and 'str'
# print(Str1 // Str2)  # TypeError: unsupported operand type(s) for //: 'str' and 'str'
# print(Str1 % Str2)   # TypeError: not all arguments converted during string formatting

'''

# operations on Float


Float1 = 4.0
Float2 = 5.0

'''
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


Comp1 = 5+10j
Comp2 = 3+8j

'''
print(Comp1 + Comp2)   # (8+18j)
print(Comp1 - Comp2)   # (2+2j)
print(Comp1 * Comp2)   # (-65+70j)
print(Comp1 / Comp2)   # (1.3013698630136987-0.136986301369863j)
# print(Comp1 // Comp2)  # TypeError: unsupported operand type(s) for //: 'complex' and 'complex'
# print(Comp1 % Comp2)   # TypeError: unsupported operand type(s) for %: 'complex' and 'complex'

'''


# Collective Datatypes --> list tuple set frozenset dict 

# operations on List

list1 = [1,2,3]
list2 = [4,5,6]

'''
print(list1 + list2)   # [1, 2, 3, 4, 5, 6] --->  In Python, the + operator for lists is defined as concatenation, not addition.
# print(list1 - list2)   # TypeError: unsupported operand type(s) for -: 'list' and 'list'
# print(list1 * list2)   # TypeError: can't multiply sequence by non-int of type 'list'
# print(list1 / list2)   # TypeError: unsupported operand type(s) for /: 'list' and 'list'
# print(list1 // list2)  # TypeError: unsupported operand type(s) for //: 'list' and 'list'
# print(list1 % list2)   # TypeError: unsupported operand type(s) for %: 'list' and 'list'

'''

# operations on Tuple


Tuple1 = (1,2,3)
Tuple2 = (4,5,6)

'''
print(Tuple1 + Tuple2)   # (1, 2, 3, 4, 5, 6)
# print(Tuple1 - Tuple2)   # TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'
# print(Tuple1 * Tuple2)   # TypeError: can't multiply sequence by non-int of type 'tuple'
# print(Tuple1 / Tuple2)   # TypeError: unsupported operand type(s) for /: 'tuple' and 'tuple'
# print(Tuple1 // Tuple2)  # TypeError: unsupported operand type(s) for //: 'tuple' and 'tuple'
# print(Tuple1 % Tuple2)   # TypeError: unsupported operand type(s) for %: 'tuple' and 'tuple'

'''

# operations on Set


Set1 = {1,2,3}
Set2 = {4,5,6}

'''
# print(Set1 + Set2)   # TypeError: unsupported operand type(s) for +: 'set' and 'set'
# print(Set1 - Set2)   # TypeError: unsupported operand type(s) for *: 'set' and 'set'
# print(Set1 * Set2)   # TypeError: unsupported operand type(s) for *: 'set' and 'set'
# print(Set1 / Set2)   # TypeError: unsupported operand type(s) for /: 'set' and 'set'
# print(Set1 // Set2)  # TypeError: unsupported operand type(s) for //: 'set' and 'set'
# print(Set1 % Set2)   # TypeError: unsupported operand type(s) for %: 'set' and 'set'

'''

# operations on Frozenset


Fset1 = frozenset(Set1)
Fset2 = frozenset(Set2)

'''

# print(Fset1 + Fset2)   # TypeError: unsupported operand type(s) for +: 'frozenset' and 'frozenset'
# print(Fset1 - Fset2)   # TypeError: unsupported operand type(s) for -: 'frozenset' and 'frozenset'
# print(Fset1 * Fset2)   # TypeError: unsupported operand type(s) for *: 'frozenset' and 'frozenset'
# print(Fset1 / Fset2)   # TypeError: unsupported operand type(s) for /: 'frozenset' and 'frozenset'
# print(Fset1 // Fset2)  # TypeError: unsupported operand type(s) for //: 'frozenset' and 'frozenset'
# print(Fset1 % Fset2)   # TypeError: unsupported operand type(s) for *% 'frozenset' and 'frozenset'

'''

# operations on Dictionary


Dict1 = {1:100,2:"shyam",3:20.5}
Dict2 = {1:50,2:"Sahane",3:10.5}

'''
# print(Dict1 + Dict2)   # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# print(Dict1 - Dict2)   # TypeError: unsupported operand type(s) for -: 'dict' and 'dict'
# print(Dict1 * Dict2)   # TypeError: unsupported operand type(s) for *: 'dict' and 'dict'
# print(Dict1 / Dict2)   # TypeError: unsupported operand type(s) for /: 'dict' and 'dict'
# print(Dict1 // Dict2)  # TypeError: unsupported operand type(s) for //: 'dict' and 'dict'
# print(Dict1 % Dict2)   # TypeError: unsupported operand type(s) for %: 'dict' and 'dict'

'''


##here we are do operations one datatype with all different datatypes

# Int With All Others Datatypes

# Int With Boolean
'''
# here Int = 5 and bool1 = True
print(Int1 + bool1)   # 6
print(Int1 - bool1)   # 4
print(Int1 * bool1)   # 5
print(Int1 / bool1)   # 5.0
print(Int1 // bool1)  # 5
print(Int1 % bool1)   # 0

# here Int = 5 and bool2bool2 = False
print(Int1 + bool2)   # 5
print(Int1 - bool2)   # 5
print(Int1 * bool2)   # 0
# print(Int1 / bool2)   # ZeroDivisionError: division by zero
# print(Int1 // bool2)  # ZeroDivisionError: division by zero
# print(Int1 % bool2)   # ZeroDivisionError: division by zero

'''

# Int With Str
'''

# here Int = 5 and Str1 = "harshal"
# print(Int1 + Str1)   # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(Int1 - Str1)   # TypeError: unsupported operand type(s) for -: 'int' and 'str'
print(Int1 * Str1)   # harshalharshalharshalharshalharshal
# print(Int1 / Str1)   # TypeError: unsupported operand type(s) for /: 'int' and 'str'
# print(Int1 // Str1)  # TypeError: unsupported operand type(s) for //: 'int' and 'str'
# print(Int1 % Str1)   # TypeError: unsupported operand type(s) for %: 'int' and 'str'

'''

# Int With Float

'''
# here Int = 5 and Float1 = 4.0

print(Int1 + Float1)   # 9.0
print(Int1 - Float1)   # 1.0
print(Int1 * Float1)   # 20.0
print(Int1 / Float1)   # 1.25
print(Int1 // Float1)  # 1.0
print(Int1 % Float1)   # 1.0
'''

# Int With Complex

'''
# here Int = 5 and Comp1 = 5+10j

print(Int1 + Comp1)   # (10+10j)
print(Int1 - Comp1)   # -10j
print(Int1 * Comp1)   # (25+50j)
print(Int1 / Comp1)   # (0.2-0.4j)
# print(Int1 // Comp1)  # TypeError: unsupported operand type(s) for //: 'int' and 'complex'
# print(Int1 % Comp1)   # TypeError: unsupported operand type(s) for %: 'int' and 'complex'

'''

# Int With List

'''
# here Int = 5 and list1 = [1,2,3]

# print(Int1 + list1)   # TypeError: unsupported operand type(s) for +: 'int' and 'list'
# print(Int1 - list1)   # TypeError: unsupported operand type(s) for -: 'int' and 'list'
print(Int1 * list1)   # [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
# print(Int1 / list1)   # TypeError: unsupported operand type(s) for /: 'int' and 'list'
# print(Int1 // list1)  # TypeError: unsupported operand type(s) for //: 'int' and 'list'
# print(Int1 % list1)   # TypeError: unsupported operand type(s) for %: 'int' and 'list'
'''

# Int With Tuple

'''
# here Int = 5 and Tuple1 = (1,2,3)

# print(Int1 + Tuple1)   # TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
# print(Int1 - Tuple1)   # TypeError: unsupported operand type(s) for -: 'int' and 'tuple'
print(Int1 * Tuple1)   # (1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
# print(Int1 / Tuple1)   # TypeError: unsupported operand type(s) for /: 'int' and 'tuple'
# print(Int1 // Tuple1)  # TypeError: unsupported operand type(s) for //: 'int' and 'tuple'
# print(Int1 % Tuple1)   # TypeError: unsupported operand type(s) for %: 'int' and 'tuple'

'''


# Int With Set

'''
# here Int = 5 and Set1 = {1,2,3}

# print(Int1 + Set1)   # TypeError: unsupported operand type(s) for +: 'int' and 'set'
# print(Int1 - Set1)   # TypeError: unsupported operand type(s) for -: 'int' and 'set'
# print(Int1 * Set1)   # TypeError: unsupported operand type(s) for *: 'int' and 'set'
# print(Int1 / Set1)   # TypeError: unsupported operand type(s) for /: 'int' and 'set'
# print(Int1 // Set1)  # TypeError: unsupported operand type(s) for //: 'int' and 'set'
# print(Int1 % Set1)   # TypeError: unsupported operand type(s) for %: 'int' and 'set'

'''


# Int With Frozenset

'''
# here Int = 5 and Fset1 = frozenset({1,2,3})

# print(Int1 + Fset1)   # TypeError: unsupported operand type(s) for +: 'int' and 'frozenset'
# print(Int1 - Fset1)   # TypeError: unsupported operand type(s) for -: 'int' and 'frozenset'
# print(Int1 * Fset1)   # TypeError: unsupported operand type(s) for *: 'int' and 'frozenset'
# print(Int1 / Fset1)   # TypeError: unsupported operand type(s) for /: 'int' and 'frozenset'
# print(Int1 // Fset1)  # TypeError: unsupported operand type(s) for //: 'int' and 'frozenset'
# print(Int1 % Fset1)   # TypeError: unsupported operand type(s) for %: 'int' and 'frozenset'

'''


# Int With Dictionary

'''
# here Int = 5 and Dict1 = {1:100,2:"shyam",3:20.5}

# print(Int1 + Dict1)   # TypeError: unsupported operand type(s) for +: 'int' and 'dict'
# print(Int1 - Dict1)   # TypeError: unsupported operand type(s) for -: 'int' and 'dict'
# print(Int1 * Dict1)   # TypeError: unsupported operand type(s) for *: 'int' and 'dict'
# print(Int1 / Dict1)   # TypeError: unsupported operand type(s) for /: 'int' and 'dict'
# print(Int1 // Dict1)  # TypeError: unsupported operand type(s) for //: 'int' and 'dict'
# print(Int1 % Dict1)   # TypeError: unsupported operand type(s) for %: 'int' and 'dict'

'''



# Float With All Other Datatypes


# Float With Boolean
'''
# here Float1 = 4.0 and bool1 = True

print(Float1 + bool1)   # 5.0
print(Float1 - bool1)   # 3.0
print(Float1 * bool1)   # 4.0
print(Float1 / bool1)   # 4.0
print(Float1 // bool1)  # 4.0
print(Float1 % bool1)   # 0.0


# here Float1 = 4.0 and bool2 = False

print(Float1 + bool2)   # 4.0
print(Float1 - bool2)   # 4.0
print(Float1 * bool2)   # 0.0
# print(Float1 / bool2)   # ZeroDivisionError: division by zero
# print(Float1 // bool2)  # ZeroDivisionError: division by zero
# print(Float1 % bool2)   # ZeroDivisionError: division by zero
'''


# Float With String
'''
# here Float1 = 4.0 and Str1 = "harshal"

# print(Float1 + Str1)   # TypeError: unsupported operand type(s) for +: 'float' and 'str'
# print(Float1 - Str1)   # TypeError: unsupported operand type(s) for -: 'float' and 'str'
# print(Float1 * Str1)   # TypeError: can't multiply sequence by non-int of type 'float'
# print(Float1 / Str1)   # TypeError: unsupported operand type(s) for /: 'float' and 'str'
# print(Float1 // Str1)  # TypeError: unsupported operand type(s) for //: 'float' and 'str'
# print(Float1 % Str1)   # TypeError: unsupported operand type(s) for %: 'float' and 'str'
'''


# Float With Integer
'''
# here Float1 = 4.0 and Int1 = 5

print(Float1 + Int1)   # 9.0
print(Float1 - Int1)   # -1.0
print(Float1 * Int1)   # 20.0
print(Float1 / Int1)   # 0.8
print(Float1 // Int1)  # 0.0
print(Float1 % Int1)   # 4.0
'''


# Float With Complex
'''
# here Float1 = 4.0 and Comp1 = 5+10j

print(Float1 + Comp1)   # (9+10j)
print(Float1 - Comp1)   # (-1-10j)
print(Float1 * Comp1)   # (20+40j)
print(Float1 / Comp1)   # (0.16-0.32j)
# print(Float1 // Comp1)  # TypeError
# print(Float1 % Comp1)   # TypeError
'''


# Float With List
'''
# here Float1 = 4.0 and list1 = [1,2,3]

# print(Float1 + list1)   # TypeError
# print(Float1 - list1)   # TypeError
# print(Float1 * list1)   # TypeError
# print(Float1 / list1)   # TypeError
# print(Float1 // list1)  # TypeError
# print(Float1 % list1)   # TypeError
'''


# Float With Tuple
'''
# here Float1 = 4.0 and Tuple1 = (1,2,3)

# print(Float1 + Tuple1)   # TypeError
# print(Float1 - Tuple1)   # TypeError
# print(Float1 * Tuple1)   # TypeError
# print(Float1 / Tuple1)   # TypeError
# print(Float1 // Tuple1)  # TypeError
# print(Float1 % Tuple1)   # TypeError
'''


# Float With Set
'''
# here Float1 = 4.0 and Set1 = {1,2,3}

# print(Float1 + Set1)   # TypeError
# print(Float1 - Set1)   # TypeError
# print(Float1 * Set1)   # TypeError
# print(Float1 / Set1)   # TypeError
# print(Float1 // Set1)  # TypeError
# print(Float1 % Set1)   # TypeError
'''


# Float With Frozenset
'''
# here Float1 = 4.0 and Fset1 = frozenset({1,2,3})

# print(Float1 + Fset1)   # TypeError
# print(Float1 - Fset1)   # TypeError
# print(Float1 * Fset1)   # TypeError
# print(Float1 / Fset1)   # TypeError
# print(Float1 // Fset1)  # TypeError
# print(Float1 % Fset1)   # TypeError
'''


# Float With Dictionary
'''
# here Float1 = 4.0 and Dict1 = {1:100,2:"shyam",3:20.5}

# print(Float1 + Dict1)   # TypeError
# print(Float1 - Dict1)   # TypeError
# print(Float1 * Dict1)   # TypeError
# print(Float1 / Dict1)   # TypeError
# print(Float1 // Dict1)  # TypeError
# print(Float1 % Dict1)   # TypeError
'''


# Bool With All Other Datatypes


# Bool With Integer
'''
# here bool1 = True and Int1 = 5

print(bool1 + Int1)   # 6
print(bool1 - Int1)   # -4
print(bool1 * Int1)   # 5
print(bool1 / Int1)   # 0.2
print(bool1 // Int1)  # 0
print(bool1 % Int1)   # 1


# here bool2 = False and Int1 = 5

print(bool2 + Int1)   # 5
print(bool2 - Int1)   # -5
print(bool2 * Int1)   # 0
print(bool2 / Int1)   # 0.0
print(bool2 // Int1)  # 0
print(bool2 % Int1)   # 0
'''


# Bool With Float
'''
# here bool1 = True and Float1 = 4.0

print(bool1 + Float1)   # 5.0
print(bool1 - Float1)   # -3.0
print(bool1 * Float1)   # 4.0
print(bool1 / Float1)   # 0.25
print(bool1 // Float1)  # 0.0
print(bool1 % Float1)   # 1.0


# here bool2 = False and Float1 = 4.0

print(bool2 + Float1)   # 4.0
print(bool2 - Float1)   # -4.0
print(bool2 * Float1)   # 0.0
print(bool2 / Float1)   # 0.0
print(bool2 // Float1)  # 0.0
print(bool2 % Float1)   # 0.0
'''


# Bool With String
'''
# here bool1 = True and Str1 = "harshal"

# print(bool1 + Str1)   # TypeError
# print(bool1 - Str1)   # TypeError
print(bool1 * Str1)   # harshal
# print(bool1 / Str1)   # TypeError
# print(bool1 // Str1)  # TypeError
# print(bool1 % Str1)   # TypeError
'''


# Bool With Complex
'''
# here bool1 = True and Comp1 = 5+10j

print(bool1 + Comp1)   # (6+10j)
print(bool1 - Comp1)   # (-4-10j)
print(bool1 * Comp1)   # (5+10j)
print(bool1 / Comp1)   # (0.04-0.08j)
# print(bool1 // Comp1)  # TypeError
# print(bool1 % Comp1)   # TypeError
'''


# Bool With List
'''
# here bool1 = True and list1 = [1,2,3]

print(bool1 * list1)   # [1, 2, 3]

# print(bool1 + list1)   # TypeError
# print(bool1 - list1)   # TypeError
# print(bool1 / list1)   # TypeError
# print(bool1 // list1)  # TypeError
# print(bool1 % list1)   # TypeError
'''


# Bool With Tuple
'''
# here bool1 = True and Tuple1 = (1,2,3)

print(bool1 * Tuple1)   # (1, 2, 3)

# print(bool1 + Tuple1)   # TypeError
# print(bool1 - Tuple1)   # TypeError
# print(bool1 / Tuple1)   # TypeError
# print(bool1 // Tuple1)  # TypeError
# print(bool1 % Tuple1)   # TypeError
'''


# Bool With Set
'''
# here bool1 = True and Set1 = {1,2,3}

# print(bool1 + Set1)   # TypeError
# print(bool1 - Set1)   # TypeError
# print(bool1 * Set1)   # TypeError
# print(bool1 / Set1)   # TypeError
# print(bool1 // Set1)  # TypeError
# print(bool1 % Set1)   # TypeError
'''


# Bool With Frozenset
'''
# here bool1 = True and Fset1 = frozenset({1,2,3})

# print(bool1 + Fset1)   # TypeError
# print(bool1 - Fset1)   # TypeError
# print(bool1 * Fset1)   # TypeError
# print(bool1 / Fset1)   # TypeError
# print(bool1 // Fset1)  # TypeError
# print(bool1 % Fset1)   # TypeError
'''


# Bool With Dictionary
'''
# here bool1 = True and Dict1 = {1:100,2:"shyam",3:20.5}

# print(bool1 + Dict1)   # TypeError
# print(bool1 - Dict1)   # TypeError
# print(bool1 * Dict1)   # TypeError
# print(bool1 / Dict1)   # TypeError
# print(bool1 // Dict1)  # TypeError
# print(bool1 % Dict1)   # TypeError
'''


# Str With All Other Datatypes


# Str With Integer
'''
# here Str1 = "harshal" and Int1 = 5

# print(Str1 + Int1)   # TypeError: can only concatenate str (not "int") to str
# print(Str1 - Int1)   # TypeError
print(Str1 * Int1)   # harshalharshalharshalharshalharshal
# print(Str1 / Int1)   # TypeError
# print(Str1 // Int1)  # TypeError
# print(Str1 % Int1)   # TypeError
'''


# Str With Float
'''
# here Str1 = "harshal" and Float1 = 4.0

# print(Str1 + Float1)   # TypeError
# print(Str1 - Float1)   # TypeError
# print(Str1 * Float1)   # TypeError: can't multiply sequence by non-int of type 'float'
# print(Str1 / Float1)   # TypeError
# print(Str1 // Float1)  # TypeError
# print(Str1 % Float1)   # TypeError
'''


# Str With Boolean
'''
# here Str1 = "harshal" and bool1 = True

# print(Str1 + bool1)   # TypeError
# print(Str1 - bool1)   # TypeError
print(Str1 * bool1)   # harshal
# print(Str1 / bool1)   # TypeError
# print(Str1 // bool1)  # TypeError
# print(Str1 % bool1)   # TypeError
'''


# Str With Complex
'''
# here Str1 = "harshal" and Comp1 = 5+10j

# print(Str1 + Comp1)   # TypeError
# print(Str1 - Comp1)   # TypeError
# print(Str1 * Comp1)   # TypeError
# print(Str1 / Comp1)   # TypeError
# print(Str1 // Comp1)  # TypeError
# print(Str1 % Comp1)   # TypeError
'''


# Str With List
'''
# here Str1 = "harshal" and list1 = [1,2,3]

# print(Str1 + list1)   # TypeError
# print(Str1 - list1)   # TypeError
# print(Str1 * list1)   # TypeError
# print(Str1 / list1)   # TypeError
# print(Str1 // list1)  # TypeError
# print(Str1 % list1)   # TypeError
'''


# Str With Tuple
'''
# here Str1 = "harshal" and Tuple1 = (1,2,3)

# print(Str1 + Tuple1)   # TypeError
# print(Str1 - Tuple1)   # TypeError
# print(Str1 * Tuple1)   # TypeError
# print(Str1 / Tuple1)   # TypeError
# print(Str1 // Tuple1)  # TypeError
# print(Str1 % Tuple1)   # TypeError
'''


# Str With Set
'''
# here Str1 = "harshal" and Set1 = {1,2,3}

# print(Str1 + Set1)   # TypeError
# print(Str1 - Set1)   # TypeError
# print(Str1 * Set1)   # TypeError
# print(Str1 / Set1)   # TypeError
# print(Str1 // Set1)  # TypeError
# print(Str1 % Set1)   # TypeError
'''


# Str With Frozenset
'''
# here Str1 = "harshal" and Fset1 = frozenset({1,2,3})

# print(Str1 + Fset1)   # TypeError
# print(Str1 - Fset1)   # TypeError
# print(Str1 * Fset1)   # TypeError
# print(Str1 / Fset1)   # TypeError
# print(Str1 // Fset1)  # TypeError
# print(Str1 % Fset1)   # TypeError
'''


# Str With Dictionary
'''
# here Str1 = "harshal" and Dict1 = {1:100,2:"shyam",3:20.5}

# print(Str1 + Dict1)   # TypeError
# print(Str1 - Dict1)   # TypeError
# print(Str1 * Dict1)   # TypeError
# print(Str1 / Dict1)   # TypeError
# print(Str1 // Dict1)  # TypeError
# print(Str1 % Dict1)   # TypeError
'''

# Complex With All Other Datatypes


# Complex With Integer
'''
# here Comp1 = 5+10j and Int1 = 5

print(Comp1 + Int1)   # (10+10j)
print(Comp1 - Int1)   # 10j
print(Comp1 * Int1)   # (25+50j)
print(Comp1 / Int1)   # (1+2j)
# print(Comp1 // Int1)  # TypeError
# print(Comp1 % Int1)   # TypeError
'''


# Complex With Float
'''
# here Comp1 = 5+10j and Float1 = 4.0

print(Comp1 + Float1)   # (9+10j)
print(Comp1 - Float1)   # (1+10j)
print(Comp1 * Float1)   # (20+40j)
print(Comp1 / Float1)   # (1.25+2.5j)
# print(Comp1 // Float1)  # TypeError
# print(Comp1 % Float1)   # TypeError
'''


# Complex With Boolean
'''
# here Comp1 = 5+10j and bool1 = True

print(Comp1 + bool1)   # (6+10j)
print(Comp1 - bool1)   # (4+10j)
print(Comp1 * bool1)   # (5+10j)
print(Comp1 / bool1)   # (5+10j)
# print(Comp1 // bool1)  # TypeError
# print(Comp1 % bool1)   # TypeError
'''


# Complex With String
'''
# here Comp1 = 5+10j and Str1 = "harshal"

# print(Comp1 + Str1)   # TypeError
# print(Comp1 - Str1)   # TypeError
# print(Comp1 * Str1)   # TypeError
# print(Comp1 / Str1)   # TypeError
# print(Comp1 // Str1)  # TypeError
# print(Comp1 % Str1)   # TypeError
'''


# Complex With List
'''
# here Comp1 = 5+10j and list1 = [1,2,3]

# print(Comp1 + list1)   # TypeError
# print(Comp1 - list1)   # TypeError
# print(Comp1 * list1)   # TypeError
# print(Comp1 / list1)   # TypeError
# print(Comp1 // list1)  # TypeError
# print(Comp1 % list1)   # TypeError
'''


# Complex With Tuple
'''
# here Comp1 = 5+10j and Tuple1 = (1,2,3)

# print(Comp1 + Tuple1)   # TypeError
# print(Comp1 - Tuple1)   # TypeError
# print(Comp1 * Tuple1)   # TypeError
# print(Comp1 / Tuple1)   # TypeError
# print(Comp1 // Tuple1)  # TypeError
# print(Comp1 % Tuple1)   # TypeError
'''


# Complex With Set
'''
# here Comp1 = 5+10j and Set1 = {1,2,3}

# print(Comp1 + Set1)   # TypeError
# print(Comp1 - Set1)   # TypeError
# print(Comp1 * Set1)   # TypeError
# print(Comp1 / Set1)   # TypeError
# print(Comp1 // Set1)  # TypeError
# print(Comp1 % Set1)   # TypeError
'''


# Complex With Frozenset
'''
# here Comp1 = 5+10j and Fset1 = frozenset({1,2,3})

# print(Comp1 + Fset1)   # TypeError
# print(Comp1 - Fset1)   # TypeError
# print(Comp1 * Fset1)   # TypeError
# print(Comp1 / Fset1)   # TypeError
# print(Comp1 // Fset1)  # TypeError
# print(Comp1 % Fset1)   # TypeError
'''


# Complex With Dictionary
'''
# here Comp1 = 5+10j and Dict1 = {1:100,2:"shyam",3:20.5}

# print(Comp1 + Dict1)   # TypeError
# print(Comp1 - Dict1)   # TypeError
# print(Comp1 * Dict1)   # TypeError
# print(Comp1 / Dict1)   # TypeError
# print(Comp1 // Dict1)  # TypeError
# print(Comp1 % Dict1)   # TypeError
'''

# List With All Other Datatypes


# List With Integer
'''
# here list1 = [1,2,3] and Int1 = 5

# print(list1 + Int1)   # TypeError: can only concatenate list (not "int") to list
# print(list1 - Int1)   # TypeError
print(list1 * Int1)   # [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3]
# print(list1 / Int1)   # TypeError
# print(list1 // Int1)  # TypeError
# print(list1 % Int1)   # TypeError
'''


# List With Float
'''
# here list1 = [1,2,3] and Float1 = 4.0

# print(list1 + Float1)   # TypeError
# print(list1 - Float1)   # TypeError
# print(list1 * Float1)   # TypeError: can't multiply sequence by non-int of type 'float'
# print(list1 / Float1)   # TypeError
# print(list1 // Float1)  # TypeError
# print(list1 % Float1)   # TypeError
'''


# List With Boolean
'''
# here list1 = [1,2,3] and bool1 = True

# print(list1 + bool1)   # TypeError
# print(list1 - bool1)   # TypeError
print(list1 * bool1)   # [1,2,3]
# print(list1 / bool1)   # TypeError
# print(list1 // bool1)  # TypeError
# print(list1 % bool1)   # TypeError
'''


# List With String
'''
# here list1 = [1,2,3] and Str1 = "harshal"

# print(list1 + Str1)   # TypeError
# print(list1 - Str1)   # TypeError
# print(list1 * Str1)   # TypeError
# print(list1 / Str1)   # TypeError
# print(list1 // Str1)  # TypeError
# print(list1 % Str1)   # TypeError
'''


# List With Complex
'''
# here list1 = [1,2,3] and Comp1 = 5+10j

# print(list1 + Comp1)   # TypeError
# print(list1 - Comp1)   # TypeError
# print(list1 * Comp1)   # TypeError
# print(list1 / Comp1)   # TypeError
# print(list1 // Comp1)  # TypeError
# print(list1 % Comp1)   # TypeError
'''


# List With Tuple
'''
# here list1 = [1,2,3] and Tuple1 = (1,2,3)

# print(list1 + Tuple1)   # TypeError
# print(list1 - Tuple1)   # TypeError
# print(list1 * Tuple1)   # TypeError
# print(list1 / Tuple1)   # TypeError
# print(list1 // Tuple1)  # TypeError
# print(list1 % Tuple1)   # TypeError
'''


# List With Set
'''
# here list1 = [1,2,3] and Set1 = {1,2,3}

# print(list1 + Set1)   # TypeError
# print(list1 - Set1)   # TypeError
# print(list1 * Set1)   # TypeError
# print(list1 / Set1)   # TypeError
# print(list1 // Set1)  # TypeError
# print(list1 % Set1)   # TypeError
'''


# List With Frozenset
'''
# here list1 = [1,2,3] and Fset1 = frozenset({1,2,3})

# print(list1 + Fset1)   # TypeError
# print(list1 - Fset1)   # TypeError
# print(list1 * Fset1)   # TypeError
# print(list1 / Fset1)   # TypeError
# print(list1 // Fset1)  # TypeError
# print(list1 % Fset1)   # TypeError
'''


# List With Dictionary
'''
# here list1 = [1,2,3] and Dict1 = {1:100,2:"shyam",3:20.5}

# print(list1 + Dict1)   # TypeError
# print(list1 - Dict1)   # TypeError
# print(list1 * Dict1)   # TypeError
# print(list1 / Dict1)   # TypeError
# print(list1 // Dict1)  # TypeError
# print(list1 % Dict1)   # TypeError
'''


# Tuple With All Other Datatypes


# Tuple With Integer
'''
# here Tuple1 = (1,2,3) and Int1 = 5

# print(Tuple1 + Int1)   # TypeError: can only concatenate tuple (not "int") to tuple
# print(Tuple1 - Int1)   # TypeError
print(Tuple1 * Int1)   # (1,2,3,1,2,3,1,2,3,1,2,3,1,2,3)
# print(Tuple1 / Int1)   # TypeError
# print(Tuple1 // Int1)  # TypeError
# print(Tuple1 % Int1)   # TypeError
'''


# Tuple With Float
'''
# here Tuple1 = (1,2,3) and Float1 = 4.0

# print(Tuple1 + Float1)   # TypeError
# print(Tuple1 - Float1)   # TypeError
# print(Tuple1 * Float1)   # TypeError: can't multiply sequence by non-int of type 'float'
# print(Tuple1 / Float1)   # TypeError
# print(Tuple1 // Float1)  # TypeError
# print(Tuple1 % Float1)   # TypeError
'''


# Tuple With Boolean
'''
# here Tuple1 = (1,2,3) and bool1 = True

# print(Tuple1 + bool1)   # TypeError
# print(Tuple1 - bool1)   # TypeError
print(Tuple1 * bool1)   # (1,2,3)
# print(Tuple1 / bool1)   # TypeError
# print(Tuple1 // bool1)  # TypeError
# print(Tuple1 % bool1)   # TypeError
'''


# Tuple With String
'''
# here Tuple1 = (1,2,3) and Str1 = "harshal"

# print(Tuple1 + Str1)   # TypeError
# print(Tuple1 - Str1)   # TypeError
# print(Tuple1 * Str1)   # TypeError
# print(Tuple1 / Str1)   # TypeError
# print(Tuple1 // Str1)  # TypeError
# print(Tuple1 % Str1)   # TypeError
'''


# Tuple With Complex
'''
# here Tuple1 = (1,2,3) and Comp1 = 5+10j

# print(Tuple1 + Comp1)   # TypeError
# print(Tuple1 - Comp1)   # TypeError
# print(Tuple1 * Comp1)   # TypeError
# print(Tuple1 / Comp1)   # TypeError
# print(Tuple1 // Comp1)  # TypeError
# print(Tuple1 % Comp1)   # TypeError
'''


# Tuple With List
'''
# here Tuple1 = (1,2,3) and list1 = [1,2,3]

# print(Tuple1 + list1)   # TypeError
# print(Tuple1 - list1)   # TypeError
# print(Tuple1 * list1)   # TypeError
# print(Tuple1 / list1)   # TypeError
# print(Tuple1 // list1)  # TypeError
# print(Tuple1 % list1)   # TypeError
'''


# Tuple With Set
'''
# here Tuple1 = (1,2,3) and Set1 = {1,2,3}

# print(Tuple1 + Set1)   # TypeError
# print(Tuple1 - Set1)   # TypeError
# print(Tuple1 * Set1)   # TypeError
# print(Tuple1 / Set1)   # TypeError
# print(Tuple1 // Set1)  # TypeError
# print(Tuple1 % Set1)   # TypeError
'''


# Tuple With Frozenset
'''
# here Tuple1 = (1,2,3) and Fset1 = frozenset({1,2,3})

# print(Tuple1 + Fset1)   # TypeError
# print(Tuple1 - Fset1)   # TypeError
# print(Tuple1 * Fset1)   # TypeError
# print(Tuple1 / Fset1)   # TypeError
# print(Tuple1 // Fset1)  # TypeError
# print(Tuple1 % Fset1)   # TypeError
'''


# Tuple With Dictionary
'''
# here Tuple1 = (1,2,3) and Dict1 = {1:100,2:"shyam",3:20.5}

# print(Tuple1 + Dict1)   # TypeError
# print(Tuple1 - Dict1)   # TypeError
# print(Tuple1 * Dict1)   # TypeError
# print(Tuple1 / Dict1)   # TypeError
# print(Tuple1 // Dict1)  # TypeError
# print(Tuple1 % Dict1)   # TypeError
'''


# Set With Integer
'''
# here Set1 = {1,2,3} and Int1 = 5

# print(Set1 + Int1)   # TypeError
# print(Set1 - Int1)   # TypeError
# print(Set1 * Int1)   # TypeError
# print(Set1 / Int1)   # TypeError
# print(Set1 // Int1)  # TypeError
# print(Set1 % Int1)   # TypeError
'''


# Set With Float
'''
# here Set1 = {1,2,3} and Float1 = 4.0

# print(Set1 + Float1)   # TypeError
# print(Set1 - Float1)   # TypeError
# print(Set1 * Float1)   # TypeError
# print(Set1 / Float1)   # TypeError
# print(Set1 // Float1)  # TypeError
# print(Set1 % Float1)   # TypeError
'''


# Set With Boolean
'''
# here Set1 = {1,2,3} and bool1 = True

# print(Set1 + bool1)   # TypeError
# print(Set1 - bool1)   # TypeError
# print(Set1 * bool1)   # TypeError
# print(Set1 / bool1)   # TypeError
# print(Set1 // bool1)  # TypeError
# print(Set1 % bool1)   # TypeError
'''


# Set With Complex
'''
# here Set1 = {1,2,3} and Comp1 = 5+10j

# print(Set1 + Comp1)   # TypeError
# print(Set1 - Comp1)   # TypeError
# print(Set1 * Comp1)   # TypeError
# print(Set1 / Comp1)   # TypeError
# print(Set1 // Comp1)  # TypeError
# print(Set1 % Comp1)   # TypeError
'''


# Set With String
'''
# here Set1 = {1,2,3} and Str1 = "harshal"

# print(Set1 + Str1)   # TypeError
# print(Set1 - Str1)   # TypeError
# print(Set1 * Str1)   # TypeError
# print(Set1 / Str1)   # TypeError
# print(Set1 // Str1)  # TypeError
# print(Set1 % Str1)   # TypeError
'''


# Set With List
'''
# here Set1 = {1,2,3} and list1 = [1,2,3]

# print(Set1 + list1)   # TypeError
# print(Set1 - list1)   # TypeError
# print(Set1 * list1)   # TypeError
# print(Set1 / list1)   # TypeError
# print(Set1 // list1)  # TypeError
# print(Set1 % list1)   # TypeError
'''


# Set With Tuple
'''
# here Set1 = {1,2,3} and Tuple1 = (1,2,3)

# print(Set1 + Tuple1)   # TypeError
# print(Set1 - Tuple1)   # TypeError
# print(Set1 * Tuple1)   # TypeError
# print(Set1 / Tuple1)   # TypeError
# print(Set1 // Tuple1)  # TypeError
# print(Set1 % Tuple1)   # TypeError
'''


# Set With Frozenset
'''
# here Set1 = {1,2,3} and Fset1 = frozenset({1,2,3})

# print(Set1 + Fset1)   # TypeError
# print(Set1 - Fset1)   # TypeError
# print(Set1 * Fset1)   # TypeError
# print(Set1 / Fset1)   # TypeError
# print(Set1 // Fset1)  # TypeError
# print(Set1 % Fset1)   # TypeError
'''


# Set With Dictionary
'''
# here Set1 = {1,2,3} and Dict1 = {1:100,2:"shyam",3:20.5}

# print(Set1 + Dict1)   # TypeError
# print(Set1 - Dict1)   # TypeError
# print(Set1 * Dict1)   # TypeError
# print(Set1 / Dict1)   # TypeError
# print(Set1 // Dict1)  # TypeError
# print(Set1 % Dict1)   # TypeError
'''


# Frozenset With Integer
'''
# here Fset1 = frozenset({1,2,3}) and Int1 = 5

# print(Fset1 + Int1)   # TypeError
# print(Fset1 - Int1)   # TypeError
# print(Fset1 * Int1)   # TypeError
# print(Fset1 / Int1)   # TypeError
# print(Fset1 // Int1)  # TypeError
# print(Fset1 % Int1)   # TypeError
'''


# Frozenset With Float
'''
# here Fset1 = frozenset({1,2,3}) and Float1 = 4.0

# print(Fset1 + Float1)   # TypeError
# print(Fset1 - Float1)   # TypeError
# print(Fset1 * Float1)   # TypeError
# print(Fset1 / Float1)   # TypeError
# print(Fset1 // Float1)  # TypeError
# print(Fset1 % Float1)   # TypeError
'''


# Frozenset With Boolean
'''
# here Fset1 = frozenset({1,2,3}) and bool1 = True

# print(Fset1 + bool1)   # TypeError
# print(Fset1 - bool1)   # TypeError
# print(Fset1 * bool1)   # TypeError
# print(Fset1 / bool1)   # TypeError
# print(Fset1 // bool1)  # TypeError
# print(Fset1 % bool1)   # TypeError
'''


# Frozenset With Complex
'''
# here Fset1 = frozenset({1,2,3}) and Comp1 = 5+10j

# print(Fset1 + Comp1)   # TypeError
# print(Fset1 - Comp1)   # TypeError
# print(Fset1 * Comp1)   # TypeError
# print(Fset1 / Comp1)   # TypeError
# print(Fset1 // Comp1)  # TypeError
# print(Fset1 % Comp1)   # TypeError
'''


# Frozenset With String
'''
# here Fset1 = frozenset({1,2,3}) and Str1 = "harshal"

# print(Fset1 + Str1)   # TypeError
# print(Fset1 - Str1)   # TypeError
# print(Fset1 * Str1)   # TypeError
# print(Fset1 / Str1)   # TypeError
# print(Fset1 // Str1)  # TypeError
# print(Fset1 % Str1)   # TypeError
'''

# Frozenset With Complex
'''
# here Fset1 = frozenset({1,2,3}) and Comp1 = 5+10j

# print(Fset1 + Comp1)   # TypeError
# print(Fset1 - Comp1)   # TypeError
# print(Fset1 * Comp1)   # TypeError
# print(Fset1 / Comp1)   # TypeError
# print(Fset1 // Comp1)  # TypeError
# print(Fset1 % Comp1)   # TypeError
'''


# Frozenset With List
'''
# here Fset1 = frozenset({1,2,3}) and list1 = [1,2,3]

# print(Fset1 + list1)   # TypeError
# print(Fset1 - list1)   # TypeError
# print(Fset1 * list1)   # TypeError
# print(Fset1 / list1)   # TypeError
# print(Fset1 // list1)  # TypeError
# print(Fset1 % list1)   # TypeError
'''


# Frozenset With Tuple
'''
# here Fset1 = frozenset({1,2,3}) and Tuple1 = (1,2,3)

# print(Fset1 + Tuple1)   # TypeError
# print(Fset1 - Tuple1)   # TypeError
# print(Fset1 * Tuple1)   # TypeError
# print(Fset1 / Tuple1)   # TypeError
# print(Fset1 // Tuple1)  # TypeError
# print(Fset1 % Tuple1)   # TypeError
'''


# Frozenset With Set
'''
# here Fset1 = frozenset({1,2,3}) and Set1 = {1,2,3}

# print(Fset1 + Set1)   # TypeError
# print(Fset1 - Set1)   # TypeError
# print(Fset1 * Set1)   # TypeError
# print(Fset1 / Set1)   # TypeError
# print(Fset1 // Set1)  # TypeError
# print(Fset1 % Set1)   # TypeError
'''


# Frozenset With Dictionary
'''
# here Fset1 = frozenset({1,2,3}) and Dict1 = {1:100,2:"shyam",3:20.5}

# print(Fset1 + Dict1)   # TypeError
# print(Fset1 - Dict1)   # TypeError
# print(Fset1 * Dict1)   # TypeError
# print(Fset1 / Dict1)   # TypeError
# print(Fset1 // Dict1)  # TypeError
# print(Fset1 % Dict1)   # TypeError
'''


# Dictionary With Integer
'''
# here Dict1 = {1:100,2:"shyam",3:20.5} and Int1 = 5

# print(Dict1 + Int1)   # TypeError
# print(Dict1 - Int1)   # TypeError
# print(Dict1 * Int1)   # TypeError
# print(Dict1 / Int1)   # TypeError
# print(Dict1 // Int1)  # TypeError
# print(Dict1 % Int1)   # TypeError
'''


# Dictionary With Float
'''
# here Dict1 = {1:100,2:"shyam",3:20.5} and Float1 = 4.0

# print(Dict1 + Float1)   # TypeError
# print(Dict1 - Float1)   # TypeError
# print(Dict1 * Float1)   # TypeError
# print(Dict1 / Float1)   # TypeError
# print(Dict1 // Float1)  # TypeError
# print(Dict1 % Float1)   # TypeError
'''


# Dictionary With Boolean
'''
# here Dict1 = {1:100,2:"shyam",3:20.5} and bool1 = True

# print(Dict1 + bool1)   # TypeError
# print(Dict1 - bool1)   # TypeError
# print(Dict1 * bool1)   # TypeError
# print(Dict1 / bool1)   # TypeError
# print(Dict1 // bool1)  # TypeError
# print(Dict1 % bool1)   # TypeError
'''


# Dictionary With String
'''
# here Dict1 = {1:100,2:"shyam",3:20.5} and Str1 = "harshal"

# print(Dict1 + Str1)   # TypeError
# print(Dict1 - Str1)   # TypeError
# print(Dict1 * Str1)   # TypeError
# print(Dict1 / Str1)   # TypeError
# print(Dict1 // Str1)  # TypeError
# print(Dict1 % Str1)   # TypeError
'''


# Dictionary With Complex
'''
# here Dict1 = {1:100,2:"shyam",3:20.5} and Comp1 = 5+10j

# print(Dict1 + Comp1)   # TypeError
# print(Dict1 - Comp1)   # TypeError
# print(Dict1 * Comp1)   # TypeError
# print(Dict1 / Comp1)   # TypeError
# print(Dict1 // Comp1)  # TypeError
# print(Dict1 % Comp1)   # TypeError
'''


# Dictionary With List
'''
# here Dict1 = {1:100,2:"shyam",3:20.5} and list1 = [1,2,3]

# print(Dict1 + list1)   # TypeError
# print(Dict1 - list1)   # TypeError
# print(Dict1 * list1)   # TypeError
# print(Dict1 / list1)   # TypeError
# print(Dict1 // list1)  # TypeError
# print(Dict1 % list1)   # TypeError
'''


# Dictionary With Tuple
'''
# here Dict1 = {1:100,2:"shyam",3:20.5} and Tuple1 = (1,2,3)

# print(Dict1 + Tuple1)   # TypeError
# print(Dict1 - Tuple1)   # TypeError
# print(Dict1 * Tuple1)   # TypeError
# print(Dict1 / Tuple1)   # TypeError
# print(Dict1 // Tuple1)  # TypeError
# print(Dict1 % Tuple1)   # TypeError
'''


# Dictionary With Set
'''
# here Dict1 = {1:100,2:"shyam",3:20.5} and Set1 = {1,2,3}

# print(Dict1 + Set1)   # TypeError
# print(Dict1 - Set1)   # TypeError
# print(Dict1 * Set1)   # TypeError
# print(Dict1 / Set1)   # TypeError
# print(Dict1 // Set1)  # TypeError
# print(Dict1 % Set1)   # TypeError
'''


# Dictionary With Frozenset
'''
# here Dict1 = {1:100,2:"shyam",3:20.5} and Fset1 = frozenset({1,2,3})

# print(Dict1 + Fset1)   # TypeError
# print(Dict1 - Fset1)   # TypeError
# print(Dict1 * Fset1)   # TypeError
# print(Dict1 / Fset1)   # TypeError
# print(Dict1 // Fset1)  # TypeError
# print(Dict1 % Fset1)   # TypeError
'''