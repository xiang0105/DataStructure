import numpy as np
import time
from collections import deque

n = 10**7 

def test_performance():
    print(f"測試開始，資料量 n = {n}\n" + "="*50)

    # --- 1. 初始化資料 ---
    arr = np.arange(n)
    lst = list(range(n))
    dq = deque(range(n))

    # --- 2. 測試：查詢 (Accessing Middle) ---
    print(f"【查詢測試 (Accessing n//2)】")
    
    start = time.time()
    _ = arr[n//2]
    print(f"Numpy Array : {time.time() - start:.8f} s (O(1))")

    start = time.time()
    _ = lst[n//2]
    print(f"Python List : {time.time() - start:.8f} s (O(1))")

    start = time.time()
    _ = dq[n//2]
    print(f"Deque       : {time.time() - start:.8f} s (O(n) - 須走訪指標)")
    print("-" * 50)

    # --- 3. 測試：頭部插入 (Insert at Head) ---
    print(f"【頭部插入測試 (Insert at index 0)】")
    
    # Numpy Array (需要整塊記憶體搬移)
    start = time.time()
    _ = np.insert(arr, 0, -1)
    print(f"Numpy Array : {time.time() - start:.8f} s (O(n))")

    # List (需要整塊記憶體搬移)
    start = time.time()
    lst.insert(0, -1)
    print(f"Python List : {time.time() - start:.8f} s (O(n))")

    # Deque (僅需修改指標)
    start = time.time()
    dq.appendleft(-1) 
    print(f"Deque       : {time.time() - start:.8f} s (O(1) - 真正的優勢！)")
    print("-" * 50)

    # --- 4. 測試：中間插入 (Insert at Middle) ---
    print(f"【中間插入測試 (Insert at index n//2)】")
    
    start = time.time()
    _ = np.insert(arr, n//2, -1)
    print(f"Numpy Array : {time.time() - start:.8f} s (O(n))")

    start = time.time()
    lst.insert(n//2, -1)
    print(f"Python List : {time.time() - start:.8f} s (O(n))")

    start = time.time()
    dq.insert(n//2, -1)
    print(f"Deque       : {time.time() - start:.8f} s (O(n) - 因搜尋位置慢)")
    print("-" * 50)

    # --- 5. 測試：尾部插入 (Insert at Tail) ---
    print(f"【尾部插入測試 (Append)】")
    
    start = time.time()
    _ = np.append(arr, -1)
    print(f"Numpy Array : {time.time() - start:.8f} s (通常需重新分配整塊)")

    start = time.time()
    lst.append(-1)
    print(f"Python List : {time.time() - start:.8f} s (O(1) amortized)")

    start = time.time()
    dq.append(-1)
    print(f"Deque       : {time.time() - start:.8f} s (O(1))")

if __name__ == "__main__":
    test_performance()