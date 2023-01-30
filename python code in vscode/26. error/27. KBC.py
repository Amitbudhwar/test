q=["which language was used in facebook ?","py","fr","php","None",4],
["which language was used in facebook ?","py","fr","php","None",4],
["which language was used in facebook ?","py","fr","php","None",4],
["which language was used in facebook ?","py","fr","php","None",4],
["which language was used in facebook ?","py","fr","php","None",4],
["which language was used in facebook ?","py","fr","php","None",4]
["which language was used in facebook ?","py","fr","php","None",4]
["which language was used in facebook ?","py","fr","php","None",4]
["which language was used in facebook ?","py","fr","php","None",4]
levels=[1000,2000,5000,10000,20000,50000,100000,500000,1000000,2000000]
money=0
for i in range(0, len(q)):
    question=q[i]
    print(f"Question for Rs. {levels[i]}")
    print(f"a. {q1[1]}     b. {q2[2]}")  
    print(f"c. {q1[3]}     d. {q2[4]}")  
    reply=int(input("Enter your answer (1 - 4)"))
    if (reply==q[-1]):
        print(f"correct answer , you won Rs.{levels[i]}")
        if(i==4):
            money=20000
        elif(i==9):
            money==2000000
    else:
        print("Wrong Answer")
        break
    
    