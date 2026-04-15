
from collections import deque

def warehouse_process(s1, s2, q, action, item=None):
    if action == "ARRIVE":
        s1.append(item)
    elif action == "SHIP":
        # 任務 2：判斷是否完全沒貨
        if len(s1) == 0 and len(s2) == 0:
            print("Error: No items to ship.")
            return

        # 任務 3：如果分類區 (s2) 是空的，把進貨區 (s1) 倒過來
        if len(s2) == 0:
            while s1:
                s2.append(s1.pop())

        # 任務 4：從分類區出貨到貨車 Q
        shipped_item = s2.pop()
        q.append(shipped_item)
        print(f"Shipped: {shipped_item}")

# --- 練習區 ---
s1 = []     # 進貨區
s2 = []     # 分類區
q = deque() # 貨車 (使用 deque 模擬 Queue)

# ==========================================
# 測資 A：基礎轉換測試 (驗證 FIFO 是否達成)
# ==========================================
print("=== 執行測資 A ===")
warehouse_process(s1, s2, q, "ARRIVE", 1)
warehouse_process(s1, s2, q, "ARRIVE", 2)
warehouse_process(s1, s2, q, "SHIP")
warehouse_process(s1, s2, q, "SHIP")
print(f"測資 A 貨車最終清單: {list(q)}")
# 預期結果: [1, 2]


# 重置貨車 Q 以便進行下一個測資
q.clear()
# ==========================================
# 測資 B：動態進出貨測試 (驗證 S2 優先權)
# ==========================================
print("\n=== 執行測資 B ===")
warehouse_process(s1, s2, q, "ARRIVE", 1)
warehouse_process(s1, s2, q, "ARRIVE", 2)
warehouse_process(s1, s2, q, "SHIP")
warehouse_process(s1, s2, q, "ARRIVE", 3)
warehouse_process(s1, s2, q, "SHIP")
print(f"測資 B 貨車最終清單: {list(q)}")