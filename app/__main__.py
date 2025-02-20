from colorama import init
from .core.instagram_client import instagram_login, get_followers
from .config import CHECK_USERNAME

def main():
    init()  # Colorma yüklee
    client = instagram_login()
    if client:
        get_followers(client, CHECK_USERNAME)

if __name__ == "__main__":
    main()
