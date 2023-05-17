sentence = input()
n = int(input())
words = set(input() for _ in range(n))
dp = [int(1e9)] * (len(sentence) + 1)

for i in range(1, len(sentence) + 1):
    for j in range(i):
        curr_word = sentence[j:i]
        n_curr = len(curr_word)
        for word in words:
            n_word = len(word)
            if n_word != n_curr:
                continue

            d1 = {}
            for c in word:
                if c in d1.keys():
                    d1[c] += 1
                else:
                    d1[c] = 1

            d2 = {}
            for c in curr_word:
                if c in d2.keys():
                    d2[c] += 1
                else:
                    d2[c] = 1

            if d1 != d2:
                continue

            cnt = 0
            for c in range(n_word):
                if word[c] != curr_word[c]:
                    cnt += 1

            if j == 0:
                dp[i] = min(dp[i], cnt)
            else:
                dp[i] = min(dp[i], dp[j] + cnt)
print(dp[-1] if dp[-1] != int(1e9) else -1)
