from isitleapyear import is_it_leap_year
from zhSzamolo import how_many_points_i_need
from fibonacci import fibonacci_sequence

for year in range(1900, 1902):
    print("Is " + str(year) + " a leap year? " + str(is_it_leap_year(year)))

how_many_points_i_need()

fibonacci_sequence(1000)
