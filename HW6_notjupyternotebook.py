#hw 6
# 6.20 v = TACGGGTAT, w = GGATACGTACG
# match premium +1, indel penalty is -1
# fill out dynamic programming table for alignment between v and w,
# draw arrows in cells to store backtrack infromation
# find score of optimal global alignment and what alignment does this score correspond to?
def optimal_global_alignment(v,w):
    graph = []
    rows = len(v)
    cols = len(w)
    counteri = 0
    counterj = 0
    for i in range(rows+1):
        temp = []
        for j in range(cols+1):
            if i == 0:
                temp.append(counteri)
                counteri -= 1
            elif j == 0:
                temp.append(counterj)
                counterj -= 1
            elif v[i] != w[j]:
                temp.append(min(temp[j-1],graph[i-1][j],graph[i-1][j-1]))
            else:
                temp.append(min(temp[j-1],graph[i-1][j],graph[i-1][j-1]+1))
        graph.append(temp)
    print(graph)

optimal_global_alignment("TACGGGTAT","GGATACGTACG")


