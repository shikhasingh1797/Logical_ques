marri=256
month="09"
year=int(input())
jan=31
feb=29
mar=31
apr=30
may=31
june=30
july=31
aug=31
date=0
total=0
date1=0
total1=0
if year %4==0:
    total=jan+feb+mar+apr+may+june+july+aug
    date=marri-total
    print(date)
    d=str(date)
    m=str(month)
    y=str(year)
    print(d+"."+m+"."+y)
else:
    total1=(jan+feb+mar+apr+may+june+july+aug)-1
    date1=marri-total1
    d=str(date1)
    m=str(month)
    y=str(year)
    print(d+"."+m+"."+y)



# HACKERRANK SOLUTION

# marri=256
#     month="09"
#     jan=31
#     feb=29
#     mar=31
#     apr=30
#     may=31
#     june=30
#     july=31
#     aug=31
#     date=0
#     total=0
#     date1=0
#     total1=0
#     if year==1918:
#         return "26.09.1918"
#     if year==1900 or year==2000 or year==2400:
#         y=str(year)
#         return "12.09."+y
#     if year >1800 and year%100==0:
#         total1=(jan+feb+mar+apr+may+june+july+aug)-1
#         date1=marri-total1
#         d=str(date1)
#         m=str(month)
#         y=str(year)
#         return (d+"."+m+"."+y)
#     if year %4==0:
#         total=jan+feb+mar+apr+may+june+july+aug
#         date=marri-total
#         print(date)
#         d=str(date)
#         m=str(month)
#         y=str(year)
#         return (d+"."+m+"."+y)
#     else:
#         total1=(jan+feb+mar+apr+may+june+july+aug)-1
#         date1=marri-total1
#         d=str(date1)
#         m=str(month)
#         y=str(year)
#         return (d+"."+m+"."+y)