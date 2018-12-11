def ss(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found


def palindrome(word):
    word = word.lower()
    print(word[::-1])  # [::-1]は文字列を逆転させる
    return word[::-1] == word


def anagram(w1,w2):
    # option spaceで定義をだす
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)


def count_characters(string):
    count_dist = {}
    for c in string:
        if c in count_dist:
            count_dist[c] += 1
        else:
            count_dist[c] = 1
    print(count_dist)


if __name__ == '__main__':
    numbers = range(0, 100)
    s1 = ss(numbers, 2)
    print(s1)
    s2 = ss(numbers, 202)
    print(s2)

print(palindrome("Mother"))
print(palindrome("Mom"))
print(anagram("iceman","cinema"))
print(anagram("leaf","tree"))
count_characters("Dynasty")





