import zipfile

def main():
    try:
        zip_file_path = 'HomeworkW8.zip'
        zip_file = zipfile.ZipFile(zip_file_path)
    except Exception as e:
        print(f"[-] Error opening ZIP file: {e}")
        return

    try:
        with open('dictionary.txt', 'r', encoding='ISO-8859-1') as dictFile:
            for line in dictFile.readlines():
                password = line.strip()
                print(f"[*] Attempting to crack ZIP file using password: {password}")
                if testPass(zip_file, password):
                    break
    except Exception as e:
        print(f"[-] Error reading dictionary.txt: {e}")

def testPass(zip_file, password):
    try:
        zip_file.extractall(pwd=bytes(password, 'utf-8'))
        print(f"[+] Found Password for ZIP file: {password}\n")
        return True
    except:
        print(f"[-] Failed with password: {password}")
        return False

if __name__ == "__main__":
    main()

