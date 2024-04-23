import subprocess

print("This ran before subprocess")
subprocess.run(["ls", "-l", "/"])
print("This ran after subprocess")