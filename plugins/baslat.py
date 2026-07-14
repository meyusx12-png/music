from pyrogram import Client, filters
from config import BOT_NAME

@Client.on_message(filters.command(["başlat", "start"]))
async def baslat(_, message):
    await message.reply_text(
        f"""🎵 **{BOT_NAME}**

Merhaba! Ben Telegram sesli sohbet müzik botuyum.

🎶 **Komutlar**
/çal <şarkı adı>
/duraklat
/devam
/geç
/durdur
/liste
/şimdi
/yardım

🎧 Beni bir gruba ekleyin ve sesli sohbet başlatın."""
    )

@Client.on_message(filters.command(["yardım", "help"]))
async def yardim(_, message):
    await message.reply_text(
        """📖 **Yardım Menüsü**

▶️ /çal <şarkı adı> - Müzik çalar
⏸ /duraklat - Müziği duraklatır
▶️ /devam - Devam ettirir
⏭ /geç - Sonraki şarkıya geçer
⏹ /durdur - Müziği durdurur
📜 /liste - Kuyruğu gösterir
🎵 /şimdi - Çalan şarkıyı gösterir
🚪 /çık - Sesli sohbetten ayrılır"""
    )