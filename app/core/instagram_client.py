import os
import time
from colorama import Fore, Style
from instagrapi import Client
from ..config import (
    INSTAGRAM_USERNAME,
    INSTAGRAM_PASSWORD,
    SETTINGS_PATH,
    SCRAPE_COUNT
)
from ..utils.file_handlers import get_processed_names
from ..utils.instagram_utils import check_and_send_request

def get_followers(cl, username):
    try:
        names = get_processed_names()
        if not names:
            print(f"{Fore.RED}İsimler listesi boş veya yüklenemedi!{Style.RESET_ALL}")
            return
            
        print(f"\n{Fore.CYAN}Takipçiler alınıyor, lütfen bekleyin...{Style.RESET_ALL}")
        
        user_id = cl.user_id_from_username(username)
        followers = cl.user_followers_v1(user_id, amount=SCRAPE_COUNT)
        total_followers = len(followers)
        
        if not followers:
            print(f"{Fore.YELLOW}Takipçi bulunamadı veya hesap gizli olabilir.{Style.RESET_ALL}")
            return
            
        print(f"\n{Fore.CYAN}@{username} kullanıcısının takipçileri:{Style.RESET_ALL}\n")

        for index, follower in enumerate(followers, 1):
            try:
                print(f"\r{Fore.CYAN}İşlenen takipçi: {index}/{total_followers}{Style.RESET_ALL}", end="")
                print(f"\n{Fore.GREEN}Kullanıcı Adı:{Style.RESET_ALL} @{follower.username}")
                print(f"{Fore.YELLOW}İsim:{Style.RESET_ALL} {follower.full_name}")
                
                if check_and_send_request(cl, follower.username, follower.full_name, names):
                    print(f"{Fore.BLUE}------------------------{Style.RESET_ALL}")
                else:
                    print(f"{Fore.BLUE}------------------------{Style.RESET_ALL}")
                
            except Exception as e:
                print(f"{Fore.RED}Takipçi kontrolü sırasında hata: {str(e)}{Style.RESET_ALL}")
                print(f"{Fore.BLUE}------------------------{Style.RESET_ALL}")
                continue
            
    except Exception as e:
        print(f"{Fore.RED}Takipçiler alınırken hata: {str(e)}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Not: Hesap gizli olabilir veya erişim kısıtlaması olabilir.{Style.RESET_ALL}")

def instagram_login():
    cl = Client()

    try:
        if os.path.exists(SETTINGS_PATH):
            cl.load_settings(SETTINGS_PATH)
            print(f"{Fore.CYAN}Önceki oturum verileri yükleniyor...{Style.RESET_ALL}")
        
        cl.set_locale('tr_TR')
        cl.set_country('TR')
        cl.set_timezone_offset(3 * 60 * 60)
        
        login = cl.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
        
        if login:
            cl.dump_settings(SETTINGS_PATH)
            print(f"{Fore.GREEN}Başarıyla giriş yapıldı!{Style.RESET_ALL}")
            print(f"\n{Fore.CYAN}Hoş geldiniz!{Style.RESET_ALL}")
            time.sleep(2)
            return cl
        
        return None
    
    except Exception as e:
        print(f"{Fore.RED}Giriş yapılırken hata: {str(e)}{Style.RESET_ALL}")
        return None
