ch = input("Enter an alphabet: ")
ch = ch.lower()
if ch in ('a', 'e', 'i', 'o', 'u'):
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")
print("-" * 50)