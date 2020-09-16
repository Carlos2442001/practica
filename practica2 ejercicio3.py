print("introducir tiempo")
h=int(input("introducir hora: "))
m=int(input("introducir minuto: "))
s=int(input("introducir segundos: "))

if s>=0 and s<=58:
    s=s+1
else:
        if s==59:
            s=0
            m=m+1
            if m==60:
                m=0
        
       
if m>0 and m<=58 and s>59:
    m=m+1
else:
        if m==59:
            m=0
            h=h+1
       
        
if h>=0 and m<=22 and m>59:
    h=h+1
else:
        if h==23:
            h=0
        
    
print("tiempo mas un segundo: " ,h,m,s)

            
            

            

        
