immutable_var=10, 'cucumber', 'tomato'
print("кортеж: ",immutable_var)
#immutable_var[0]='potato' # Элементы в кортеже нельзя изменить(если элементом кортежа не является список)
mutable_list=[10, 'cucumber','tomato']
print("список: ",mutable_list)
mutable_list[0]='potato'
print("новый список: ",mutable_list)