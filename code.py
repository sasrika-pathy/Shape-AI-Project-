import hashlib
x= input ("enter text")

def main():
    tex= x.encode("utf-8")
    hash= hashlib.md5(tex)
    hex= hash.hexdigest()
    print(hex)
    return
main()
