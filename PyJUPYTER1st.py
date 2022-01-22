#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Om namah shivay


# # PYTHON BOOTCAMP
# # BY JOSE PORTILLA (PIERIAN DATA)
# ## DATE:- 13TH JAN 2022

# ## LET'S BEGIN THE ULTIMATE JOURNEY
# 
# 
# # 03rd_Folder PYTHON OBJECTS AND DATA STRUCTURES BASICS
# 
# # PYTHON OBJECTS AND DATA STRUCTURES BASICS
# 

# ## 12.NUMBERS

# In[2]:


3*2


# In[3]:


4+3


# In[4]:


3/3


# In[5]:


5/2


# # modulo or "Mod" operator

# In[6]:


5/4


# In[7]:


5%4 ''' % is mod operator 
        and it just return remainder'''


# In[8]:


6%2


# In[9]:


2**3 #two times ** is just represents power of 2


# In[10]:


2**4


# In[11]:


5**3


# In[12]:


5**0


# In[13]:


0**4


# In[14]:


0**0


# In[16]:


2**3 + 3*4 # python is following bodmas rule


# In[17]:


(2**3 + 3)*4 


# In[1]:


(2**3 + 3)**4


# ## 014. VARIABLE ASSIGNMENTS

# In[2]:


# python supports dynamic typing


# In[3]:


a=5


# In[4]:


a


# In[ ]:


a


# In[1]:


a=10


# In[2]:


a


# In[3]:


a+a


# In[10]:


a=a+a#run cell over and over


# In[11]:


a


# In[14]:


a


# In[15]:


type(a)


# In[19]:


a=32.3


# In[20]:


type(a)


# In[21]:


type(a)


# In[22]:


int = 3# int is a special keyword so avoid using it


# In[23]:


int


# In[24]:


type(int)


# In[26]:


my_income = 100

tax_rate=0.1

tax=my_income * tax_rate


# In[27]:


tax


# # 015 STRINGS (indexing and slicing) 16th Jan 2022

# In[31]:


"hello"


# In[32]:


'hello'


# In[33]:


print("hello")


# In[34]:


a="I am Iron Man"


# In[35]:


print(a)


# In[36]:


type(a)


# In[37]:


"spidey"
"peter parker"


# In[38]:


print("spidey")
print('peter parker')


# In[39]:


print("peter \nparker")


# In[40]:


print('peter \tparker')


# In[41]:


len("peter parker")


# In[42]:


len("spidey")


# In[43]:


len(a)


# In[44]:


# lets start string indexing
mystring="peter spidey"


# In[45]:


mystring[0]


# In[46]:


mystring[9]


# In[47]:


mystring[11]


# In[48]:


mystring[-1]


# In[49]:


mystring[-11]


# In[50]:


mystring[-12]


# In[54]:


#mystring[-13] #string index out of range so errror will occur 


# In[56]:


#mystring[13]


# In[1]:


ms="hello world"


# In[2]:


ms


# In[5]:


#SLICING
ms[1:]


# In[6]:


ms[:-1]


# In[7]:


ms


# In[9]:


ms[:]


# In[13]:


print(ms[:0])


# In[14]:


print(ms[-1:])


# In[15]:


s="abcdefghijk"


# In[16]:


s


# In[17]:


print(s[:3])


# In[19]:


print(s[3:])


# In[22]:


print(s[2])


# In[23]:


s[3:6]


# In[24]:


s[-3:3]


# In[25]:


s[-1:1]


# In[26]:


s[1:-1]


# In[27]:


s[1:0]


# In[28]:


s[0:1]


# In[30]:


s[0:0]


# In[31]:


s


# In[32]:


s[0:-1]


# In[33]:


s[-5:-1]


# In[34]:


## lets see step size


# In[35]:


s[::]


# In[36]:


s[:]


# In[37]:


s[::2]


# In[38]:


s[-0:3]


# In[39]:


s


# In[40]:


s[2:7:2]


# In[41]:


s[2:8:3]


# In[42]:


s[::-1]


# In[44]:


s[::-2]


# In[47]:


s[2:8:-1]


# In[48]:


s[8:2:-1]


# In[49]:


s[8:2:-2]


