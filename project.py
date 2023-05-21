

print("welcome to student portal")
print("Menu:" "\n"
      "1. Student login" "\n"
      "2. Teacher login")
print("\n")

a=int(input("enter option 1 or 2:"))
print("\n")
if a==1:
    print("1.New user")
    b=int(input("enter option 1 to login"))
    if b==1:
        print("Student Login")
        print("\n")
        c=input("enter username:")
        print("CT2 Marks to be entered")
        sub=["maths","english","physics","chemistry","compscience"]
        
        CT2m={}
        sum2=0
        sum3=0
        sum4=0
        ma2=[]
        
        for j in sub:
            print("enter",j,"marks")
            tot2=float(input("enter total marks of this subject"))
            marks2=float(input("enter marks obtained"))
            percent2=(marks2/tot2)*100
            if percent2>=33:
                cr="pass"
            else:
                cr="fail"
            if 91<=percent2<=100:
                grade2="A1"
            elif 81<=percent2<=90:
                grade2="A2"
            elif 71<=percent2<=80:
                grade2="B1"
            elif 61<=percent2<=70:
                grade2="B2"
            elif 51<=percent2<=60:
                grade2="C1"
            elif 41<=percent2<=50:
                grade2="C2"
            elif 33<=percent2<=40:
                grade2="D"
            elif 21<=percent2<=32:
                grade2="E1"

            elif 0<=percent2<=20:
                grade2="E2"
            else:
                print("error")
            sum2=sum2 +marks2
            ma2.append(marks2)

            
            CT2m[j]={"marks":marks2,"percentage":percent2,"grade":grade2,"pass or fail":cr}
            
        import json
        print(json.dumps(CT2m, indent=5)) 

        print("Total marks in CT2=",sum2, "overall percentage in CT2",(sum2/185)*100)

        CT3m={}
        sum2=0
        ma3=[]
        for k in sub:
            print("enter",k,"marks")
            tot3=float(input("enter total marks of this subject"))
            marks3=float(input("enter marks obtained"))
            percent3=(marks3/tot3)*100
            if percent3>=33:
                cr="pass"
            else:
                cr="fail"
            if 91<=percent3<=100:
                grade3="A1"
            elif 81<=percent3<=90:
                grade3="A2"
            elif 71<=percent3<=80:
                grade3="B1"
            elif 61<=percent3<=70:
                grade3="B2"
            elif 51<=percent3<=60:
                grade3="C1"
            elif 41<=percent3<=50:
                grade3="C2"
            elif 33<=percent3<=40:
                grade3="D"
            elif 21<=percent3<=32:
                grade3="E1"

            elif 0<=percent3<=20:
                grade3="E2"
            else:
                print("error")
            sum3+=marks3
            ma3.append(marks3)

            
            CT3m[k]={"marks":marks3,"percentage":percent3,"grade":grade3,"pass or fail":cr}
            
        import json
        print(json.dumps(CT3m, indent=5)) 

        print("Total marks in CT2=",sum3, "overall percentage in CT2",(sum3/185)*100)

        Sem1m={}
        ma4=[]
        
        for i in sub:
            print("enter",i,"marks")
            tot4=float(input("enter total marks of this subject"))
            marks4=float(input("enter marks obtained"))
            percent4=(marks4/tot4)*100
            if percent4>=33:
                cr="pass"
            else:
                cr="fail"
            if 91<=percent4<=100:
                grade4="A1"
            elif 81<=percent4<=90:
                grade4="A2"
            elif 71<=percent4<=80:
                grade4="B1"
            elif 61<=percent4<=70:
                grade4="B2"
            elif 51<=percent4<=60:
                grade4="C1"
            elif 41<=percent4<=50:
                grade4="C2"
            elif 33<=percent4<=40:
                grade4="D"
            elif 21<=percent4<=32:
                grade4="E1"

            elif 0<=percent4<=20:
                grade4="E2"
            else:
                print("error")
            sum4=sum4+marks4
            ma4.append(marks4)

            
            Sem1m[i]={"marks":marks4,"percentage":percent4,"grade":grade4,"pass or fail":cr}
            
        import json
        print(json.dumps(Sem1m, indent=5))  

        print("Total marks in CT2=",sum4, "overall percentage in CT2",(sum4/370)*100)

        math=[CT2m["maths"]["percentage"],CT3m["maths"]["percentage"],Sem1m["maths"]["percentage"]]
        english=[CT2m["english"]["percentage"],CT3m["english"]["percentage"],Sem1m["english"]["percentage"]]
        physics=[CT2m["physics"]["percentage"],CT3m["physics"]["percentage"],Sem1m["physics"]["percentage"]]
        chem=[CT2m["chemistry"]["percentage"],CT3m["chemistry"]["percentage"],Sem1m["chemistry"]["percentage"]]
        comp=[CT2m["compscience"]["percentage"],CT3m["compscience"]["percentage"],Sem1m["compscience"]["percentage"]]
        print("here are your percentage improvements")
        pi={"math":[math[1]-math[0],math[2]-math[1]],"english":[english[1]-english[0],english[2]-english[1]],"physics":[physics[1]-physics[0],physics[2]-physics[1]],"chem":[chem[1]-chem[0],chem[2]-chem[1]],"comp":[comp[1]-comp[0],comp[2]-comp[1]]}
        print(pi)
        print("here are your predicted percentages")
        pd={"math":(math[1]+(((math[1]-math[0])+(math[2]-math[1]))/2)),"english":(english[1]+(((english[1]-english[0])+(english[2]-english[1]))/2)),"physics":(physics[1]+(((physics[1]-physics[0])+(physics[2]-physics[1]))/2)),"chem":(chem[1]+(((chem[1]-chem[0])+(chem[2]-chem[1]))/2)),"compscience":(comp[1]+(((comp[1]-comp[0])+(comp[2]-comp[1]))/2))}
        
        print(pd)
        overall=[CT2m,CT3m,Sem1m,pi,pd]
        print(overall)
        print(" open the given url, copy and paste the output overall and save the file as yourusername.txt under same folder as this file")
            #gdocs taken out for personal reasons
        #print("https://docs.google.com/document/d/1tx9ZYV2x8AcxwcO2Wpumb0tnEilW55TWOrVY4kBMhQg/edit")
        


        
else:
    print("welcome teacher portal")
    ufo=input("enter student full name followed by.txt")
    f = open(ufo, "r")
    print(f.read())
    
    
    
    



    


        
        
        
       


        

    
        


