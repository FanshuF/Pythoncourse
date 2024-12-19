def calculate_bonus(profit):
    bonus = 0
    if profit <= 100000:
        bonus = int(profit * 0.1)  # 低于或等于10万元时，奖金可提10%
    elif profit <= 200000:
        bonus = int(100000 * 0.1 + (profit - 100000) * 0.075)  # 高于10万元，低于20万元时
    elif profit <= 400000:
        bonus = int(100000 * 0.1 + 100000 * 0.075 + (profit - 200000) * 0.05)  # 20万到40万之间时
    elif profit <= 600000:
        bonus = int(100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + (profit - 400000) * 0.03)  # 40万到60万之间时
    elif profit <= 1000000:
        bonus = int(
            100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + (profit - 600000) * 0.015)  # 60万到100万之间时
    else:
        bonus = int(100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + 400000 * 0.015 + (
                    profit - 1000000) * 0.01)  # 高于100万元时

    return bonus

I = float(input("请输入当月利润："))
bonus = calculate_bonus(I)
print(f"应发放的奖金总数为：{bonus}元")