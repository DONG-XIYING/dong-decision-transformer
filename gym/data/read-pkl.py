import pickle

pickle_file_path = 'hopper-medium-v2.pkl'

try:
    with open(pickle_file_path, 'rb') as f:
        data = pickle.load(f)
        print(data)
except Exception as e:
    print(f"Error loading pickle file: {e}")
