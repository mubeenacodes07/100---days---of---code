s = input("enter name/number: ").lower()
if s == s[::-1]:
    print("palindromic")
else:
    print("not palindromic")