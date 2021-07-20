>>> set={"loki","venkat",510,"loki"}
>>> set
{'loki', 'venkat', 510}  #set doesn't allows duplicate values
>>> len(set)  #length of the set
3
>>> set.add("aditya") #adding element into set
>>> set
{'loki', 'venkat', 'aditya', 510}
>>> set1={'loki',510} #taking another set
>>> set.remove(510)   #removing element in set 
>>> set
{'loki', 'venkat', 'aditya'}
>>> set.update(set1)  #updates 2 sets
>>> set
{'venkat', 'loki', 'aditya', 510}
>>> set.intersection(set1) #intersection of 2 sets
{'loki', 510}
>>> set.count("loki") #count function doesn't exists in set
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    set.count("loki")
AttributeError: 'set' object has no attribute 'count'
>>> set.pop() #popping random element
'venkat'
>>> set
{'loki', 'aditya', 510}
>>> 
