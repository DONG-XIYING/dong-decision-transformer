import pickle
import numpy as np
import matplotlib.pyplot as plt

pickle_file_path = 'walker2d-expert-v2.pkl'

# データをロード
try:
    with open(pickle_file_path, 'rb') as f:
        data = pickle.load(f)
        print("Data loaded successfully.")
except Exception as e:
    print(f"Error loading pickle file: {e}")
    data = None

# データが正しくロードされた場合、分析を行う
if data:
    # データのサンプルを表示して構造を確認
    print("Sample data:", data[0] if isinstance(data, list) else list(data.items())[:5])

    # 例として、報酬のヒストグラムを作成
    if isinstance(data, list):
        # データがリスト形式の場合
        rewards = [d['rewards'] for d in data if 'rewards' in d]
    elif isinstance(data, dict):
        # データが辞書形式の場合
        rewards = data.get('rewards', [])

    if rewards:
        # 報酬がリストのリスト形式の場合、一つのリストに統合
        if isinstance(rewards[0], list) or isinstance(rewards[0], np.ndarray):
            rewards = np.concatenate(rewards)
# 自動でビンの数を決定する
        bins = np.histogram_bin_edges(rewards, bins='auto')
        
        # ヒストグラムを作成
        plt.hist(rewards, bins=bins,color='lightblue', alpha=0.6) #edgecolor='black', 

        # 追加のデザイン
        #plt.axvline(np.mean(rewards), color='red', linewidth=2)  # 平均値に赤い線を追加  
        plt.title('Rewards of Walker2D-Expert', fontsize=14)
        plt.xlabel('Reward', fontsize=14)
        plt.ylabel('Frequency', fontsize=14)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.show()
    else:
        print("No rewards data found in the loaded data.")
else:
    print("No data to analyze.")
