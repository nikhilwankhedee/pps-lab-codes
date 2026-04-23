
scores = (45, 67, 89, 23, 54, 78, 12, 100, 65)

print("Total Runs:", sum(scores))
print("Highest Score:", max(scores))

half_centuries = 0
for s in scores:
    if 50 <= s < 100:
        half_centuries += 1

print("Half Centuries:", half_centuries)

print("Scores in Reverse:")
for s in reversed(scores):
    print(s)
