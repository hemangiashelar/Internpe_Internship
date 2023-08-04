#operators in python

# 1. arithmatic operators
#(+, -, *, /, //,**)
a=50
b=20
#addition
print ("addition :", a+b)
print ("subtraction", a-b)
print ("multiplication", a*b) 
print ("division", a/b)#floating point
print ("floor division",a//b)#integic value
print ("modulous division", a%b) #reminder
print ("power operator :", 10**2) 
print ("power operator :", 5**3) 

# 2. Relational or comparison operator :
#<, <= ,> , >=, ==, !=

#comparisons

print (a>b)
print (a>=b)
print (a<b)
print (a<=b)
print (a==b)
print (a!=b)

print(10==10)#true
print (10==13) #false

# 3. logical Operator
# and, or, not 

print (10==10 and "raju"== "rastogi" ) # false

print (10 ==10 and "raju"== "raju" ) # true 
print(5 and 10) # both true values 

print(0 and 10) # 0 is false 

# or
print (10 or 20)

print(True or False)

# not 
print (not True)
print (not False)

# 4.  bitwise operator (applicable for int and boolean value only)
# & => bitwise and (if both 1 then 1 else 0 )
# | => bitwise or (if any 1 then 1 else 0)
# ^ =>  if both same then output 0 else 1
# ~ => complement
# >> =>
# << =>
print (5 & 6)

print(5|6)

print(5^6)

print (15>>1)
print (15<<1)

# 5. assignment Operator
a=5 
print (a)

# 6. Special Operator
# 1. identity Operator 
      # is, is not 
      
a = 5 
b = 5 # both id is same 
print (a is b) 

print ("id of a :", id (a))
print ("id of b :", id (b))

print (a is not b)

#2. membership operator 
# in , not in 

var = "india is great"
print ("great"in var)
print ("hellow"in var)
print ("hellow" not in var)








