import string
import random
if __name__=="__main__":
    s1=string.ascii_lowercase

    s2=string.ascii_uppercase
    
    s3=string.digits

    s4=string.punctuation
plen=int(input("Enter length of password"))
s=list()
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)
random.shuffle(s)
print("Your password is:")
print("".join(random.sample(s,plen)))