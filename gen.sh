# small hack cos I too stupid to figure out the python packaging
# this file, copies the `regex.txt` file to a python file, which python 
# package makes use of it
touch regex.py
echo '# This file is auto generated using `gen.sh`. Do not modify.\n\nregex_string = """' > regex.py
cat regex.txt >> regex.py
echo '"""' >> regex.py
mv regex.py src/pincode/regex_codes.py

