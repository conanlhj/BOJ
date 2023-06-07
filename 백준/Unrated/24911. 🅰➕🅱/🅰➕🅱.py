d = {
    u"💯": 100, u"🧑‍🏫": 22, u"🧑🏻‍🏫": 22, u"🧑🏼‍🏫": 22,
    u"🧑🏽‍🏫": 22, u"🧑🏾‍🏫": 22, u"🧑🏿‍🏫": 22, u"👩🏻‍🏫": 22,
    u"👩‍🏫": 22, u"👨🏿‍🏫": 22, u"👨🏾‍🏫": 22, u"👨🏽‍🏫": 22,
    u"👨🏼‍🏫": 22, u"👨🏻‍🏫": 22, u"👨‍🏫": 22, u"👩🏼‍🏫": 22,
    u"👩🏽‍🏫": 22, u"👩🏾‍🏫": 22, u"👩🏿‍🏫": 22, u"🏪": 24,
    u"🏎️": 3, u"🥇": 1, u"🥈": 2, u"🥉": 3,
    u"🎱": 8, u"🎰": 777, u"📟": 40404, u"📅": 17,
    u"📆": 17, u"🔞": 18, u"🔂": 1, u"0️⃣": 0,
    u"1️⃣": 1, u"2️⃣": 2, u"3️⃣": 3, u"4️⃣": 4,
    u"5️⃣": 5, u"6️⃣": 6, u"7️⃣": 7, u"8️⃣": 8,
    u"9️⃣": 9, u"🔟": 10, u"🔢": 1234, u"": 109
}


A = input()
B = input()
if A in d:
     a = d[A]
else:
     a = 0
if B in d:
     b = d[B]
else:
     b = 0
sum_ = str(a+b)

dp = [int(1e9)] * (len(sum_)+1)
dp[0] = 0
prev = [""] * (len(sum_)+1)

for i in range(1, len(sum_)+1):
     for key, value in d.items():
          value = str(value)
          if i - len(value) < 0:
               continue
          
          if value == sum_[i-len(value):i]:
               if dp[i] > dp[i-len(value)]+1:
                    dp[i] = dp[i-len(value)]+1
                    prev[i] = key

stack = []
i = len(prev)-1
while i > 0:
     stack.append(prev[i])
     i -= len(str(d[prev[i]]))
print("".join(stack[::-1]))