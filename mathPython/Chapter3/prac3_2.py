from Chapter3.practice3_1 import calculate_mean,calculate_median,calculate_mode,calculate_mode_plus
from Chapter3.practice3_2 import frequency_table
from Chapter3.practice3_4 import find_differences,calculate_variance

donations = []

with open("mydata.txt") as f:
    for line in f:
        donations.append(int(line))

print("平均:{}\n".format(calculate_mean(donations)))
print("中央値:{}\n".format(calculate_median(donations)))
print("最頻値:{}\n".format(calculate_mode_plus(donations)))
print("差異:{}\n".format(find_differences(donations)))
print("分散:{}\n".format(calculate_variance(donations)))
print("標準偏差:{}\n".format(calculate_variance(donations) ** 0.5))






