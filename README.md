# Key Generator

# Installation

```
pip3 install python-keygen
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
