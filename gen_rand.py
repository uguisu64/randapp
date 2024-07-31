import numpy as np

# 正規分布の乱数を生成する関数
def generate_normal_with_target_mean(target_mean, size):
    # 初期化
    mean_diff = 1.0  # 初期値を大きくとる
    # 平均0, 標準偏差1の正規分布乱数を生成
    data = np.random.normal(loc=0.0, scale=1.0, size=size)
    # 生成した乱数の平均値を計算
    current_mean = np.mean(data)

    # 目標平均値との差を計算
    mean_diff = current_mean - target_mean

    # 乱数全体に差を足して、目標平均値に調整する
    data_adjusted = data - mean_diff

    return data_adjusted

if __name__ == '__main__':
    # 目標の平均値
    target_mean = 0.335
    # 平均値が0.335になる正規分布の乱数を生成
    random_numbers = generate_normal_with_target_mean(target_mean)

    # 生成した乱数の平均値を確認（確認用）
    print("生成した乱数の平均値:", np.mean(random_numbers))