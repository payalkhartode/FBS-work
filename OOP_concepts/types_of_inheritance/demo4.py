
num1 = 10
num2 = 20
sum_int = num1 + num2
print(sum_int)


str1 = "Virat "
str2 = "Koholi"
sum_str = str1 + str2
print(sum_str)


list1 = [1, 2, 3]
list2 = [4, 5, 6]
sum_list = list1 + list2
print(sum_list)

class Time:
    def __init__(self, hr, min, sec):
        self.hr = hr
        self.min = min
        self.sec = sec

    def __str__(self):
        return f"{self.hr} : {self.min} : {self.sec}"

    def __add__(self, other):
        tsec = self.sec + other.sec
        addmin = tsec // 60
        tsec = tsec % 60
        tmin = self.min + other.min + addmin
        addhr = tmin // 60
        tmin = tmin % 60
        thr = self.hr + other.hr + addhr
        return Time(thr, tmin, tsec)
        # thr=self.hr+other.hr
        # tmin=self.min+other.min
        # tSec=self.sec+other.sec
        # t=Time(thr,tmin,tSec)
        # return t
        # # return "I am in addition"


t1 = Time(12, 14, 60)
t2 = Time(7, 55, 45)
# print(t1)
# print(t2)
print(t1 + t2)
