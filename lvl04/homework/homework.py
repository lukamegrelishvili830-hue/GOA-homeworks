# 2) მომხმარებელს შემოაყვანინე სამი რიცხვი, ხოლო პროგრამამ დაბეჭდოს მათი საშუალო არითმეტიკული.
a = float(input("enter the first number:"))
b = float(input("enter the second number:"))
c = float(input("enter the third number:"))
sashualo = ((a + b + c)/3)
print(sashualo)

# 3) მომხმარებელს შემოატანინე ორი რიცხვი და დაბეჭდე მათი ჯამი.
a = int(input("enter the first number:"))
b = int(input("enter the second:"))
jami = a + b
print(jami)

# 4) input ფუნქციის საშუალებით შემოიყვანეთ თქვენი და თქვენი ოჯახის წევრების სახელები და დაპრინტეთ ერთი დიდი წინადადება კონკატენაციის სახით.
me = input("enter your name:")
bebo = input("enter grandmother's name:")
deda = input("enter mother's name:")
mama = input("enter father's name:")
dzma = input("enter brother's name:")
print( me + " " + bebo + " " + deda + " " + mama + " " + dzma)

# 5) მომხმარებელს შემოატანინეთ მისი ქალაქის, უბნის, კორპუსის და სართულის შესახებ ინფორმაცია (რომლებიც უნდა შეინახოთ ცალ-ცალკე ცვლადებში). მაგ. city = "Tbilisi", District = "{თქვენი უბანი}" და ა.შ. საბოლოოდ print() ბრძანების საშუალებით ტერმინალში გამოიტანეთ მომხმარებლის სრული მისამართი.
city = input("enter your city:")
district = input("enter your district:")
korpusi = input("enter your building number:")
full_adress = city + "" + district + "" + korpusi
print(full_adress)

# 6) მომხმარებელს შემოატანინეთ ასაკი და ამოყენებითმსგავსი ფორმატის წინადადება: 
# "You are ასაკი years old".
asaki = input("enter your age:")
print(" you are " + asaki + " years old ")