from math import pi

integer_var = 10
float_var = 10.5
complex_var = 3 + 4j
list_var = [1, 2, 3]
tuple_var = (4, 5, 6)
dict_var = {"name": "Alice", "age": 25}
set_var = {7, 8, 9}
bool_var = True

print(type(integer_var))
print(type(float_var))
print(type(complex_var))
print(type(list_var))
print(type(tuple_var))
print(type(dict_var))
print(type(set_var))
print(type(bool_var))

converted_float = float(integer_var)
converted_int = int(float_var)

print(converted_float)
print(converted_int)
