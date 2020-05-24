# %%
import pandas as pd
import numpy as np
import time
# %%

l = np.random.randint(0, 10, 100000)
# print(l)
print("配列の長さ:", len(l))

start = time.time()
# print("演算配列",l)
total = 0

for x in l:
    total = total+x

# print("演算結果",total)
print("----- for文")
print("処理時間:", time.time() - start)

df = pd.DataFrame(l)
# print(df)

start = time.time()
# print("演算配列", l)

# print("演算結果", df.sum())
print("----- df.sum()")
print("処理時間:", time.time() - start)

# %%
