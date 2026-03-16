# 1.假設有一個 arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])。請問執行 arr[:2, 1:] 會得到什麼結果？
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[:2, 1:])

# ans = [[1,2],[5,6]]

# 2.假設有 numpy arr1 = [10, 20, 30] 與 arr2 = [2, 2, 3]。若要計算各元素相乘，哪種寫法最正確 ?

import numpy as np
arr1 = np.array([10, 20, 30])
arr2 = np.array([2, 2, 3])

print(arr1 * arr2) 
# ans = arr1 * arr2

# 3.假設有一個形狀為 (10000, 10000) 的二維陣列 arr。若要計算「每 row 的總和」該怎麼寫 ?

import numpy as np
arr = np.random.rand(10000, 10000)  # 假設這是你的二維陣列
print(arr.sum(axis=1))

# ans = arr.sum(axis=1)

# 4.假設你有一個包含一百萬個隨機浮點數的一維陣列 data。現在你想把其中「大於 0 的數字」全部挑出來組成一個新的陣列。下列哪一種寫法執行速度最快？

# ans = data[data > 0]

# 假設需要實作一個 ReLU 函數的效果，該怎麼寫?

# ans = np.maximum(0, data)