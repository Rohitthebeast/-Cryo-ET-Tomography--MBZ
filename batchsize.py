import pickle

def load_pickle_in_batches(file_path, batch_size):
    with open(file_path, 'rb') as f:
        try:
            while True:
                batch_data = []
                for _ in range(batch_size):
                    try:
                        batch_data.append(pickle.load(f))
                    except EOFError:
                        break
                if not batch_data:
                    break
                yield batch_data
        except Exception as e:
            print(f"An error occurred while loading batches: {e}")

# Example usage
if __name__ == "__main__":
    file_path = 'C:/Users/rohit/OneDrive/Desktop/Research MBZUAI/2000_30_01.pickle'
    batch_size = 32  # Adjust the batch size as needed

    for batch in load_pickle_in_batches(file_path, batch_size):
        print(f"Loaded batch of size: {len(batch)}")