# In[50]:


s


# # 017 STRING PROPERTIES AND METHODS

# ## IMMUTABILITY

# In[53]:


name="Sam"


# ### Concatenation

# In[57]:


#replacing s with p


# In[67]:


last_letters=name[1:]


# In[68]:


last_letters


# In[69]:


print(last_letters)


# In[71]:


"P"+last_letters


# In[72]:


new='P'+last_letters


# In[73]:


print(new)


# In[74]:


#now next example


# In[85]:


x="Hello World"


# In[90]:


y=" it is a Beautiful outside!"


# In[91]:


x


# In[88]:


y


# In[89]:


x+y


# In[92]:


print(x+y)


# In[93]:


z=x+y


# In[94]:


z


# In[95]:


print(z)


# In[96]:


letter = "z"


# In[97]:


z


# In[98]:


letter


# In[99]:


let="s"


# In[107]:


let*10 #multiplications with letters OR string multiplications


# In[108]:


a="Sid"


# In[109]:


a * 3


# In[110]:


a=" Sid d"


# In[111]:


a*3


# In[112]:


a="Sid9"


# In[114]:


a*2


# In[115]:


a * 0


# In[116]:


print(a*2)


# In[117]:


print(a*0)


# In[118]:


a*-1


# In[120]:


print(a*-3)


# In[124]:


b=a*4


# In[125]:


b


# In[126]:


print(b)


# In[134]:


'''When we are performing concatenatiom or multiplication
we are going to get error when we try to concatenate a number with a string'''

print(2+3) # this makes sense 
print("2" + '3') #here, its not going to add, its going to concatenate these two strings
# this is a call back to dynamic typing
# We had to be very careful to data types


# ### built-in string methods/function

# In[12]:


x ="hello world"


# In[25]:


x.upper() #press x. and hit tab button, you will see yeah that


# In[26]:


x


# In[27]:


s=x.upper()


# In[28]:


print(x)


# In[29]:


print(s)


# In[30]:


x


# In[31]:


type(x)


# In[32]:


type(s)


# In[33]:


s.lower()


# In[34]:


x.split() 


# In[172]:


x= "this is a String"


# In[173]:


x.split()
# this split method will create a list of a string 


# In[177]:


x.split("i") #this code will split on 'i' and white space will be included


# In[179]:


print(x.split())


# In[181]:


print("x.split()") # this is a string 


# In[185]:


print(x.split('i')) # and not print(x.split(i)) 


# In[189]:


x.count("i")


# In[193]:


x.casefold()


# In[200]:


print(x.center(43))


# In[204]:


x.endswith("f")


# In[205]:


x.endswith("g")


# In[213]:


x.find("i")


# In[218]:


x.index("g")


# In[223]:


x.title()


# ## 019 PRINT FORMATTING WITH STRINGS 

# ### Formatting with the .format() Method
# ### A good way to format objects into your strings for print statements is with the string .format() method. 
# ### The syntax is :- 
# ### 'String here {} then also{}'.format('something1','something2')

# In[250]:


print("this is a string {}".format("Inserted") )


# In[251]:


print("The {} {} {}".format('fox',"brown",'quick'))


# In[252]:


print("The {2} {1} {0}".format('fox',"brown",'quick'))


# In[256]:


print("The {0} {0} {0}".format('fox',"brown",'quick'))


# In[264]:


print("The {2} a {1} {0}".format('fox',"brown",'quick'))


# In[272]:


print("The {q} {b} {f}".format(f='fox',b="brown",q='quick')) #prefer this instead of below code(i.e index posoition)


# In[35]:


print("The {2} {1} {0}".format('fox',"brown",'quick'))


# In[38]:


print("The {f} {f} {f}".format(f='fox',b="brown",q='quick')) #inserted objects can be assigned keywords


# ## Float Formating follows "{value:width.precision f}" (no space between precision and f)

# In[39]:


result=100/777


# In[40]:


print(result)
type(result)


# In[44]:


print("The result is {}".format(result))
print(f'The result is {result}')


# In[100]:


