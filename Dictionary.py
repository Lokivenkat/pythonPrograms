>>> person={'firstname':'loki','lastname':'venkat','number':'510'}
>>> person
{'firstname': 'loki', 'lastname': 'venkat', 'number': '510'} #{'key':'value'}
>>> person.keys()  #prints all keys
dict_keys(['firstname', 'lastname', 'number'])
>>> person.values()  #prints all values
dict_values(['loki', 'venkat', '510'])
>>> person.copy()   
{'firstname': 'loki', 'lastname': 'venkat', 'number': '510'}
>>> person.update({'mobile':'79953'}) #adding another key to dictionary
>>> person
{'firstname': 'loki', 'lastname': 'venkat', 'number': '510', 'mobile': '79953'}
>>> person.fromkeys({"college":"aditya"})
{'college': None}
>>> person
{'firstname': 'loki', 'lastname': 'venkat', 'number': '510', 'mobile': '79953'}
>>> person.popitem() #pops last key 
('mobile', '79953')
>>> person
{'firstname': 'loki', 'lastname': 'venkat', 'number': '510'}
>>> person.pop("number") #pops certain key
'510'
>>> person
{'firstname': 'loki', 'lastname': 'venkat'}
>>> person.clear() #clear all keys in dictionary
>>> person
{}
>>> person={'firstname':'loki','lastname':'venkat','number':'510'}
>>> person['age']=35  #adding another key
>>> person
{'firstname': 'loki', 'lastname': 'venkat', 'number': '510', 'age': 35}
