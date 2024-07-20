def generateParanthesis(n):
    res = []
    stack = []
    nClosed, nOpened = 0, 0
    def backtrack(nClosed, nOpened):
        if nClosed == nOpened == n:
            res.append("".join(stack))
        if nClosed < nOpened:
            stack.append(")")
            backtrack(nClosed + 1, nOpened)
            stack.pop()
        if nOpened < n:
            stack.append("(")
            backtrack(nClosed, nOpened + 1)
            stack.pop()

    backtrack(0, 0)


    return res


print(generateParanthesis(4))

