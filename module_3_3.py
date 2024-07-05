# 1.Функция с параметрами по умолчанию:
def print_params(a=1, b='Anaconda', c=True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1,2,3])

# 2.Распаковка параметров:
values_list = [1, 'Python', True]
values_dict = {'a':3, 'b':4, 'c':6}

print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:

values_list_2 = [1, 'String']
print_params(*values_list_2, 42)
