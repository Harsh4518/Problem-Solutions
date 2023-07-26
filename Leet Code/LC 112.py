s="iloveleetcode"
words=["i","love","leetcode","apples"]

ans=""

for i in words:

    ans+=i

    if ans==s:

        print("True")
        break

else:

    print("False")
