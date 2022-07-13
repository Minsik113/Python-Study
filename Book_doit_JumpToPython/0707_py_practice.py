a=  input()
print(a)



# %%
a=list("pithon")
a[1]="y"
print(''.join(a))
# %%
pin="881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
b=pin.split('-')
print(b[1][0])
# %%
#문제6
a = int(input("당신의 나이는 몇살이세요?"))
print("제 나이는 %d 입니다" %a)
print(f"제 나이는 {a}입니다.")

#문제7
name = input("당신의 이름은?")
print("제 이름은 %s 입니다." % name)
print(f"제 나이는 {name}입니다.")

#문제8
print("제 나이는 %d 이고, 이름은 %s 입니다." %(a,name))
print(f"제 나이는 {a} 이고, 이름은 {name} 입니다.")
#%%

money = int(input())
print("교환할돈: ", money)
c500 = money // 500
# money -= c500*500
money %= 500

c100 = money // 100
# money -= c100*100
money %= 100

c50 = money // 50
# money -= c50*50
money %= 50

c10 = money // 10
# money -= c10*10
money %= 10

print(c500, c100, c50, c10)
# %%
a = "Life-is-too short"
a.replace("Life","Your leg")
a.split('-')


#%%
#문제1
sesac= ['red', 'blue', 'green'] 
print(sesac[0])
print(sesac[2])
print(len(sesac))

#문제2
sesac="python1"
print(sesac)
print(sesac[3:]) # hon1
print(sesac[:3]) # pyt
print(sesac[:4]) # pyth
print(sesac[:6]) # python#문제3

#문제3
sesac1 = ['red', 'blue', 'green']
sesac2 = ['orange', 'black','white']
sesac3 = sesac1 + sesac2
print(sesac3)
print(sesac1*2)
print(sesac3[:-1])

#문제4
mySesac= [ [ 1, 2, 3, 4] ,[5, 6, 7, 8] ,[9, 10, 11, 12] ]
print(mySesac[0][1]) #2
print(mySesac[1][3]) #8
print(mySesac[2]) #[9,10,11,12]

#문제5
sesac = [ '설현' , '초아' , '지민', '유나' , '유경', '혜정' , '민아', '찬미' ]
print(sesac[2])
print(sesac[-2])
print([sesac[0]])
print([sesac[-2],sesac[-1]])
print([sesac[1],sesac[2]])
print([sesac[1],sesac[4],sesac[-1]])

#문제6
money = int(input("교환할 돈은 얼마?"))
money = 999999
c50000 = money // 50000; money %= 50000
c10000 = money // 10000; money %= 10000
c5000  = money // 5000; money %= 5000
c1000  = money // 1000; money %= 1000
rest   = money
print(c50000, c10000, c5000, c1000, rest)
