import re
import unicodedata

def get_choseong(text):
    """한글 문자열에서 초성만 추출하는 함수"""
    CHO = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
    result = ""
    for char in text:
        if '가' <= char <= '힣':
            char_code = ord(char) - ord('가')
            choseong_index = char_code // 588
            result += CHO[choseong_index]
        else:
            result += char
    return result

def search_by_choseong(filename, query):
    """텍스트 파일에서 초성 검색을 수행하는 함수 (입력한 초성과 같은 글자 수의 단어만 검색)"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        query_choseong = get_choseong(query)
        query_length = len(query)
        results = []
        
        for line in lines:
            words = line.strip().split()
            for word in words:
                if len(word) == query_length and get_choseong(word) == query_choseong:
                    results.append(word)
        
        return results
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
        return []

if __name__ == "__main__":
    filename = "words.txt"  # 검색할 텍스트 파일
    while True:
        query = input("검색할 초성을 입력하세요 (종료하려면 'exit' 입력): ")
        if query.lower() == 'exit':
            break
        results = search_by_choseong(filename, query)
        
        if results:
            print("검색 결과:", results)
        else:
            print("검색된 단어가 없습니다.")
