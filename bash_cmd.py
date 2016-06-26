bashCommand = "ls"
import subprocess
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output = process.communicate()[0].split("\n")[:-1]
print(output[0])
for file in output:
    print(file)