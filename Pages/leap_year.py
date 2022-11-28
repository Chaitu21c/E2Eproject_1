global leap
def is_leap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                leap=True
                print(leap)
        else:
            leap=True
            print(leap)
    else:
        leap = False
        print(leap)
year=int(input("enter year: "))
is_leap(year)
