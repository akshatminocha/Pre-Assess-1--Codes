# 1) Moving all '-' in Front of the entered string

def main():
    n=input("enter a string: ")
    c=0
    for i in n:
        if(i=="-"):
            n=n.replace("-","",1)
            c=c+1
    print("-"*c+n)
main()    
            


# 2) Counting Number of occurrences of all the characters of a string

from collections import Counter

def find_most_occ_char():
    n=input("enter a string: ")
  
    # now create dictionary using counter method 
    # which will have strings as key and their  
    # frequencies as value 
    wc = Counter(n) 
  
    # Finding maximum occurrence of a character  
        # and get the index of it. 
    s = max(wc.values()) 
    i = wc.values() 
      
    print (wc.items())
find_most_occ_char()    


