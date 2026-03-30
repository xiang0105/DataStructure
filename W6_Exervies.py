# In-class exercises 1

# 0. 引入套件
from collections import deque

# 1. 建立一個名為 barracks 的 Queue
barracks = deque()

# 2. 玩家依序點擊生產：劍士、弓手、騎士
barracks.append("劍士")
barracks.append("弓手")
barracks.append("騎士")
print(f"目前排隊名單：{list(barracks)}")

# 3. 兵營生產完畢，請將排在最前面的單位拿出來
finished_unit = barracks.popleft()
print(f"生產完成：{finished_unit} 出列！")
print(f"剩下的排隊名單：{list(barracks)}")


# In-class exercises 2

# 0. 引入套件
from collections import deque 

barracks = deque(["劍士", "弓手"])
print(f"初始狀態：{list(barracks)}")

print("\n--- 測試 1：玩家想再塞一個『騎士』進來 (防爆測試) ---")

# 任務 1：請檢查 barracks 長度。如果小於 2 才能加進去
if len(barracks) < 2:
    barracks.append("騎士")
    print("騎士排隊成功！")
else:
    print("產線全滿，拒絕騎士！")

print("\n--- 測試 2：系統瘋狂加速，連續出列 3 次 (防呆測試) ---")

# 任務 2：我們手動複製貼上 3 次出列動作。請加上防呆機制，避免第 3 次 Error
# (第 1 次出列)
if len(barracks) > 0:
    print(f"{barracks.popleft()} 生產完成！")
else:
    print("兵營閒置中，無法出列")

# (第 2 次出列)
if len(barracks) > 0:
    print(f"{barracks.popleft()} 生產完成！")
else:
    print("兵營閒置中，無法出列")

# (第 3 次出列 - 這裡會觸發防呆)
if len(barracks) > 0:
    print(f"{barracks.popleft()} 生產完成！")
else:
    print("兵營閒置中，無法出列")