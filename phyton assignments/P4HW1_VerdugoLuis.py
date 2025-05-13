# verdugo luis
# 05/01/2025
# P4HW1
# SCORES

score_num = int(input("How many scores do you want to enter? "))
print()

# empty list
scores = []

for num in range(1, score_num + 1):
    # collect scores
    score = float(input("Enter score #" + str(num) + ": "))
    # Evaluate entry
    while score < 0 or score > 100:
      print("Invalid Score Entered!!!")
      print("Score should be between 0 and 100")
      score = float(input("Enter score #" + str(num) + " again: "))
    scores.append(score)
    print()

# find lowest score
lowest = min(scores)
scores_modified = scores.copy()
scores_modified.remove(lowest)

# calculate average
average = sum(scores_modified) / len(scores_modified)

# determine grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# DISPLAY results
print("--------------Results--------------")
print(f"{'Lowest Score:':<15} {lowest}")
print(f"{'Modified List:':<15} {scores_modified}")
print(f"{'Scores Average:':<15} {average:.2f}")
print(f"{'Grade:':<15} {grade}")
print("-----------------------------------")