print("The result is {r} \n{r} is of type float".format(r=result)) 
# advantage of .format is we dont have to repeat(doubling) everything after assigning a keyword
# we dont need to write too much of code and eventually this will save time
 
    
# INSERTED OBJECTS CAN BE REUSED, AVOIDING DUPLICATION 

    
    # though .format method is old but it's gold itself
    # also Formatted String Method (f-strings) is also a new gold


# In[302]:


print("The result is {r:10.3f}".format(r=result))
#not allowed :- {r:10.3 f} i.e is no spaces is allowed
#here, 10 defines width(white spaces)


# In[303]:


result1=100.12345


# In[305]:


print("The result1 is {r:1.2f}".format(r=result1))


# In[83]:


# ALIGNMENT PADDING  PRECISION

# within curley braces :- assign field length, left/right alignment,etc

print("{0:8} | {1:9}".format('Fruit','Quantity'))
print("{0:8} | {1:9}".format('Apples', 3.))
print("{0:8} | {1:9}".format('Oranges',10))


# In[85]:



print("{0:<8} | {1:^8} | {2:>8}".format('left',"centre",'right'))
print("{0:<8} | {1:^8} | {2:>8}".format(11,22,33))


# In[98]:


## We can PRECEDE th Alignment operator with padding character

print("{0:=<8} | {1:-^8} | {2:.>8}".format('left',"centre",'right'))
print("{0:=<8} | {1:-^8} | {2:.>8}".format(11,22,33))


# In[99]:


print("{0:9<8} | {1:S^8} | {2:%>8}".format('left',"centre",'right'))
print("{0:(<8} | {1:!^8} | {2:)>8}".format(11,22,33))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[347]:


name="Siddharth"


# In[348]:


print("Hello, I am {}".format(name))


# In[349]:


print(f"Hello, I am {name}") 
# f-strings literals
#Dont forget f in the begining


# In[350]:


name="Spidey"
age=9


# In[351]:


print(f"{name} is {age} years old.")


# In[ ]:





# In[50]:


player="Thomas"


# In[51]:


point="43"


# In[52]:


print("last night "+player+" scored "+point+" points ")
# Concatenation


# In[53]:


print(f"last night {player} scored {point} points ")
# String Formatting


# In[61]:


print("last night {p} scored {pt} points ".format(p=player, pt=point))#not p="player"


# In[362]:


#Since I will likely encounter many versions in someone else's code in future so I need to learn all


# In[363]:


#I am the Best


# ## Formating with Placeholders

# In[65]:


print("I %s Iron Man" %'am')
print("I %s Iron Man\nI %s the Best" %('am','am')) #heve to repeat every time thats why .format is the best
#modulo % is reffered as string formatting operator


# In[371]:


print("I %s Iron %s" %('am',"Man")) #passing multiple items


# In[375]:


x,y= "am","Man"

print("I %s Iron %s" %(x,y)) #Passing Variable names


# In[ ]:





# In[378]:


#Padding and Precision of floating point numbers


# In[380]:


print("Floating point no. : %5.2f" %(13.544))


# In[381]:


print("Floating point no. : %1.0f" %(13.544)) #will take approximate due to '.5'


# In[387]:


print("Floating point no. : %10.5f" %(13.544))


# In[388]:


print("Floating point no. : %45.2f" %(13.544))


# In[389]:



##Multiple Formatting


# In[394]:


print("First: %s, Second:%5.2f, Third:%r" %('hi',3.1415,'bye!')  )


# In[399]:


print("First: %s, Second:%10.3f, Third:%r" %('hi',3.1415,'bye!')  ) # %r and %s 


# In[ ]:





# In[ ]:





# In[ ]:





# # 021 LISTS IN PYTHON

# In[400]:


my_list= [1,2,3,4]


# In[401]:


len(my_list)


# In[404]:


my_list=["String" ,100,5.5]


# In[405]:


len(my_list)


# In[408]:


mylist= ['one','two','three',4]


# In[409]:


print(mylist)


# In[410]:


type(mylist)


# In[411]:


mylist


# In[412]:


mylist


# In[413]:


mylist[0]


# In[414]:


print(mylist[0])


# In[415]:


type(mylist[0])


# In[416]:


print(mylist[3])


# In[417]:


type(mylist[3])


# In[ ]:





# In[418]:


print(mylist)


