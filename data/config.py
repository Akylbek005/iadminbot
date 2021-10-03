from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = '1754811598:AAHMz-bDYtfmo1T1tyZqlrqTS3KmtZA8N1Y'  # Забираем значение типа str
ADMINS = ['874928357'] # Тут у нас будет список из админов
IP = "localhost"  # Тоже str, но для айпи адреса хоста
CHANNEL_ID = -1001598596296
IS_POSTING_REQUESTEQ = False
