import time
from colorama import Fore, Style
from ..config import DURATION
from .file_handlers import save_successful_request, convert_to_english_chars

def check_and_send_request(cl, username, full_name, names):
    try:
        username_lower = username.lower()
        username_check = convert_to_english_chars(username_lower)
        for name in names:
            if name in username_check:
                try:
                    user_id = cl.user_id_from_username(username)
                    cl.user_follow(user_id)
                    print(f"{Fore.GREEN}✅ İstek gönderildi! (Kullanıcı adında '{name}' bulundu){Style.RESET_ALL}")
                    save_successful_request(username, full_name, "Kullanıcı adında isim bulundu")
                    time.sleep(DURATION) 
                    return True
                except Exception as e:
                    print(f"{Fore.RED}⛔ İstek gönderilirken hata: {str(e)}{Style.RESET_ALL}")
                    return False
        
        full_name_lower = full_name.lower() if full_name else ""
        for name in names:
            if name in full_name_lower:
                try:
                    user_id = cl.user_id_from_username(username)
                    cl.user_follow(user_id)
                    print(f"{Fore.GREEN}✅ İstek gönderildi! (İsminde '{name}' bulundu){Style.RESET_ALL}")
                    save_successful_request(username, full_name, "Profil isminde isim bulundu")
                    time.sleep(DURATION)
                    return True
                except Exception as e:
                    print(f"{Fore.RED}İstek gönderilirken hata: {str(e)}{Style.RESET_ALL}")
                    return False
                    
        return False
    except Exception as e:
        print(f"{Fore.RED}İsim kontrolü sırasında hata: {str(e)}{Style.RESET_ALL}")
        return False
