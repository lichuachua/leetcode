class Solution:
    def findRepeatDocument(self, documents: List[int]) -> int:
        for i in range(len(documents)):
            while documents[i] != i:
                if documents[documents[i]] == documents[i]:
                    return documents[i]
                # 先给 documents[documents[i]]赋值，不影响documents[i]的值
                documents[documents[i]], documents[i] = documents[i], documents[documents[i]]
                ''''
                documents[i], documents[documents[i]] = documents[documents[i]], documents[i]
                这种写法会导致先给documents[i]赋值，再对documents[documents[i]]赋值（documents[i]是新更新的值），导致错误---死循环
                '''
                '''
                也可以直接使用下面的这种写法
                tmp = documents[documents[i]]
                documents[documents[i]] = documents[i]
                documents[i] = tmp
                '''
        return 0
