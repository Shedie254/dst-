def findJudge(N, trust):
    """
    The town judge is the person who is trusted by everyone (except themself)
    and trusts no one.

    We can solve this problem by keeping track of the in-degree and out-degree of each person.
    The in-degree is the number of people who trust a person, and the out-degree is the number of people
    a person trusts.

    The town judge will have an in-degree of n - 1 (everyone trusts them except themself) and an out-degree of 0
    (they trust no one).
    """
    indegree = [0] * (N + 1)  # indegree[i] stores the number of people who trust person i
    outdegree = [0] * (N + 1)  # outdegree[i] stores the number of people person i trusts

    # For each trust relationship (a, b), increment indegree[b] and outdegree[a]
    for i, j in trust:
        outdegree[i] += 1
        indegree[j] += 1

    # The town judge is the person with in-degree n - 1 and out-degree 0
    for i in range(1, N + 1):
        if indegree[i] == N - 1 and outdegree[i] == 0:
            return i

    return -1

# Example usage:
N = 2
trust = [[1, 2]]
judge = findJudge(N, trust)
print(judge)  # Output: 2

N = 3
trust = [[1, 3], [2, 3]]
judge = findJudge(N, trust)
print(judge)  # Output: 3

N = 4
trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
judge = findJudge(N, trust)
print(judge)  # Output: -1
