#!/bin/sh

# Variables can either be defined and directly used...
SOME_VAR="Hello World!"
echo "${SOME_VAR}"

# ...or provided during script invocation like in this task.
# When this script is executed, the REPO_URL variable will
# already be set, so you should use it in your code *without*
# re-defining it!

# To refer to the REPO_URL variable in this script, use the
# following syntax: "${REPO_URL}"
# including the quotation marks

# Add your terminal commands below. Make sure to first run them
# locally on your machine to have more detailed error output.
# When running your script locally, make sure you provide
# REPO_URL on the command line when invoking script.sh as explained
# in the instructions:
REPO_URL="some-url" ./script.sh

 git clone "${REPO_URL}" repo
 cd repo
printf "ccc" > c.txt
git add .
git commit -am "Add new file c.txt with some content"
git push origin main