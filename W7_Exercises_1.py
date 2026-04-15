def balanced_push(stacks, data):
    # 步驟一：Overflow 檢查

    if len(stacks[-1]) < 6:
        return "Error: No stacks available.", stacks
            
    # 步驟二：尋找目標 Stack，設定初始值以利後續比較
    min_len = 5          # 思考：尋找最小值時，初始的比較基準應該設為多少 ?
    target_idx = -1     # 用來記錄最終決定要放入的 Stack 編號

    for i in range(len(stacks)):
        current_len = len(stacks[i])

        # 步驟三：比較邏輯，同時解決「找最少」與「同數量找最小編號」兩個問題 ?
        if current_len < min_len:
            min_len = current_len
            target_idx = i

    # 步驟四：將資料放入找到的目標 Stack
    if target_idx != -1:
        stacks[target_idx].append(data)

    return stacks


# ----------------------------------------
# 測試區 : 測資 A
#   - [['A', 'D'], ['B'], ['C']]

server_stacks = [[], [], []]
balanced_push(server_stacks, "A")
balanced_push(server_stacks, "B")
balanced_push(server_stacks, "C")
balanced_push(server_stacks, "D")

print(server_stacks)  # 預期輸出 : [['A', 'D'], ['B'], ['C']]

# 測試區 : 測資 B
#   - 模擬系統已經運行一段時間的狀態
#   - [['A', 'B', 'C'], ['D', 'E', 'X'], ['F', 'G']]

server_stacks = [['A', 'B', 'C'], ['D', 'E'], ['F', 'G']]
balanced_push(server_stacks, "X")

print(server_stacks)  # 預期輸出 : [['A', 'B', 'C'], ['D', 'E', 'X'], ['F', 'G']]

# 測試區 : 測資 C
#   - Server Full

server_stacks = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
]
balanced_push(server_stacks, "999")

print(server_stacks)  # 預期輸出 : Error: No stacks available. [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
