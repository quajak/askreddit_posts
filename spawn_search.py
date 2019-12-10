# will get one month of data as quick as possible
import subprocess

year = 2019
month = 2
day = 0
for i in range(30):
    day += 1
    subprocess.Popen("python search.py " + str(year) + " " + str(month)  + " "+ str(day))

print("Finished spawning processes!")