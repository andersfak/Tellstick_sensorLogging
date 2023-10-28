import subprocess

# Run the tdtool command and capture its output
try:
    command_output = subprocess.check_output(['tdtool', '--list-sensors'], stderr=subprocess.STDOUT, text=True)
except subprocess.CalledProcessError as e:
    print(f"Error running tdtool: {e.output}")
    exit(1)

# Specify the filename to append the output
output_filename = 'sensor_list.txt'

calibrate = -0.5

lines = command_output.splitlines()
with open(output_filename, 'a') as file:
	for line in lines:
		if "id=247" in line or "id=13" in line:
			values = line.split("\t")
			values[4] = values[4].replace("temperature=","")
			temp = float(values[4]) + calibrate
			valueTime = values[6].replace("time=","")
			
			# age is sensor last heard
			age = values[7]

			file.write(str(temp) + "\t" + valueTime + "\t" + age + "\n")
