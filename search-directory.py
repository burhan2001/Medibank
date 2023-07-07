import os
import collections


def search_directory(directory):
    word_count = collections.defaultdict(int)

    # Recursive function to search through directory and subdirectories
    def search_files(path):
        for root, _, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                process_file(file_path)

    # Process individual file
    def process_file(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    word_count[word.lower()] += 1

    search_files(directory)

    # Filter and sort results
    filtered_words = [(word, count) for word, count in word_count.items() if count > 2]
    filtered_words.sort(key=lambda x: x[1], reverse=True)

    # Print the results
    for word, count in filtered_words:
        print(f'{word}: {count}')


# Usage
search_directory('/path/to/directory')
