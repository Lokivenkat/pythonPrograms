>>> t=('loki','venkat',510)
>>> t
('loki', 'venkat', 510)
>>> t[0]  #printing index value
'loki'
>>> t[0]="aditya"
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    t[0]="aditya"
TypeError: 'tuple' object does not support item assignment
>>> t.index('venkat')  #finding index value
1
>>> t=('loki','venkat',510,'aditya','college')
>>> t
('loki', 'venkat', 510, 'aditya', 'college')
>>> t.count('loki')   #counting the element in the tuple
1
>>> t=(1,2,3,1,2,5,7,1,2,8,5,3,0)
>>> t.count(1)
3
>>> t.count(3)
2
>>> t=('loki','venkat',510,'aditya')
>>> tList=list(t)   #we cannot change element in tuple...so we change the tuple into list to change
>>> tList
['loki', 'venkat', 510, 'aditya']
>>> tList[2]="college"  #replacing elemnt in list
>>> tList
['loki', 'venkat', 'college', 'aditya']
>>> t=tuple(tList)  #again changing into tuple
>>> t
('loki', 'venkat', 'college', 'aditya')
>>> min(t)  #minimum in the tuple
'aditya'
>>> max(t)  #maximum in the tuple
'venkat'
>>> t[0:2]  #printing using index
('loki', 'venkat')
>>> t[0:3]  #printing using index
('loki', 'venkat', 'college')
>>> t[-1]   #printing using index
'aditya'    
