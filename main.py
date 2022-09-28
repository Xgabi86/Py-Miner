a = "abcd"
with open('DB1.txt', 'w') as writer:
    writer.write(a)
    print("DB1 Set to:")
    print(a)