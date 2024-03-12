# 6. Given a sentence with missing words and an array of
# words. Replace all ‘_’ in a sentence with the words from
# the array.


def ashot(a: str):
    a = a.split(' ')
    list2 = ['Ashot', 'problem']

    if '_' in a:
        for i in range(len(a)):
            if a[i] == '_':
                a[i] = list2[0]
                del list2[0]
    return " ".join(a)


print(ashot('_ we have a _ .'))
 