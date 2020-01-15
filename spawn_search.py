# will get one month of data as quick as possible
import subprocess

year = 2018
month = 3
day = 0
for i in range(30):
    day += 1
    command = "python search.py " + str(year) + " " + str(month)  + " "+ str(day)
    print(command)
    subprocess.Popen(command)

print("Finished spawning processes!")