'''day= {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

number =int(input())
if number in day:
    day=day[number]
    print(day)
else:
    print("Invalid input")'''


class A:
    def m1(self):
        print("m1 in class A")
class B(A):
    def m2(self):
        print("m2 in class B")
class C(B):
    def m3(self):
        print("m3 in class C")

obj_c=C()
obj_c.m1()
obj_c.m2()
obj_c.m3()


