import numpy as np

def NeedlemanWunsch(a, b, i, j, score, penalty, arr, Parent):
    if i == 0 and j == 0:
        return 0
    elif arr[i][j] != -1:
        return arr[i][j]
    else:
        if i > 0 and j > 0:
            if a[i-1] == b[j-1]:
                s = score
                arr[i][j] = NeedlemanWunsch(a, b, i-1, j-1, score, penalty, arr, Parent) + s
                Parent[i][j] = (i-1, j-1)
            else:
                s = penalty
                diag = NeedlemanWunsch(a, b, i-1, j-1, score, penalty, arr, Parent)
                up = NeedlemanWunsch(a, b, i-1, j, score, penalty, arr, Parent)
                left = NeedlemanWunsch(a, b, i, j-1, score, penalty, arr, Parent)
                arr[i][j] = max(diag, up, left) + s
                if diag == arr[i][j]-s:
                    Parent[i][j] = (i-1, j-1)
                elif up == arr[i][j]-s:
                    Parent[i][j] = (i-1, j)
                elif left == arr[i][j]-s:
                    Parent[i][j] = (i, j-1)
        elif i > 0:
            s = penalty
            arr[i][j] = NeedlemanWunsch(a, b, i-1, j, score, penalty, arr, Parent) + s
            Parent[i][j] = (i-1, j)
        else:
            s = penalty
            arr[i][j] = NeedlemanWunsch(a, b, i, j-1, score, penalty, arr, Parent) + s
            Parent[i][j] = (i, j-1)
        return arr[i][j]

def AlignSequences(a, b, score, penalty):
    rows = len(a)
    cols = len(b)
    arr = np.zeros((rows+1, cols+1), dtype=int)
    arr.fill(-1)
    Parent = [[0]*(cols+1) for i in range(rows+1)]
    max_score = NeedlemanWunsch(a, b, rows, cols, score, penalty, arr, Parent)

    ans = []
    p = []
    i, j = rows, cols
    while(i > 0 or j > 0):
        ans.append(arr[i][j])
        p.append((i,j))
        idx = Parent[i][j]
        i, j = idx[0], idx[1]

    s1 = ''
    s2 = ''
    for i in range(len(p)-1):
        t = p[i]
       
