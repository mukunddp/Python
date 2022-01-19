"""s = "SuperExcited"
print(s[-6:-1])               # xcite
print(s[-6::-1])              #xErepuS
print(s[-1])"""
#list      - ordered, changeable/mutable
l=[1,2,5,"mukund",25.5,4]
l.append("parve")
print(l[-1])
"""print(l)                # [1, 2, 5, 'mukund', 25.5, 4, 'parve']

#tuple - cant add another - ordered , not changeable
t=(51,52,"mukund")
print(t)                # (51, 52, 'mukund')

#set   - follows his own rule prints in his own way (unordered, not changeable)
s ={"mukund",5 , 23 ,1 ,2, "parve" ,99}
print(s)                # {1, 2, 99, 'mukund', 5, 23, 'parve'}

#Dictionary - unordered, changeable
d = { 'temp ': 25,
      'hum ': 86.5 ,
      }
print(d) """