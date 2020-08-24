class count:
    def __init__(self,count=0):
        self__count=count

c1 = count(2)
c2 = count(2)
print(id(c1)==id(c2),end="")
s1="Good"
s2="Good"
print(id(s1)==id(s2))
