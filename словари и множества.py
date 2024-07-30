my_dict = {'take':1992 , 'max':1995 ,'sasha':2000 , 'anton':2002}
print(my_dict)
print(my_dict.get('anton'))
print(my_dict.get('alena'))
my_dict.update({'nastya':2003,'elena':1990})
print(my_dict)
my_dict.pop('elena')
print(my_dict)
my_set = {1,11,11,1,3,3,5,(1,2,2),'takei' }
print(my_set )
my_set.update({9,8})
print(my_set )
my_set.discard(3)
print(my_set)