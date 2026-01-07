#from PIP import rock

#rock.rock()

#a="retrieval","augmented","generation"
#print(a,sep="")



#print("retrieval","augmented" ,"generation", sep="")

#a=(1,2,3,4,5)

#for i  in enumerate(a):
#    print(i)
#   




#a=()
#a=a+(1,)
#print(a)

#arr = tuple(input())
#x = input()
#print(arr.index(x))


#t= ()
#z=int(input())
#t=t+(z,)
#x=int(input())
#if x in t:
#   print(t.index(x))
#   
#   
#else:
#   print("False")

#dict={}
#set={3,4,5,6,7}
#set.remove(3)
#print(set)
#dict.update({"pythonic":"thinking", 1:3})
#print(dict)

#st="data analysis of machine learning "


#print(st + "python")
#print("".join("_"))


#age=int(input("Enter your age :"))
#if age>=18:
#     print("you are eligible.")
#else:
#     print("not you are eligible ")

#s1=int(input("Sub1 % : " ))
#s2=int(input("Sub2 % :  "))
#s3=int(input("Sub3 % : "))
#total= (s1+s2+s3)/3

#if s1<33 or s2<33 or s3<33:
#    print ("You are fail, You don't have a sufficent mark  in an individual subject.")
#elif total==40 or total>=33 :
#    print("pass")  
#    print(f"you obtaining percentage is {total}%")

#else:
#    print("fail")
#    print(f"you obtaining percentage is {total}%")


#m1= int(input("number_1 : "))
#m2= int(input("number_2: "))
#m3= int(input("number_3 : "))
#m4= int(input("number_4 : "))

#if m1>m2 :
#   a=m1
#if m2>m1:
#    a=m2
#if m3>m4:
#    b=m3
#if m4>m3:
#     b=m4
#if a>b:
#   print(f"Yes, definetly {a} is greater than others.")
#else:
#    print(f"Yes, definetly {b} is greater than others.")


#try:
#  m1= int(input("number_1 : "))
#  m2= int(input("number_2: "))
#  m3= int(input("number_3 : "))
#  print(f"Yes, definetly {max(m1,m2,m3)} is greater than others.")
#except ValueError:
#    print("Invalid input..?")
#if m1>m2:
#    n=m1
#else:  #if m1<m2:
#   n=m2
#if m3>n:
#  q= m3

#if m1>m3:
#   q=m1
#else:
#    q=n
#if n>q:
#    print(f"Yes, definetly {n} is greater than others.")
#else:
#     print(f"Yes, definetly {n} is greater than others.")



#name=input("Your name..")

#z=len(name)
#if z==10:
#   print("name character is 10")
#   
#else:
#    print("name character is not 10")

#user =  input("\t 🔍Search anything....")
#li=["hack" , "money begets money","fishing","hacker","track","tracess","bulling","data crash"]
#for i in li:
#    if i in user:
#      print("⚠️This is illegal which makes harm your device.")
#      break

#    else:
#       print("safe...✅")
#       break


#u=float(input("Enter your total marks : "))
#if 90<=u<=100:
#    print("Outstanding! you got A+.")
#elif 80<=u<90:
#    print(" Excellent!  you got A.")
#else:
#    print("Poor grade , keep move on.")


#li= {1,2,5,9,6 }        #1,2,5,9,6     #  [1,2,5,9,6]
#n= int(input("number"))
#for i, v in enumerate(li):
#     if n==v:
#        print("The given number of it's index is",i)
#        break



#art="Today the technology one of the significantly to us. All the technology based on Artificial Intelligence.  By Mark Zuckerberg."


#art=input("\t What's new today.? ").strip().lower()
#z= "mark zuckerberg"
#if z  in art:
#     print(f"Great!  your post about {z}.")
#else:
#     print("I think your post about someone else.")

#list=["Mathematices","Physics","Chemistry"]
#i=0
#while i<len(list):
#      print(list[i])
#      i+=1

#for i in range(0,50):
#    print(i)
#else :
      #print("done)
      
  

#s="py"
#print(not(not (s or "")))

#str = "GFG"
#print(not (not(str and " ")))

#d=""
#a=" "
#print(len(d))
#print(len(a))

#print(oct(23) + oct(23))
#print((~9))
#print(2%5)

#print(1_00_000)


#import math
#print(abs(4/9))
#print(float('inf'))
#z=math.log(16,2)
#print(z)

#print(float("inf"))
#print("dgdh")

#li={"py","floor",6,0,1,6,7,3}
#for i in li :
# print(i)
# 
 #True= False
# while True:
#     print(True)
#     break

#d={0,1,3}
#for i in d:
#    print(i)

#str="1,2,3,[4,5,6]"#immutable
#print(len(str))
#print(str.replace("4","9"))
#print(str)


#li=[1,2,(10,5,7),{1,1,8,5,5,6},{2:"repl",7:"mutable"}]
#print(id(li))
#print(len(li))#mutable
#li.insert(2,0)
#print(li)

#li.remove(2)
#z=li[2]
#print(li,z)

#li.append({4:"hackathon"})
#print(li)

#l=[8,5,4,[123,456]]

#print(l)
#l.remove(5
#print(l)
#set={75,875,62,{25,876}}
#print(len(set))


set={"philosophy","egypt","atronome","weapon"}
s={82,75,1,56,3}
print(s.pop())