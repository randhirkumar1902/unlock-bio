print('''script is written by...
..............................Aashi anonyomous😊
''')
print("Starting Program....")
num = int(input("Enter the time without space "))

if num < 0 or num > 9999:
    print("Invalid input!")
else:
    result = (9999 - num) * (9999 - num)
    print("password found:", result)