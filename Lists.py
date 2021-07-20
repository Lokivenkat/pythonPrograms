>>> list=["loki","venkat","510"]
>>> list
['loki', 'venkat', '510']
>>> type(list)  #type of list
<class 'list'>
>>> list[0:3]   
['loki', 'venkat', '510']
>>> list[1]
'venkat'
>>> list.append("aditya") #adding data at the last
>>> list
['loki', 'venkat', '510', 'aditya']
>>> list[1]="Engineering"
>>> list
['loki', 'Engineering', '510', 'aditya']
>>> list.insert(1,"venkat")  #adding data at the particular position
>>> list
['loki', 'venkat', 'Engineering', '510', 'aditya']
>>> list=['loki', 'venkat', 'Engineering', '510', 'aditya']
>>> list.extend(['college','campus'])  #adding multiple data
>>> list
['loki', 'venkat', 'Engineering', '510', 'aditya', 'college', 'campus']
>>> print(len(list)) #length of the list
7
>>> list.remove("venkat") #removing element
>>> list
['loki', 'Engineering', '510', 'aditya', 'college', 'campus']
>>> list.pop()  #popping last element
'campus'
>>> list
['loki', 'Engineering', '510', 'aditya', 'college']
>>> list.pop(1) #popping element using index
'Engineering'
>>> list
['loki', '510', 'aditya', 'college']
>>> del list[1] #deleting element using del function
>>> list
['loki', 'aditya', 'college']
>>> list.sort() #sorting elements in list
>>> list
['aditya', 'college', 'loki']
>>> list.reverse() #reversing the elements in the list
>>> list
['loki', 'college', 'aditya']
>>> min(list) #displays minimum in the list
'aditya'
>>> max(list) #displays maximum in the list
'loki'
>>> list.sort(reverse=True) #arranging in descending order
>>> list
['loki', 'college', 'aditya']
>>> 
