# Verdugo Luis
# 04/24/2025
# P2HW2
# grades 
# calculate grades

# calling math module function.
import math
# display/print title
print('----------Grades------------')
# inputs & assignments
print('Enter grade for Module 1:', end=' ')
m1 = float(input())
print('Enter grade for Module 2:', end=' ')
m2 = float(input())
print('Enter grade for Module 3:', end=' ')
m3 = float(input())
print('Enter grade for Module 4:', end=' ')
m4 = float(input())
print('Enter grade for Module 5:', end=' ')
m5 = float(input())
print('Enter grade for Module 6:', end=' ')
m6 = float(input())
# variables / math calculations
largest = max(m1,m2,m3,m4,m5,m6)
lowest = min(m1,m2,m3,m4,m5,m6)
module_sum = m1+m2+m3+m4+m5+m6
average = module_sum / 6
# print/display results
print('----------Results-----------')
print(f"{'Lowest Grade:':<20} {lowest:.1f}")
print(f"{'Highest Grade:':<20} {largest:.1f}")
print(f"{'Sum of Grades:':<20} {module_sum:.1f}")
print(f"{'Average:':<20} {average:.2f}")
print("----------------------------")
