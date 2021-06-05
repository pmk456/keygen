# Author = Patan Musthakheem
# Version = 1.6
# Licence = Apache 2.0
import random
from string import ascii_uppercase, digits
from sys import exit




class KeyGen:
    def __init__(self):
        self.valid_keys = []

    
    def gen_key(self, length) -> None:
        key_base = 1423
        for i in range(10000000):
            key = ''.join(random.choices(ascii_uppercase + digits, k=20))  
            bases = []
            for k in key:
                base = ord(k)
                bases.append(base)
            if sum(bases) == key_base:
                O1 = key[:4] + "-" + key[4:]
                O2 = O1[:9] + "-" + O1[9:]
                O3 = O2[:14] + "-" + O2[14:]
                Final_Key = O3[:19] + "-" + O3[19:]
                print(f"Valid Key:{Final_Key}")
                self.valid_keys.append(Final_Key)
                if len(self.valid_keys) == length:
                    print(f"[+] Generated {length} Keys")
                    per = input("[+] Save It To A File: ")
                    if per == "y" or per == "Y" or per == "Yes" or per == "yes":
                        name = input("[+] Enter Name For The File: ")
                        try:
                            with open(name, "w") as file:
                                file.write('\n'.join(self.valid_keys))
                        except Exception:
                            print("[-] Cant Save It To A File")
                        else:
                            print("[+] Save Success")  
                    break
    def validate(self, key) -> bool:
        key = key.replace("-", "")
        if len(key) > 20 or len(key) < 20:
            print("[-] Enter Correct Key")
            return None
            exit(1)
        key_base = 1423
        bases = []
        for k in key:
            base = ord(k)
            bases.append(base)
        if sum(bases) == key_base:
            return True
        else:
            return False



__version__ = 1.6
__author__ = "Patan Musthakheem"
__licence__ = "Apache 2.0"











