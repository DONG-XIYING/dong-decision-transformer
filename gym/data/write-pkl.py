import pickle

# データセットをロード
with open('1-ant-expert-v2.pkl', 'rb') as f:
    data = pickle.load(f)

# アクション0の値を0に設定してアクチュエータの故障を模擬
for trajectory in data:
    trajectory['actions'][:, 7] = 0

# 変更されたデータセットを保存
with open('ant-expert-v2.pkl', 'wb') as f:
    pickle.dump(data, f)
