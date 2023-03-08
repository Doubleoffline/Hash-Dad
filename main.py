import hashlib

def print_header():
    print("""
 __    __       ___           _______. __    __      _______       ___       _______  
|  |  |  |     /   \         /       ||  |  |  |    |       \     /   \     |       \ 
|  |__|  |    /  ^  \       |   (----`|  |__|  |    |  .--.  |   /  ^  \    |  .--.  |
|   __   |   /  /_\  \       \   \    |   __   |    |  |  |  |  /  /_\  \   |  |  |  |
|  |  |  |  /  _____  \  .----)   |   |  |  |  |    |  '--'  | /  _____  \  |  '--'  |
|__|  |__| /__/     \__\ |_______/    |__|  |__|    |_______/ /__/     \__\ |_______/ 
                                                                                      
                                                    
    Made by Double
    """)

def get_hash_type():
    print("[*] Please enter the hash type:")
    print("    [1] MD5")
    print("    [2] SHA1")
    print("    [3] SHA256")
    print("    [4] SHA512")
    hash_type = input("Hash type [1-4]: ")
    if hash_type not in ["1", "2", "3", "4"]:
        print("[-] Invalid hash type specified.")
        exit()
    return hash_type

def load_wordlist(wordlist_file):
    try:
        with open(wordlist_file, "r", encoding="utf-8", errors="ignore") as f:
            wordlist = f.read().splitlines()
            print("[+] Loaded wordlist with %d entries." % len(wordlist))
            return wordlist
    except FileNotFoundError:
        print("[-] Wordlist file not found.")
        exit()

def crack_hash(hash_type, hash_input, wordlist):
    if hash_type == "1":
        hash_func = hashlib.md5
        print("[+] Cracking with MD5")
    elif hash_type == "2":
        hash_func = hashlib.sha1
        print("[+] Cracking with SHA1")
    elif hash_type == "3":
        hash_func = hashlib.sha256
        print("[+] Cracking with SHA256")
    elif hash_type == "4":
        hash_func = hashlib.sha512
        print("[+] Cracking with SHA512")

    for word in wordlist:
        hashed_word = hash_func(word.encode()).hexdigest()
        if hashed_word == hash_input:
            print("[+] Hash cracked! The password is: %s" % word)
            return
    print("[-] Hash not found in wordlist.")

def main():
    print_header()

    hash_type = get_hash_type()
    hash_input = input("Enter the hash to crack: ")
    wordlist_file = input("Enter the wordlist file name: ")
    wordlist = load_wordlist(wordlist_file)

    crack_hash(hash_type, hash_input, wordlist)

if __name__ == "__main__":
    main()
