year = int(input())
Century = year // 100 + 1
Golden_number = (year % 19)+1
Julian_epact = (11 * (Golden_number-1)) % 30
Difference_Jul_Gre =(3*Century/4)
Difference_Jul_Met = (8*Century+5)/25
Gregorian_epact = Julian_epact - Difference_Jul_Gre + Difference_Jul_Met + 8
print (int(Gregorian_epact))




