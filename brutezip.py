import zipfile
from tqdm import tqdm

info = '''
    =====================================================
   | Created by Kawojue Raheem Olumuyiwa                 |
   | Facebook: Kawojue Raheem Olumuyiwa (CoderHacker)    |
   | Whatsapp: +2349059137330                            |
   | Gmail: kawojue08@gmail.com                          |
   | YouTube Channel: Bright Hacks (Subscribe)           |
    ===================================================
    '''

print(info)

wordlist = input("Wordlist: ")
zip_F = input("Enter Zip File Path: ")

zip_F = zipfile.ZipFile(zip_F)
words = len(list(open(wordlist, "rb")))

print("Total password to Test: " + str(words))

with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=words, unit="word"):
        try:
            zip_F.extractall(pwd=word.strip())
            print(word)
        except:
            continue
        else:
            print("Password Found:", word.decode().strip())
            exit(0)
print("Password not found, try another wordlist.")

wordlist.close()
