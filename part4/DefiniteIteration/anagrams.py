def anagrams(text1:str, text2:str):
    if(sorted(text1) == sorted(text2)):
        return True
    else:
        return False

if __name__ == "__main__":
    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) # False