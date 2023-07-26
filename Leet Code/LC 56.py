from collections import Counter
ransomNote="aa"
magazine="aab"

a=Counter(ransomNote)
b=Counter(magazine)

if a<=b:

    print("TRUE")

else:

    print("FALSE")
