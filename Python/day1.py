def name():
    while True:
        a = input("enter your name: ").strip()
        if a.isalpha():
            return f"hello {a} nice to meet you."
        else:
            print("invalid please enter (letters only)")
            
print(name())