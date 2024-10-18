import os
import socket
from collections import Counter
import re

def word_count(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
    words = re.findall(r"\b\w+\b", text.lower())
    return words

def handle_contractions(text):
    contractions = {
        "i'm": "i am", "can't": "cannot", "don't": "do not", "won't": "will not", "you're": "you are"
        # Add more as needed
    }
    for contraction, expanded in contractions.items():
        text = text.replace(contraction, expanded)
    return text

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

if __name__ == "__main__":
    # File paths
    file1 = "/home/data/IF.txt"
    file2 = "/home/data/AlwaysRememberUsThisWay.txt"
    
    # Word count for IF.txt
    words_file1 = word_count(file1)
    count_file1 = len(words_file1)
    counter_file1 = Counter(words_file1)
    top3_file1 = counter_file1.most_common(3)

    # Word count for AlwaysRememberUsThisWay.txt (handling contractions)
    with open(file2, 'r') as f:
        text_file2 = f.read().lower()
    text_file2 = handle_contractions(text_file2)
    words_file2 = re.findall(r"\b\w+\b", text_file2)
    count_file2 = len(words_file2)
    counter_file2 = Counter(words_file2)
    top3_file2 = counter_file2.most_common(3)

    # Grand total
    grand_total = count_file1 + count_file2

    # Get IP address
    ip_address = get_ip_address()

    # Write results to result.txt
    with open("/home/data/output/result.txt", 'w') as f:
        f.write(f"IF.txt word count: {count_file1}\n")
        f.write(f"Top 3 most frequent words in IF.txt: {top3_file1}\n")
        f.write(f"AlwaysRememberUsThisWay.txt word count: {count_file2}\n")
        f.write(f"Top 3 most frequent words in AlwaysRememberUsThisWay.txt: {top3_file2}\n")
        f.write(f"Grand total word count: {grand_total}\n")
        f.write(f"Container IP address: {ip_address}\n")

    # Print the contents of result.txt to the console
    with open("/home/data/output/result.txt", 'r') as f:
        print(f.read())
