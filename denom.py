# denomination of withdrawl cash

m_2000s,m_500s,m_200s,m_100s=10,20,50,30

#print((m_2000s*2000)+(m_500s*500)+(m_200s*200)+(m_100s*100))

output=""

cash=int(input("Tell us required cash: "))

t_2000s,t_500s,t_200s,t_100s=m_2000s,m_500s,m_200s,m_100s

if t_2000s>0 and cash//2000!=0:
    req=cash//2000 # 5000//2000>> 2
    if req<=t_2000s:
        cash-=(req*2000)
        t_2000s-=req
        output+="2000 X "+str(req)+"\n"
    else:
        cash-=(t_2000s*2000)
        output+="2000 X "+str(t_2000s)+"\n"
        t_2000s=0

if t_500s>0 and cash//500!=0 and cash>0:
    req=cash//500 # 5000//2000>> 2
    if req<=t_500s:
        cash-=(req*500)
        t_500s-=req
        output+="500 X "+str(req)+"\n"
    else:
        cash-=(t_500s*500)
        output+="500 X "+str(t_500s)+"\n"
        t_500s=0

if t_200s>0 and cash//200!=0 and cash>0:
    req=cash//200 # 5000//2000>> 2
    if req<=t_200s:
        cash-=(req*200)
        t_200s-=req
        output+="200 X "+str(req)+"\n"
    else:
        cash-=(t_200s*200)
        output+="200 X "+str(t_500s)+"\n"
        t_200s=0

if t_100s>0 and cash//100!=0 and cash>0:
    req=cash//100 # 5000//2000>> 2
    if req<=t_100s:
        cash-=(req*100)
        t_100s-=req
        output+="100 X "+str(req)+"\n"
    else:
        cash-=(t_100s*100)
        output+="100 X "+str(t_100s)+"\n"
        t_100s=0

if cash>0:
    print("Can't dispense required amount")
else:
    m_2000s,m_500s,m_200s,m_100s=t_2000s,t_500s,t_200s,t_100s
    print("Required cash withdrawn successfully")
    print(output)