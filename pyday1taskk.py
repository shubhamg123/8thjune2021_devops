import ctypes
a=input()
address=id(a)
print("type",address)
adress1=int(input())
val=ctypes.cast(adress1,ctypes.py_object).value
print("the value at address is",val)
