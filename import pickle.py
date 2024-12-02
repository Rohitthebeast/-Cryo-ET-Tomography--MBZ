import pickle

def load_subset(file_path, subset_size):
    try:
        with open(file_path, 'rb') as f:  # Ensure binary mode
            data = pickle.load(f)  # Load the pickle file

        if isinstance(data, list) or isinstance(data, tuple):
            return data[:subset_size]
        elif isinstance(data, dict):
            return {k: data[k] for k in list(data.keys())[:subset_size]}
        else:
            print("Data type not supported for subset extraction")
            return None
    except UnicodeDecodeError as e:
        print(f"UnicodeDecodeError: {e}")
        return None
    except EOFError as e:
        print(f"EOFError: {e}")
        return None
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Path to your pickle file
file_path = 'C:/Users/rohit/OneDrive/Desktop/Research MBZUAI/2000_30_01.pickle'
subset_size = 1000  # Adjust the subset size as needed

subset_data = load_subset(file_path, subset_size)

if subset_data is not None:
    print(f"Loaded subset of size: {subset_size}")
    # Proceed with your data processing or model training using subset_data
else:
    print("Failed to load subset of data")