# In[425]:


mylist[1:]


# In[426]:


mylist


# In[435]:


anotherlist=[5,'Six']


# In[436]:


anotherlist


# In[442]:


mylist    +  anotherlist # spaces dont matters here
# CONCATENATION 


# In[443]:


newlist = mylist+ anotherlist


# In[448]:


print(       newlist)


# In[449]:


newlist


# In[450]:


newlist[0]='ONE ALL CAPS'


# In[451]:


newlist


# In[463]:


newlist.append("Seven")


# In[466]:


print(newlist)


# In[474]:


newlist.reverse()


# In[475]:


newlist


# In[476]:


newlist.pop()


# In[477]:


newlist


# In[482]:


newlist.pop()


# In[483]:


newlist


# In[486]:


popped_item = newlist.pop()


# In[487]:


popped_item


# In[488]:


newlist


# In[496]:


newlist.append("Five")


# In[497]:


newlist


# In[498]:


newlist.pop(0)


# In[499]:


newlist


# In[500]:


newlist.pop(-1)


# In[501]:


newlist


# In[ ]:






# In[502]:


new_list=["a",'e','x',"b","c"]
num_list=[4,1,8,3]


# In[503]:


new_list.sort()


# In[504]:


new_list


# In[505]:


num_list


# In[506]:


num_list.sort()


# In[507]:


num_list


# In[508]:


num_list.reverse()


# In[509]:


num_list


# In[510]:


num_list


# In[13]:



#OM NAMAH SHIVAY
#ABSOLUTE ZERO
# NOTHING


# In[72]:


person=input("I AM ")
message="hello, {}!".format(person)#if we use more than once '{}' in this code it will show error
message1="Hello, {p} \n{p} is the Best".format(p=person)#but here it wont
print(message)
print(message1)


# In[3]:


print("iron")


# In[55]:


import time

for i in range (100): # 100 times will execute i.e. from 0 to 99
    print(i,end='  ') # spaces
    time.sleep(1) # "1" means 1 second; if we use '0.5' second it will work
#to stop press "cntrl+c" OR interrupt the kernel


# In[ ]:





# In[ ]:





# In[ ]:





# # 023 DICTIONARIES IN PYTHON
# # 18th JAN 2022

# In[4]:


my_dict = {"key1":"VALUE1", 'key2':'value2'}


# In[5]:


my_dict


# In[8]:


my_dict['key1']


# In[9]:


prices_lookup={'apple':2.99,"oranges":1.99, 'milk':5.80}


# In[11]:


prices_lookup['apple'] 


# In[12]:


d= {'k1':123 ,  'k2':[0,1,2], 'k3':{"insidekey":100}}


# In[13]:


d['k2']


# In[16]:


d['k3']


# In[18]:


d['k3']["insidekey"]


# In[19]:


print(d)


# In[20]:


print(type(d))


# In[24]:


print(type(d['k1']))


# In[25]:


print(type(d['k2']))


# In[26]:


print(type(d['k3']))


# In[78]:


print(type(d['k3']['insidekey']))


# In[ ]:


# in Dictionaries we can add another dictionary inside it
# also we can add list in it
#


# In[31]:


d2= {'k1':123 ,  'k2':[0,1,2], 'k3':{"insidekey":{"innerinsidekey":9}}}


# In[32]:


print(d2)


# In[33]:


type(d2)


# In[34]:


print(type(d2['k3']['insidekey']))


# In[35]:


print(type(d2['k3']['insidekey']['innerinsidekey']))


# In[77]:


print(d2["k3"])


# In[ ]:





# In[76]:


print(d2["k3"]['insidekey']['innerinsidekey'])
#print(d2["k3"]['innerinsidekey'])this is'nt allowed; above code should use


# In[ ]:





# In[79]:


print(d)


# In[80]:


d['k2']


# In[100]:


d['k2'][0] 
# grabbing no.'0' from list of dictionary 
# which is in second key having zero position/index location 


# In[ ]:


d


# In[ ]:





# In[103]:


d={'key1':['a','b','c']}


# In[ ]:


d


# In[104]:


d["key1"]


# In[ ]:


#grabbing c
print('s')


# In[ ]:





# In[ ]:




