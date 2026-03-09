class Solution:
    def evalRPN(self, tokens):
        stk = []

        for t in tokens:
            if t in ["+", "-", "*", "/"]:
                rtg = stk.pop()
                lft = stk.pop()

                if t == "+":
                    ans = lft + rtg
                elif t == "-":
                    ans = lft - rtg
                elif t == "*":
                    ans = lft * rtg
                else:  # division
                    ans = int(lft / rtg)   # truncate toward zero like C++

                stk.append(ans)
            else:
                stk.append(int(t))

        return stk[-1]