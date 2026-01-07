liName = []
liGrade = []
alpha = []
for n in range(int(input())):
    name = input(f"Name {n+1}: ").strip()
    grade = float(input("Grade: "))
    liName.append([name,grade])
    liGrade.append(grade)

second_Minimun = sorted(set(liGrade))[1]
for i in range(len(liName)):
    if liName[i][1] == second_Minimun:
        alpha.append(liName[i][0])

# Alphabatically print
for result in sorted(alpha):
    print(result)