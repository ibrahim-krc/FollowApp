import time
from colorama import Fore, Style
import unidecode

def convert_to_english_chars(text):
    """Türkçe karakterleri ing karaktere çevirmek için func"""
    return unidecode.unidecode(text.lower())

def get_processed_names():
    try:
        with open('isimler.txt', 'r', encoding='utf-8') as f:
            names = [line.strip() for line in f.readlines() if line.strip()]
        
        processed_names = []
        for name in names:
            name_lower = name.lower()
            name_english = convert_to_english_chars(name_lower)
            if name_english != name_lower:  
                processed_names.append(name_lower)  
                processed_names.append(name_english)  
            else:
                processed_names.append(name_lower)
        return processed_names
    except Exception as e:
        print(f"{Fore.RED}İsimler dosyası okunurken hata: {str(e)}{Style.RESET_ALL}")
        return []

def save_successful_request(username, full_name, request_type):
    try:
        with open('basarili_istekler.txt', 'a', encoding='utf-8') as f:
            f.write(f"Kullanıcı Adı: {username}\n")
            f.write(f"İsim: {full_name}\n")
            f.write(f"İstek Türü: {request_type}\n")
            f.write(f"Tarih: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("-" * 50 + "\n")
    except Exception as e:
        print(f"{Fore.RED}Başarılı istek kaydedilirken hata: {str(e)}{Style.RESET_ALL}")
