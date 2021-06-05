# Key Generator

# Installation Using PIP
```
pip3 install python-keygen
```
# Using Source Code
```
git clone https://github.com/pmk456/keygen.git
python3 setup.py install
```
# Usage
### To Generate Key
```
from keygen import KeyGen
keygen = KeyGen()
keygen.gen_key(length=20)
```
### To Validate A Key
```
from keygen import KeyGen
keygen = KeyGen()
key = input("Enter Your Key: ")
is_valid = keygen.validate(key) # return true if key is valid else false
if is_valid:
    print("Valid Key")
else:
    print("Not Valid Key")
```
