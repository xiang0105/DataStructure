from collections import deque

player_gold = 150 
barracks_A = deque() 
barracks_B = deque() 

orders = [
    {}, {}, {}, {}, # 這些是空單
    {"unit": "劍士", "cost": 20},
    {"unit": "弓手", "cost": 30},
    {"unit": "騎士", "cost": 50},
    {"unit": "投石車", "cost": 40}
]

for round_num, order in enumerate(orders):
    print(f"\n--- 第 {round_num} 回合 ---")

    # 1. 不管有沒有訂單，偶數回合都要先「出列」（生產完成）
    if round_num % 2 == 0 and round_num != 0: # 排除第0回合還沒開始做的情況
        if barracks_A: # 這是 if len(barracks_A) > 0 的簡寫
            print(f"A廠生產完成: {barracks_A.popleft()} 出列")
        if barracks_B:
            print(f"B廠生產完成: {barracks_B.popleft()} 出列")

    # 2. 檢查這回合有沒有「訂單內容」
    # 如果 order 裡面沒有 unit，代表是空單，直接進下一輪
    if "unit" not in order:
        print("本回合無新訂單")
        print(f"目前產線 A: {list(barracks_A)} | B: {list(barracks_B)}")
        continue

    # 3. 既然有訂單，才開始處理扣錢與分配
    cost = order["cost"]
    unit = order["unit"]

    if player_gold < cost:
        print(f"黃金不足，無法生產 {unit}")
    else:
        # 分配邏輯
        if len(barracks_A) < 2 and len(barracks_A) <= len(barracks_B):
             player_gold -= cost
             barracks_A.append(unit)
             print(f"{unit} 分配至 A廠 | 剩餘黃金 {player_gold}")
        elif len(barracks_B) < 2:
            player_gold -= cost
            barracks_B.append(unit)
            print(f"{unit} 分配至 B廠 | 剩餘黃金 {player_gold}")
        else:
            print(f"產線全滿！{unit} 訂單拒絕")

    print(f"A: {list(barracks_A)} | B: {list(barracks_B)}")