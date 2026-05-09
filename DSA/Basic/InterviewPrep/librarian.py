def keyword_index(docs):

    words = set()
    for line in docs:
        for word in line.split():
            words.add(word)

    res = {}

    for word in words:
        tmpDict = {}
        for index, line in enumerate(docs):
            if word in line:
                tmpDict[index] = line.split().count(word)
                # if we use line.count(word) then "python is a snake".count('a') 
                # will give 2 which is incorrect!

        if (tmpDict):
            res[word] = tmpDict

    return res

# Optimized solution O(n)
def keyword_index_opt(docs):

    res = {}

    for i, line in enumerate(docs):
        for word in line.split():
            if word not in res:
                res[word] = {i: 1}
            else:
                if i not in res[word]:
                    res[word][i] = 1
                else:
                    res[word][i] = res[word][i] + 1

    return res


docs = ["Hello world", "world of python", "python is a snake"]
print(keyword_index_opt(docs))

# Expected output: {'Hello': {0: 1}, 'world': {0: 1, 1: 1}, 'of': {1: 1}, 'python': {1: 1, 2: 1},
# 'is': {2: 1}, 'a': {2: 1}, 'snake': {2: 1}}
