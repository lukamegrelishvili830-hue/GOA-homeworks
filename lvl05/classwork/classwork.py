# 1)მომხმარებელს შემოატანინეთ თავისი საყვარელი ფერი input-ის მეშვეობით, შეინახეთ იგი ცვლადში და დაბეჭდეთ ტექსტი: „თქვენი საყვარელი ფერია: [ფერი]“.
fav_color = input("enter your favourite color:")
print("your favourite color is",fav_color)
# 2)მომხმარებელს შემოატანინეთ 2 ცალი რიცხვი სხვადასხვა დამოუკიდებელი input-ის მეშვეობით, თქვენი დავალებაა ეს რიცხვები გადაიყვანოთ მთელ რიცხვებად (int()) და დაბეჭდოთ მათი ნამრავლი.
num_1 = int(input("enter the first number:"))
num_2 = int(input("enter the second number:"))
print(num_1 * num_2)
# 3)მომხმარებელს შემოატანინეთ თავისი წელი (მაგალითად, დაბადების წელი), გადაიყვანეთ ის integer ტიპად, გამოთვალეთ რამდენი წლის იქნებიან 2026 წელს და დაბეჭდეთ შედეგი.
birth_year = int(input("enter your birth year:"))
age_in_2026 = 2026 - birth_year
print(age_in_2026)
# 4)მომხმარებელს შემოატანინეთ რიცხვი input-ის მეშვეობით (ის ავ
user_input = input("enter: ")
print(type(user_input))
converted_value = int(user_input)
print(type(converted_value))