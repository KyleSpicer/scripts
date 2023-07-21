#!/bin/bash

# This script generates a list of username-password pairs with updated numbers.

# It uses a for loop to iterate a specified number of times, generating pairs in the following format:
# username1:password1
# username2:password2
# ...

# The script then saves the generated output string to an output file name "credentials.txt" in the current directory.

# Ensure you change permissions of the file using "chmod +x", to make the script executable.

num_iters=1000

output_string=""

for ((i=1; i<=$num_iters; i++)); do
	username="username$i"
	password="password$i"
	output_string+="\n$username:$password"
done

# remove leading newline character from output string
output_string="${output_string#\\n}"

# write result to output file
output_file="credentials.txt"

echo -e "$output_string" > "$output_file"

echo -e "Generated credentials saved to $output_file"
