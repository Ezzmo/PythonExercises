file = open("teams.txt", "w+")

teams = ["Man Utd", "Man City", "Liverpool", "Arsenal", "Leicester"]

for i in range(len(teams)):
    file.write(teams[i]+"\n")
    file.readline()
file.close()

file = open("teams.txt","r")
for i, b in enumerate(file):
    if i==0 or i==3:
        print(b)
