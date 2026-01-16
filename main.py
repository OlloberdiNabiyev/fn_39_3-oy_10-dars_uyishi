from collections import namedtuple


#1
# Student = namedtuple("Student",['name','age','score'])
# students = [
#     ('Bakir',18,70),
#     ('Toxir',24,85),
#     ('Jalil',20,99),
#     ('Nodir',22,60),
#     ('Murod',18,65)
# ]

# for student in students:
#     st = Student(*student)
#     if st.score > 80:
#         print(st.name,st.age,st.score)


# 2
# Product = namedtuple('Product',['name','price','quantity'])
# products = [
#     ('olma',20000,4),
#     ('nok',25000,5),
#     ('ananas',30000,4),
#     ('non',5000,15)
# ]

# for product in products:
#     pr = Product(*product)
#     if (pr.price * pr.quantity) > 100000:
#         print(pr.name,pr.price,pr.quantity)


# 3
# Person = namedtuple('Person',['first_name','last_name','birth_year'])
# people = [
#     ('Bakir','Bakirov',2008),
#     ('Toxir','Bakirov',2002),
#     ('Jalil','Bakirov',2006),
#     ('Nodir','Bakirov',2004),
#     ('Murod','Bakirov',2005)
# ]

# max_age = people[0][2]
# max_name = ''
# max_lastname = ''
# for person in people:
#     pr = Person(*person)
#     if pr.birth_year < max_age:
#         max_age = pr.birth_year
#         max_name = pr.first_name
#         max_lastname = pr.last_name
# print(max_name,max_lastname,max_age)

# 4
# Flight = namedtuple('Flight',['from_city','to_city','duration'])
# flight = [
#     ('Tashkent','Moscow',1.45),
#     ('Moscow','Paris',4),
#     ('Paris','Rio De Janeiro',7),
#     ('Rio De Janeiro','Tashkent',12)
# ]
# total_duration = 0
# for i in flight:
#     fl = Flight(*i)
#     total_duration += fl.duration
#     if fl.duration > 2:
#         print(fl.from_city,fl.to_city,fl.duration)
# print(total_duration)

# 5
# Movie = namedtuple('Movie',['title','rating','year'])
# movies = [
#     ('endi dadam boydoq',9,2016),
#     ('Hijron',6,2010),
#     ('kelin',7,2018),
# ]
# for movie in movies:
#     mov = Movie(*movie)
#     if mov.year > 2015 and mov.rating >= 8:
#         print(movie)

# 6
# numbers = [15, 42, 8, 23, 56, 4, 91, 37, 12, 68]
# total = 0
# for number in numbers:
#     total += number
# print(total / len(numbers))

# 7
# colors = ("red", "green", "blue", "yellow")
# print(colors.index('blue'))
# colors += ('black',) # qoshildi xatosiz lekin ',' qoymaganimda qoshilmasdi chunki uni tuple emas str deb oylab qolardi.
# print(colors)

# 8
# matn = 'Tashkent va Fergana nomer 1'
# raqam = 0
# joy = 0
# harf = 0
# for i in matn:
#     if i.isdigit():
#         raqam += 1
#     elif i.isalpha():
#         harf += 1
#     else:
#         joy += 1
# print(f'matnda {raqam}ta raqam, {joy} ta bosh joy, {harf}ta harf bor')

# 9
# to = range(1,100)
# fa = list(filter(lambda value: value % 5 == 0 and value % 3 != 0,to))
# print(fa)

# 10
# Sequence = namedtuple('Sequence',['title','author','pages'])
# books = [
#     ('dunyoning ishlari','O\'tkir Hoshimov',300),
#     ('sos','nomalum',400),
# ]
# max_page = books[0][2]
# total_pages = 0
# for book in books:
#     b = Sequence(*book)
#     if b.pages > max_page:
#         max_page = b.pages
#     total_pages += b.pages
# print(max_page)
# print(total_pages)