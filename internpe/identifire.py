#creating identifiers in python
#integer data type
#octal no #hexadecimal no #
"""
var=123  
123 is decimal no (0-9)

print(type(var))
#binary form
bvar= 0b1111
print(type(bvar))
print(bvar)

#octal form (0to7)
ovar = 0o123
print (type(ovar))
print(ovar)


decimal (10)
binary(2)


#hexadecimal(16)
hvar=0xface
print(type(hvar))
print(hvar)

#binary data converts 15
print(bin(30))
print(hex(20))
print(oct(40))



#floating data type
# float - to represent the floating point values
#we can also store numbers in exponential forms
fvar = 1.10e20
print(type(fvar))
print(fvar)

#complex :
#no of form a+bj
#a indicates real part (int, float)
#b indicates imaginary part (int, float)(only dec form)
cvar= 20+50j
print(type(cvar))
print(cvar)

cvar= 0b1111+32j
print(cvar.real)

#boolean data types 
bvar = True
print(type(bvar))

# string :

#svar= "hi my name is hemangi"
#print(type(svar))

#sum of 2 nos 

#print(f"sum of 2 and 6 is \n {8+6}")

 
svar ="python"

print (svar[0])
print (svar[-1])
print (svar[4])
print (svar[-3])

#slicing in string :
print(svar[0:3]

#print(svar[::-1]) #REVERSE STRING
print(svar[0:6:1]) #no output
print(svar[-1::-1])#reverse string

channel_name = "learn coding"
message ="Subscribe to our channel:{channel_name}"
print (message)  #formating of string

print ( "sum of 2 and 6 is{2+6} ")

#methods of string
#find method
info = "a quick brown fox jumps over the lazy dog"
print(info.find('quick')) #position of quick
print(info.find('fox')) #position of fox return index position
print(info.find('o'))
print(info.find('o',11))
print(info.find('o',12,-1))
print(info.find('o',16,-2))
print(info.find('o'))
#index method
 # indexing  left to right starts with 0 &right to left start with -1
svar= "i am learning python with learn coding"
print (svar[0]) 
print (svar[2])
print (svar[-1])
print (svar[3]) 
print (svar[-6]) 
#slicing in string(left to right starts with 0 &right to left start with -1)
svar ="python"
print (svar[0:3])
print (svar[2:3])
print (svar[1:1000])
print (svar[-4:1000])
print (svar[:])
print(svar[2:])
print(svar[0:6:2])
print(svar[0:6:3])
#print (svar[1000]) #index error
#how to reverse string 
#reverse of string using slicing 
str="python"
print(str[::-1])
print(str[-1::-1])
#formating of string
#{}= replacement operator
channel_name ="Learn coding"
message = "suscribe to our channel{channel_name}"
print (message)
"""
"""6.Range:
    range (begning, ending, step)
     Type casting : we can convert one type into another type. this conversion is known as type casting..
     eg
     int ()
     float()
     bool ()
     str() 
     
    """
   
        
        