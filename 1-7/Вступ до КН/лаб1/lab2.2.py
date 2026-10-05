a = int(input("Введіть чисельник першого дробу: "))
b = int(input("Введіть знаменник першого дробу: "))
c = int(input("Введіть чисельник другого дробу: "))
d = int(input("Введіть знаменник другого дробу: "))
sum_num = a*d+c*b
sum_den = b*d
diff_num = a*d-c*b
diff_den = b*d
prod_num = a*c
prod_den = b*d

print("Сума:", sum_num, "/", sum_den,
" Різниця:", diff_num, "/", diff_den,
" Добуток:", prod_num, "/", prod_den)