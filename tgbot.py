#!/usr/bin/env python3



# ────────────────────────────────────────────



#   #𝗠ᴀᴅ𝗘 #𝗕ʏ 𝐁ᴇ4sᴛ 



# ────────────────────────────────────────────



import ssl



ssl._create_default_https_context = ssl._create_unverified_context







import asyncio, functools, gc, json, logging, os, platform as _plt, random, requests, time



from typing import Dict, List, Optional, Set, Tuple







if _plt.system() == "Windows":



    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())



else:



    try:



        import uvloop as _uvloop; _uvloop.install()



        print("  uvloop active")



    except ImportError:



        pass







from telegram import Bot, ChatMemberAdministrator, ReactionTypeEmoji, Update



from telegram.constants import ParseMode



from telegram.error import RetryAfter, TelegramError



from telegram.ext import (



    Application, ChatMemberHandler,



    CommandHandler, ContextTypes, MessageHandler, PrefixHandler, filters,



)







TOKENS: List[str] = [



"9057982927:AAGtH7-GqCe7gOtTSBzwyYYFWDo9KXSxEfo", #1
    "9081313687:AAHoLZW_iowwl5DFl7CoEixe4PxsePL0jQo", #2

    "9238300345:AAHiJJWlLYIscbvPbHZtendkdyNM-GGzQ9c", #3
    "9201478484:AAF9pPEmSF4y6cuuDHy4VOjtY9jlykaGgiE", #4
    "9290487096:AAFI96A5MWOSRc8qwzszpskLsFsntKaK4U4", #5 
    
    "8631986531:AAEuG5j-EDoQKfMgzgAQhMl9_FUyvH_xIVg", #6
    
    "8216445027:AAF8VMNqPdloKo7QKWslu5g539vQ861X0Jo", #7
    
    "8902401024:AAFcXFh9m0u82-bDgI5K-ZqWZakEpk_bCU8", #8
    
    "8883519465:AAENRsE4Ol8QvpEla9M8gEQX2sPpehttPPc", #9
    
    "9005040574:AAGhB7ooggQARQImNGPOvV5tguKI1-nB9qg", #6
    
    "9033182254:AAEoYvaX8acc8ehyfYbDOrrQtNvyQKzedKA", #7
    
    "9153753582:AAH9jPx0w823AwGtTINkWzwxLyD8i3CiFY8", #8



]


YOUR_ID = 9271821991  # <--- YAHA APNI NUMERIC ID DALO (E.g. 8160881443)

OWNERS:     frozenset = frozenset({str(YOUR_ID), YOUR_ID})
SUDO_PATH:  str       = "sudo_data.json"
NEXUS_PATH: str       = "nexus_data.json"








_Λ_PULSE: float = 0.05



_Θ_HOUND: float = 60.0







_ξ_GLYPH = "nc"



_ν_GLYPH = "spam"



_μ_GLYPH = "swipe"







_Δ_delay: List[float] = [0.0]







_Φ_mpfp: List[Optional[str]] = [None]







_P_NC: List[str] = [



"«|-😜-|»", "«|-😉-|»", "«|-😎-|»", "«|-🤩-|»", "«|-🥳-|»",



"«|-😏-|»", "«|-😁-|»", "«|-😆-|»", "«|-🤣-|»", "«|-😂-|»",



"«|-😊-|»", "«|-😍-|»", "«|-😘-|»", "«|-😗-|»", "«|-😙-|»",



"«|-😚-|»", "«|-🤗-|»", "«|-🙂-|»", "«|-🙃-|»", "«|-😋-|»",



"«|-🤪-|»", "«|-😝-|»", "«|-😛-|»", "«|-🤭-|»", "«|-🫢-|»",



"«|-🫣-|»", "«|-🤫-|»", "«|-🤔-|»", "«|-🫡-|»", "«|-😇-|»",



"«|-🥰-|»", "«|-😌-|»", "«|-🤠-|»", "«|-🥸-|»", "«|-😺-|»",



"«|-😸-|»", "«|-😹-|»", "«|-😻-|»", "«|-😼-|»", "«|-🙈-|»",



"«|-🙉-|»", "«|-🙊-|»", "«|-🐱-|»", "«|-🐶-|»", "«|-🦊-|»",



"«|-🐼-|»", "«|-🐨-|»", "«|-🐯-|»", "«|-🦁-|»", "«|-🐸-|»",



"«|-🐵-|»", "«|-🦄-|»", "«|-🐲-|»", "«|-🐉-|»", "«|-🦋-|»",



"«|-🐝-|»", "«|-🐞-|»", "«|-🕷️-|»", "«|-🦂-|»", "«|-🐢-|»",



"«|-🐬-|»", "«|-🦈-|»", "«|-🐙-|»", "«|-🦀-|»", "«|-🐠-|»",



"«|-🔥-|»", "«|-⚡-|»", "«|-💥-|»", "«|-✨-|»", "«|-🌟-|»",



"«|-⭐-|»", "«|-🌙-|»", "«|-☀️-|»", "«|-🌈-|»", "«|-❄️-|»",



"«|-☁️-|»", "«|-🌊-|»", "«|-🌪️-|»", "«|-🌋-|»", "«|-🪐-|»",



"«|-🌍-|»", "«|-🌎-|»", "«|-🌏-|»", "«|-☄️-|»", "«|-💫-|»",



"«|-🍀-|»", "«|-🌹-|»", "«|-🌺-|»", "«|-🌸-|»", "«|-🌻-|»",



"«|-🌼-|»", "«|-🍁-|»", "«|-🍂-|»", "«|-🌴-|»", "«|-🌵-|»",



"«|-🎉-|»", "«|-🎊-|»", "«|-🎈-|»", "«|-🎁-|»", "«|-🎀-|»",



"«|-🏆-|»", "«|-🥇-|»", "«|-🥈-|»", "«|-🥉-|»", "«|-👑-|»",



"«|-💎-|»", "«|-🛡️-|»", "«|-⚔️-|»", "«|-🏹-|»", "«|-🔱-|»",



"«|-❤️-|»", "«|-🧡-|»", "«|-💛-|»", "«|-💚-|»", "«|-💙-|»",



"«|-💜-|»", "«|-🖤-|»", "«|-🤍-|»", "«|-🤎-|»", "«|-💕-|»",



"«|-💞-|»", "«|-💓-|»", "«|-💗-|»", "«|-💖-|»", "«|-💘-|»",



"«|-🚀-|»", "«|-🛸-|»", "«|-✈️-|»", "«|-🚁-|»", "«|-⛵-|»",



"«|-🚗-|»", "«|-🏍️-|»", "«|-🚓-|»", "«|-🚒-|»", "«|-🚑-|»",



"«|-⌚-|»", "«|-📱-|»", "«|-💻-|»", "«|-🖥️-|»", "«|-⌨️-|»",



"«|-🖱️-|»", "«|-🎮-|»", "«|-🕹️-|»", "«|-📷-|»", "«|-🎥-|»",



"«|-🎵-|»", "«|-🎶-|»", "«|-🎸-|»", "«|-🎹-|»", "«|-🥁-|»",



"«|-🎺-|»", "«|-🎻-|»", "«|-🎷-|»", "«|-🎤-|»", "«|-🎧-|»",



"«|-🍕-|»", "«|-🍔-|»", "«|-🍟-|»", "«|-🌭-|»", "«|-🌮-|»",



"«|-🌯-|»", "«|-🍗-|»", "«|-🍖-|»", "«|-🍜-|»", "«|-🍣-|»",



"«|-🍩-|»", "«|-🍪-|»", "«|-🎂-|»", "«|-🍰-|»", "«|-🧁-|»",



"«|-☕-|»", "«|-🍵-|»", "«|-🥤-|»", "«|-🧃-|»", "«|-🍫-|»",



"«|-💰-|»", "«|-💵-|»", "«|-💸-|»", "«|-🏦-|»", "«|-📈-|»",



"«|-📉-|»", "«|-📝-|»", "«|-📚-|»", "«|-📖-|»", "«|-🔮-|»",



"«|-🎯-|»", "«|-🎲-|»", "«|-♠️-|»", "«|-♥️-|»", "«|-♦️-|»",



"«|-♣️-|»", "«|-🃏-|»", "«|-🎰-|»", "«|-🎳-|»", "«|-🏀-|»"



]



_P_NCCHUD: List[str] = [



"😭","😱","🥱","😥","😤","😡","🤬","😳","🥵","🥶",



"😨","😰","😓","🤗","🤔","🤭","🤫","🤥","😶","😐",



"😑","😬","🙄","😯","😦","😧","😮","😲","😴","🤤",



"😪","😵","🤐","🥴","🤢","🤮","🤧","😷","🤒","🤕",



"🤑","🤠","😈","👿","💀","☠️","👻","👽","🤖","💩",



"🔥","✨","🌟","💫","⭐","⚡","💥","💨","💦","💤",



"💢","💯","💬","❤️","🧡","💛","💚","💙","💜","🖤",



"🤍","🤎","💔","❣️","💕","💞","💓","💗","💖","💘",



"💝","💟","💌","💋","👀","🧠","🦷","🦴","👶","👦",



"🐶","🐱","🐭","🐹","🐰","🦊","🐻","🐼","🐨","🐯",



"🦁","🐮","🐷","🐸","🐵","🙈","🙉","🙊","🐒","🐔",



"🐧","🐦","🐤","🐣","🐥","🦆","🦅","🦉","🦇","🐺",



"🐗","🐴","🦄","🐝","🐛","🦋","🐌","🐞","🐜","🪲",



"🌍","🌎","🌏","🌐","🪐","🌙","🌑","🌒","🌓","🌔",



"🌕","🌖","🌗","🌘","🌚","🌝","🌞","☀️","⛅","☁️",



"🌧️","⛈️","🌩️","🌨️","❄️","☃️","🌬️","🌪️","🌫️","🌈",



"🍎","🍏","🍊","🍋","🍌","🍉","🍇","🍓","🍒","🍑",



"🥭","🍍","🥥","🥝","🍅","🍆","🥑","🥦","🥬","🥒",



"🌶️","🌽","🥕","🧄","🧅","🥔","🍠","🥐","🍞","🧀",



"⚽","🏀","🏈","⚾","🎾","🏐","🏉","🥏","🎱","🏓",



"🏸","🥊","🥋","🎽","🛹","🛼","🛷","⛸️","🥌","🎿",



"🏂","🪂","🏋️","🤼","🤸","⛹️","🤺","🤾","🏌️","🏇",



"🚗","🚕","🚙","🚌","🚎","🏎️","🚓","🚑","🚒","🚐",



"🚚","🚛","🚜","🛻","🚲","🛴","🛵","🏍️","✈️","🚀",



"🛸","🚁","🚂","🚆","🚇","🚢","⛵","🚤","⚓","🚧"



]



_P_NCBE4ST: List[str] = [



"<💐>",



"<🌸>",



"<💮>",



"<🪷>",



"<🏵️>",



"<🌹>",



"<🥀>",



"<🌺>",



"<🌻>",



"<🌼>",



"<🌷>",



"<🪻>",



"<⚜️>",



"<🍀>",



"<☘️>",



"<🌿>",



"<🍃>",



"<🍂>",



"<🍁>",



"<🌱>",



"<🌾>",



"<🌵>",



"<🌲>",



"<🌳>",



"<🎋>",



"<🎍>",



"<🪴>"



]



_P_SEXUAL: List[str] = [



"Rᴀɴᴅ ₊˚₊˚.⋆⋆",



"Cᴜᴅ ᴋᴇsᴇ Gᴀʏᴀ ₊˚₊˚.⋆⋆",



"Bʜᴀɢ Mᴀᴛ ₊˚₊˚.⋆⋆",



"Gᴜʟᴀᴍ Bᴀɴ Pɪʟʟᴇ ₊˚₊˚.⋆⋆",



"Iᴅʜᴇʀ Aᴀ Tᴇʀɪ Bᴇʜɴ Cᴏᴅᴜ ₊˚₊˚.⋆⋆",



"Tᴇʀɪ Mᴀ Kᴏ Qᴜᴛᴜʙ Mɪɴᴀʀ Lᴇ Jᴀᴜ ₊˚₊˚.⋆⋆",



"Dᴀғᴀɴ Mᴀᴛ Hᴏ Gᴀʀᴇᴇʙ Lᴀʀᴋᴇ ₊˚₊˚.⋆⋆",



"Jᴀᴅᴏᴏ Sᴇ Cʜᴜᴅɪ Tᴇʀɪ Mᴏᴍ ₊˚₊˚.⋆⋆",



"Tᴇʀɪ Mᴀ Kᴀ Bʜᴏsᴅᴀ Mᴀʀᴜ ₊˚₊˚.⋆⋆",



"Tᴇʀɪ Mᴏᴍ ᴄʜᴜᴅᴀɪ Aʀᴄ ᴄʜᴀʟᴜ ʜᴀɪ ₊˚₊˚.⋆⋆",



"Wᴡᴇ Mᴇ Cʜᴜᴅɪ Tᴇʀʏ Mᴏᴍ ₊˚₊˚.⋆⋆",



"Tᴇʀɪ Mᴀ Lᴇsʙɪᴀɴ Cʜᴏᴅ ₊˚₊˚.⋆⋆",



"Pʀᴇɢᴀɴᴀɴᴛ Kʀᴜ Tᴇʀʏ Mᴏᴍ Kᴏ ₊˚₊˚.⋆⋆",



"Dᴇᴋʜ Aᴘɴɪ Mᴀ ᴋɪ Cʜᴜᴅᴀɪ ₊˚₊˚.⋆⋆",



"Kᴀʟᴘᴀɴɪᴋ Yᴜɢ ᴋɪ Rᴀɴᴅɪ ᴛᴇʀɪ Mᴀ ₊˚₊˚.⋆⋆",



"Tᴇʀɪ Mᴀ Dɪᴀɴᴏsᴏᴜʀ Aʀᴄ ᴍᴇ Cʜᴜᴅ Gʏɪ ₊˚₊˚.⋆⋆",



"Dᴏʀᴀᴇᴍᴏɴ Aʀʜᴀ Hᴏɢᴀ Tᴇʀɪ Mᴀ Cʜᴏᴅɴᴇ ₊˚₊˚.⋆⋆",



"Esᴇ ɴʜɪ Bᴏʟᴛᴇ Wʀɴᴀ Tᴇʀɪ Mᴀ Cʜᴜᴅ Jᴀʏɢɪ ₊˚₊˚.⋆⋆",



"Tᴇʀɪ Mᴀ Kᴏ Osᴄᴀʀ Mɪʟɴᴀ Cʜᴀʜɪʏᴇ Cʜᴜᴅɴᴇ Kᴀ ₊˚₊˚.⋆⋆",



"𝐁ᴇ4sᴛ  Bᴀᴘ Bᴏʟ Mᴅᴄ ₊˚₊˚.⋆⋆",



"Hᴀᴡʙᴀᴢ Bᴀɴᴇɢᴀ Tᴍʀ ₊˚.⋆",



"Tᴇʀɪ Bᴇʜᴇɴ Kᴜᴛᴛɪʏᴀ ₊˚.⋆"



"Tᴇʀɪ Mᴀ Pᴏᴋᴇᴍᴏɴ ₊˚.⋆",



"Kᴏɴsᴇ Pᴏsɪᴛɪᴏɴ Mᴇ Cᴏᴅᴜ Tᴇʀɪ Mᴀ Kᴏ ₊˚.⋆",



"BᴀᴛʜRᴏᴏᴍ Mᴇ Cʜᴜᴅᴇɢᴀ Oʀ Bᴇᴅʀᴏᴏᴍ ₊˚.⋆"



"Cʜᴜᴅᴀ Tᴇʀɪ Mᴏᴍ ₊˚.⋆",



"Tᴇʀɪ Mᴀ Kᴀ Bᴀʟᴀᴛᴀᴋʀ Hᴏɢᴀʏᴀ Bʜᴀɢᴏᴏ ₊˚.⋆"



]



_P_CHUD_SWIPE: List[str] = [



"{name} 𝗟ꪊꪀ𝗗 𝗖ʜꪊs 𝗦ꪶꪖꪜꫀ",



"{name} तेरी 𝘔𝘰𝘮 𝘞𝘰𝘳𝘭𝘥 𝘊𝘭𝘢𝘴𝘴 रण्डी😂🔥",



"{name} सही 𝘊𝘩𝘶𝘥𝘪 तेरी Mom😠😝😠",



"{name} 𝘛𝘦𝘳𝘪 मां को अल्लाह 𝘊𝘩𝘰𝘥𝘦🖕🎀🐊",



"{name} 𝘒𝘺𝘢 रे 𝘚𝘮𝘪𝘭𝘦𝘺 जैसा रन्डी बनेगा🤴👑",



"{name} तेरी 𝘔𝘢 𝘊𝘩𝘰𝘥𝘶 क्या RandSon🥰🔥🥀",



"{name} तेरी माँ की छूट में गुलाब जामुन 🚀💢🍕",



" {name} अपनी मां 𝘬𝘪 𝘊𝘩𝘶𝘥𝘢𝘪 का आनंद ले !!"



]



_T_TSWIPE: List[str] = [



"<🩷>⋆｡°✩Tᴇʀɪ Mᴀ Oɴʟʏ 𝐁ᴇ4sᴛ  Cʜᴏᴅᴇɢᴀ¿?✩°｡⋆<🩷>"



"<❤️>⋆｡°✩Tᴇʀɪ Mᴀ Kᴏ Pʜᴀsɪ Pᴇ Cʜᴀᴅᴅʜᴀ Dɪʏᴀ ʜᴜ✩°｡⋆<❤️>"



"<🧡>⋆｡°✩Tᴇʀɪ Mᴀ Cʜᴜᴅ Gʏɪ Tᴏᴋᴏ Tᴀʟɪ✩°｡⋆<🧡>"



"<💛>⋆｡°✩Cʜᴜᴅᴋᴇ Mᴀʀɪ Kᴇsɪ Tᴇʀɪ Mᴏᴍ✩°｡⋆<💛>"



"<💚>⋆｡°✩Tᴇʀɪ Bᴇʜᴇɴ Kɪ Cʜᴜᴛ Mᴇ Hᴀᴀᴛʜ Dᴀʟᴅᴜɴɢᴀ RᴀɴᴅSᴏɴ✩°｡⋆<💚>"



"<🩵>⋆｡°✩Tᴇʀɪ Tᴀᴋʟɪ Mᴀ Kᴇ Sᴀʀ Pʀ Pᴇʀ Rᴋʜ Kʀ Bᴏʟᴜɴɢᴀ Tᴇʀɪ Mᴀ Rᴀɴᴅɪ✩°｡⋆<🩵>"



"<💙>⋆｡°✩Tᴇʀɪ Mᴀ Kɪ Cʜᴜᴅᴀɪ Mᴀsᴛ Eɴᴊᴏʏ Kʀ Rʜᴀ✩°｡⋆<💙>"



"<💜>⋆｡°✩Tᴇʀɪ Mᴀ OɴʟʏFᴀɴs Pᴇ Nᴜᴅᴇ Dᴀʟ Rʜɪ Jᴀ Kᴇ Dᴇᴋʜ✩°｡⋆<💜>"



"<🖤>⋆｡°✩Kᴀᴍᴢᴏʀ Eʏ Tᴜ Gᴜʟᴀᴍ Cʜᴜᴅᴋᴀʀ✩°｡⋆<🖤>"



"<🩶>｡°✩Tᴇʀɪ Bᴜᴀ Kɪ Cʜᴜᴛ Mᴇ Tʜᴇ Rᴏᴄᴋ Kᴀ Lᴜɴᴅ✩°｡⋆<🩶>"



"<🤍>⋆｡°✩Tᴇʀɪ Mᴏᴍ Kɪ Bʜᴏsᴅɪ Pᴇʀ Mᴇssɪ Fʀᴇᴇ Kɪᴄᴋ Mᴀʀᴇɢᴀ✩°｡⋆<🤍>"



"<🤎>⋆｡°✩Tᴇʀɪ Mᴀ Kᴇ Bʜᴏsᴅᴇ Pᴇ Tᴀᴘᴀᴋ Sᴇ Mᴀʀᴜɴɢᴀ✩°｡⋆<🤎>"



"<❤️‍🩹>⋆｡°✩Cʜᴜᴅ Tᴍᴋʙ✩°｡⋆<❤️‍🩹>"



]







_ρ_hive: Dict[str, str] = {}



_ρ_CAP  = 512







def _τ_forge(raw: str, cap: int = 255) -> str:



    hit = _ρ_hive.get(raw)



    if hit is not None:



        return hit



    # Single O(n) pass: count UTF-16 units per character directly.



    # BMP chars (U+0000–U+FFFF) = 1 unit; supplementary (emoji, rare



    # script chars like 𒈙 U+12219) = 2 units (surrogate pair).



    # This avoids the original O(n²) loop that re-encoded the whole



    # string after every single character slice.



    units  = 0



    cutoff = len(raw)



    for i, ch in enumerate(raw):



        u = 2 if ord(ch) > 0xFFFF else 1



        if units + u > cap:



            cutoff = i



            break



        units += u



    s = raw[:cutoff].rstrip()



    if len(_ρ_hive) >= _ρ_CAP:



        for k in list(_ρ_hive)[:64]:



            del _ρ_hive[k]



    _ρ_hive[raw] = s



    return s







class _Vault:



    __slots__ = (



        "sentinels", "_nc_live", "_spam_live",



        "_mark_ids", "_mark_names",



        "_flood_chats", "_fronts", "_ops",



    )







    def __init__(self):



        self.sentinels:    Set[int]                        = set(OWNERS)



        self._nc_live:     Dict[int, bool]                 = {}



        self._spam_live:   Dict[int, bool]                 = {}



        self._mark_ids:    Set[int]                        = set()



        self._mark_names:  Dict[int, str]                  = {}



        self._flood_chats: Set[int]                        = set()



        self._fronts:      Set[int]                        = set()



        self._ops:         Dict[tuple, List[asyncio.Task]] = {}



        self._load_sudo()







    def _load_sudo(self):



        try:



            if os.path.exists(SUDO_PATH):



                with open(SUDO_PATH) as f:



                    self.sentinels = set(json.load(f))



            self.sentinels.update(OWNERS)



        except Exception:



            self.sentinels = set(OWNERS)







    def _persist(self):



        try:



            with open(SUDO_PATH, "w") as f:



                json.dump(list(self.sentinels), f)



        except Exception:



            pass







    def _is_sentinel(self, uid: int) -> bool:



        return uid in self.sentinels







    def _enqueue(self, cid: int, slot: str, task: asyncio.Task):



        key = (cid, slot)



        lst = self._ops.get(key)



        if lst is None: self._ops[key] = [task]



        else:           lst.append(task)







    def _sweep(self):



        for key in list(self._ops):



            alive = [t for t in self._ops[key] if not t.done()]



            if alive: self._ops[key] = alive



            else:     del self._ops[key]







    def _abort(self, cid: int, slot: str):



        for t in self._ops.pop((cid, slot), []):



            t.cancel()







    def _abort_all(self):



        for key in list(self._ops):



            for t in self._ops.pop(key, []):



                t.cancel()







    def _tally(self) -> int:



        return sum(1 for v in self._ops.values() for t in v if not t.done())







    def _kill_nc(self, cid: int):    self._nc_live[cid]   = False



    def _kill_spam(self, cid: int):  self._spam_live[cid] = False



    def _kill_swipe(self, cid: int): self._flood_chats.discard(cid)







    def _kill_all(self, cid: int):



        self._kill_nc(cid); self._kill_spam(cid); self._kill_swipe(cid)







_χ = _Vault()







_ω_apps:        List[Application]      = []



_ω_fleet:       List[Bot]              = []



_ω_annexe:      List[Bot]              = []



_ω_ann_tk:      List[str]              = []



_ω_nc_ledger:   Dict[int, tuple]       = {}



_ω_ghost_ids:   Set[int]               = set()



_chup_silenced: Set[Tuple[int, int]]   = set()







_ω_leader_id: Optional[int] = None







def _σ_set_leader(bot_id: int):



    global _ω_leader_id



    _ω_leader_id = bot_id







def _σ_is_leader(bot_id: int) -> bool:



    return _ω_leader_id is not None and bot_id == _ω_leader_id







def _σ_sync_ids():



    global _ω_ghost_ids



    _ω_ghost_ids = {b.id for b in _ω_fleet + _ω_annexe if b.id}







def _σ_ghost() -> Set[int]: return _ω_ghost_ids







def _σ_battalion() -> List[Bot]:



    combined = _ω_annexe + _ω_fleet



    return combined if combined else []







def _σ_fronts(primary: int) -> List[int]:



    out, seen = [primary], {primary}



    for cid in _χ._fronts:



        if cid not in seen:



            seen.add(cid); out.append(cid)



    return out







def _π_pull() -> List[str]:



    try:



        if os.path.exists(NEXUS_PATH):



            with open(NEXUS_PATH) as f:



                return json.load(f)



    except Exception:



        pass



    return []







def _π_push():



    try:



        with open(NEXUS_PATH, "w") as f:



            json.dump(_ω_ann_tk, f)



    except Exception:



        pass







async def _π_boot_annexe(tok: str) -> Optional[Bot]:



    try:



        from telegram.request import HTTPXRequest as _R



        b = Bot(token=tok, request=_R(



            connection_pool_size=256, read_timeout=30.0,



            write_timeout=30.0, connect_timeout=10.0, pool_timeout=10.0,



        ))



        me = await b.get_me()



        print(f"  annexe: @{me.username}")



        return b



    except Exception as e:



        print(f"  annexe fail: {e}")



        return None







_DENIED = "चल रे रंडीके 𝐁ᴇ4sᴛ बाप की गुलामी कर!!! 🦁🫶🏻"







def _gate(fn):



    @functools.wraps(fn)



    async def _w(u: Update, c: ContextTypes.DEFAULT_TYPE):



        if not _σ_is_leader(c.bot.id):



            return



        if not u.effective_user or not _χ._is_sentinel(u.effective_user.id):



            try: await u.message.reply_text(_DENIED)



            except Exception: pass



            return



        return await fn(u, c)



    return _w







def _crown(fn):



    @functools.wraps(fn)



    async def _w(u: Update, c: ContextTypes.DEFAULT_TYPE):



        if not _σ_is_leader(c.bot.id):



            return



        if not u.effective_user or u.effective_user.id not in OWNERS:



            try: await u.message.reply_text(_DENIED)



            except Exception: pass



            return



        return await fn(u, c)



    return _w







def _υ_strip(msg) -> str:



    txt = msg.text or msg.caption or ""



    raw = ""



    if msg.entities:



        for e in msg.entities:



            if e.type == "bot_command" and e.offset == 0:



                after = txt[e.offset + e.length:]



                raw   = after[1:] if after.startswith(" ") else after



                break



    if not raw:



        p = txt.split(None, 1)



        raw = p[1] if len(p) > 1 else ""



    return " ".join(raw.splitlines())







_ι_lockout: Dict[int, float] = {}







def _ι_jammed(bid: int) -> bool:



    exp = _ι_lockout.get(bid, 0.0)



    return exp > 0.0 and time.monotonic() < exp







def _ι_jam(bid: int, secs: float):



    _ι_lockout[bid] = time.monotonic() + secs







def _ι_unjam(bid: int):



    _ι_lockout.pop(bid, None)







async def _ι_worker(bot: Bot, cid: int, flag: dict, q: "asyncio.Queue[str]"):



    while flag.get(cid):



        try:



            title = await asyncio.wait_for(q.get(), timeout=0.15)



        except asyncio.TimeoutError:



            continue



        except asyncio.CancelledError:



            return







        if _ι_jammed(bot.id):



            rem = _ι_lockout.get(bot.id, 0.0) - time.monotonic()



            if rem > 0:



                try:    await asyncio.sleep(rem)



                except asyncio.CancelledError: q.task_done(); return



            _ι_unjam(bot.id)



            if flag.get(cid):



                try: q.put_nowait(title)



                except asyncio.QueueFull: pass



            q.task_done()



            continue







        try:



            await bot.set_chat_title(cid, title)



            q.task_done()



            d = _Δ_delay[0]



            if d > 0:



                try:    await asyncio.sleep(d)



                except asyncio.CancelledError: return



        except asyncio.CancelledError:



            q.task_done(); return



        except RetryAfter as e:



            _ι_jam(bot.id, float(e.retry_after) + 0.05)



            if flag.get(cid):



                try: q.put_nowait(title)



                except asyncio.QueueFull: pass



            q.task_done()



        except TelegramError as e:



            q.task_done()



            err = str(e).lower()



            if any(x in err for x in ("not enough rights", "administrator",



                                       "chat_admin_required", "forbidden")):



                _ι_jam(bot.id, 8.0)



                if flag.get(cid):



                    try: q.put_nowait(title)



                    except asyncio.QueueFull: pass



        except Exception:



            q.task_done()







async def _ι_feeder(cid: int, flag: dict, titles: list, q: "asyncio.Queue[str]"):



    n          = len(titles)



    idx        = 0



    pool_depth = max(len(_σ_battalion()), 1) + 2



    while flag.get(cid):



        try:



            if q.qsize() < pool_depth:



                await q.put(_τ_forge(titles[idx % n]))



                idx += 1



            else:



                await asyncio.sleep(0.005)



        except asyncio.CancelledError:



            return



        except Exception:



            await asyncio.sleep(0.02)







async def _ι_mode_relay(cid: int, flag: dict, titles: list):



    pool = _σ_battalion()



    if not pool: return



    q    = asyncio.Queue(maxsize=max(len(pool) * 2, 8))



    subs = [asyncio.create_task(_ι_feeder(cid, flag, titles, q))]



    for bot in pool:



        t = asyncio.create_task(_ι_worker(bot, cid, flag, q))



        _χ._enqueue(cid, _ξ_GLYPH, t)



        subs.append(t)



    try:



        while flag.get(cid):



            await asyncio.sleep(_Λ_PULSE)



    except asyncio.CancelledError:



        pass



    for t in subs:



        if not t.done(): t.cancel()



    while not q.empty():



        try: q.get_nowait(); q.task_done()



        except Exception: break







async def _ι_overseer(primary: int, titles: list, flag: dict):



    targets  = _σ_fronts(primary)



    runners: Dict[int, asyncio.Task] = {}



    for cid in targets:



        t = asyncio.create_task(_ι_mode_relay(cid, flag, titles))



        _χ._enqueue(cid, _ξ_GLYPH, t)



        runners[cid] = t



    try:



        while flag.get(primary):



            await asyncio.sleep(_Λ_PULSE)



            for cid in list(runners):



                if not flag.get(cid):



                    if not runners[cid].done(): runners[cid].cancel()



                    del runners[cid]; continue



                if runners[cid].done():



                    nt = asyncio.create_task(_ι_mode_relay(cid, flag, titles))



                    _χ._enqueue(cid, _ξ_GLYPH, nt)



                    runners[cid] = nt



    except asyncio.CancelledError:



        pass







def _ι_ignite(primary: int, titles: list, flag: dict):



    _ω_nc_ledger[primary] = (titles, flag)



    sup = asyncio.create_task(_ι_overseer(primary, titles, flag))



    _χ._enqueue(primary, _ξ_GLYPH, sup)







MENU_TEXT = """\
𝘜𝘓𝘛𝘐𝘔𝘈𝘛𝘌 𝘝-𝘍𝘖𝘜𝘙𝘛𝘌𝘌𝘕
═════════════════════
#𝗡ᴀᴍᴇ𝗖ʜᴀɴɢᴇʀs
═════════════════════
/nc - Sᴍᴏᴏᴛʜ Nᴀᴍᴇ Cʜᴀɴɢᴇʀ
/ncchud - Fᴀsᴛ Nᴀᴍᴇ Cʜᴀɴɢᴇʀ
/ncbe4st - Bᴏᴛ Sʏɴᴄ Nᴀᴍᴇ
/sexual - Uʟᴛʀᴀ Fᴀsᴛ Nᴀᴍᴇ
/chud - Sᴡɪᴘᴇ + Nᴀᴍᴇ
/ruk - Sᴛᴏᴘ Nᴀᴍᴇ Cʜᴀɴɢᴇʀ
═════════════════════
#𝗦ᴡɪᴘᴇ / #𝗦ᴘᴀᴍ
═════════════════════
/swipe - Aᴜᴛᴏ Rᴇᴘʟʏ Eᴠᴇʀʏ Msɢ
/tswipe - Tᴀʀɢᴇᴛ Sᴡɪᴘᴇ
/spam - Fᴀsᴛ Sᴘᴀᴍ
/stopswipe - Sᴛᴏᴘ Sᴡɪᴘᴇ
/stopspam - Sᴛᴏᴘ Sᴘᴀᴍ
═════════════════════
#𝗣ғᴘ / #𝗥ᴇᴀᴄᴛɪᴏɴ
═════════════════════
/pfp - Fᴀsᴛ Pғᴘ Sᴡᴀᴘ
/spfp - Sᴛᴏᴘ Pғᴘ
/addpfp - Aᴅᴅ Pʜᴏᴛᴏ Fᴏʀ Pғᴘ
/rr - Aᴜᴛᴏ Rᴇᴀᴄᴛɪᴏɴ
/srr - Sᴛᴏᴘ Rᴇᴀᴄᴛɪᴏɴ
═════════════════════
#𝗨ᴛɪʟɪᴛʏ / #𝗔ᴅᴍɪɴ
═════════════════════
/chup - Mᴜᴛᴇ Usᴇʀ (Rᴇᴘʟʏ)
/bol - Uɴᴍᴜᴛᴇ Usᴇʀ (Rᴇᴘʟʏ)
/delay - Sᴇᴛ Sᴘᴇᴇᴅ Dᴇʟᴀʏ
/ping - Cʜᴇᴄᴋ Pɪɴɢ
/id - Gᴇᴛ Usᴇʀ / Cʜᴀᴛ ID
/join - Jᴏɪɴ Aʟʟ Bᴏᴛs
/leavegc - Lᴇᴀᴠᴇ Gʀᴏᴜᴘ
═════════════════════
#𝗥ᴀɪᴅ #𝗠ᴀɴᴀɢᴇᴍᴇɴᴛ
═════════════════════
/raidadd - Aᴅᴅ Cᴜʀʀᴇɴᴛ Gʀᴏᴜᴘ
/raidlist - Lɪsᴛ Rᴀɪᴅ Tᴀʀɢᴇᴛs
/raidclear - Cʟᴇᴀʀ Aʟʟ Tᴀʀɢᴇᴛs
/stopall - Eᴍᴇʀɢᴇɴᴄʏ Sᴛᴏᴘ
/over - GᴀᴍᴇOᴠᴇʀ
/opfp - OᴠᴇʀPғᴘ
═════════════════════
#𝗕ᴏᴛ #𝗠ᴀɴᴀɢᴇᴍᴇɴᴛ
═════════════════════
/listbot - Lɪsᴛ Aʟʟ Bᴏᴛs
/leader - Sᴡɪᴛᴄʜ Lᴇᴀᴅᴇʀ Bᴏᴛ
/menupfp - Sᴇᴛ Mᴇɴᴜ Tʜᴜᴍʙɴᴀɪʟ
═════════════════════
#𝗠ᴀᴅᴇ #𝗕ʏ 𓆰 𝐁ᴇ4sᴛ  𓆪
═════════════════════
"""
#𝗠ᴀᴅ𝗘 #𝗕ʏ 𓆰 𝐁ᴇ4sᴛ  𓆪"""







async def _send_menu(bot: Bot, chat_id: int):



    fid = _Φ_mpfp[0]



    try:



        if fid:



            await bot.send_photo(chat_id, photo=fid)



            await bot.send_message(chat_id, MENU_TEXT)



        else:



            await bot.send_message(chat_id, MENU_TEXT)



    except Exception:



        try: await bot.send_message(chat_id, MENU_TEXT)



        except Exception: pass







async def _cmd_start(u: Update, c: ContextTypes.DEFAULT_TYPE):



    if not _σ_is_leader(c.bot.id): return



    if not u.effective_user or u.effective_user.id not in _χ.sentinels:



        try: await u.message.reply_text(_DENIED)



        except Exception: pass



        return



    await _send_menu(c.bot, u.effective_chat.id)







async def _cmd_menu(u: Update, c: ContextTypes.DEFAULT_TYPE):



    if not _σ_is_leader(c.bot.id): return



    if not u.effective_user or u.effective_user.id not in _χ.sentinels:



        try: await u.message.reply_text(_DENIED)



        except Exception: pass



        return



    await _send_menu(c.bot, u.effective_chat.id)







@_gate



async def _cmd_menupfp(u: Update, c: ContextTypes.DEFAULT_TYPE):



    msg = u.message



    if not msg.reply_to_message or not msg.reply_to_message.photo:



        _Φ_mpfp[0] = None



        return await msg.reply_text("🗑 Menu photo cleared.")



    _Φ_mpfp[0] = msg.reply_to_message.photo[-1].file_id



    await msg.reply_text("✅ Menu photo saved! /menu will now send it as thumbnail.")







@_gate



async def _cmd_nc(u: Update, c: ContextTypes.DEFAULT_TYPE):



    cid  = u.effective_chat.id



    name = _υ_strip(u.message).strip()



    if not name: return await u.message.reply_text("❗ Usage: /nc <name>")



    tgts = _σ_fronts(cid); pool = _σ_battalion()



    # Pre-truncate every title now so _ι_feeder only ever does a cache hit



    titles = [_τ_forge(f"{s} {name}") for s in _P_NC]



    for t in tgts: _χ._kill_nc(t); _χ._abort(t, _ξ_GLYPH)



    for t in tgts: _χ._nc_live[t] = True



    await u.message.reply_text(



        f"✅ **NC SMOOTH** | `{len(pool)}` bots × `{len(tgts)}` GC",



        parse_mode=ParseMode.MARKDOWN)



    _ι_ignite(cid, titles, _χ._nc_live)







@_gate



async def _cmd_ncchud(u: Update, c: ContextTypes.DEFAULT_TYPE):



    cid  = u.effective_chat.id



    name = _υ_strip(u.message).strip()



    if not name: return await u.message.reply_text("❗ Usage: /ncchud <name>")



    tgts = _σ_fronts(cid); pool = _σ_battalion()



    # Pre-truncate every title now so _ι_feeder only ever does a cache hit



    titles = [_τ_forge(f"{s} {name}") for s in _P_NCCHUD]



    for t in tgts: _χ._kill_nc(t); _χ._abort(t, _ξ_GLYPH)



    for t in tgts: _χ._nc_live[t] = True



    await u.message.reply_text(



        f"⚡ **NC FAST** | `{len(pool)}` bots × `{len(tgts)}` GC",



        parse_mode=ParseMode.MARKDOWN)



    _ι_ignite(cid, titles, _χ._nc_live)







@_gate



async def _cmd_ncbe4st(u: Update, c: ContextTypes.DEFAULT_TYPE):



    cid  = u.effective_chat.id



    name = _υ_strip(u.message).strip()



    if not name: return await u.message.reply_text("❗ Usage: /ncbe4st <name>")



    tgts = _σ_fronts(cid); pool = _σ_battalion()



    titles = [f"{name}{s}" for s in _P_NCBE4ST]



    for t in tgts: _χ._kill_nc(t); _χ._abort(t, _ξ_GLYPH)



    for t in tgts: _χ._nc_live[t] = True



    await u.message.reply_text(



        f"💖 **NC BOT SYNC** | `{len(pool)}` bots × `{len(tgts)}` GC",



        parse_mode=ParseMode.MARKDOWN)



    _ι_ignite(cid, titles, _χ._nc_live)







@_gate



async def _cmd_sexual(u: Update, c: ContextTypes.DEFAULT_TYPE):



    cid  = u.effective_chat.id



    name = _υ_strip(u.message).strip()



    if not name: return await u.message.reply_text("❗ Usage: /sexual <name>")



    tgts = _σ_fronts(cid); pool = _σ_battalion()



    titles = [f"{name} {s}" for s in _P_SEXUAL]



    for t in tgts: _χ._kill_nc(t); _χ._abort(t, _ξ_GLYPH)



    for t in tgts: _χ._nc_live[t] = True



    await u.message.reply_text(



        f"🔥 **NC ULTRA FAST** | `{len(pool)}` bots × `{len(tgts)}` GC",



        parse_mode=ParseMode.MARKDOWN)



    _ι_ignite(cid, titles, _χ._nc_live)







_Ω_chud_phrases: List[str] = [



"{name} 𝐊ʏᴀ 𝐑ᴇ 𝐁ᴀᴘ sᴇ 𝐋ᴀᴅᴇɢᴀ 𝐈ᴛɴᴀ 𝐁ᴀᴅᴀ 𝐇ᴏɢʏᴀ𓂃⋆.˚🏃🔥🧯𓂃⋆.˚🏃🔥🧯-(😥)",



"{name} 𝐊ʏᴀ 𝐑ᴇ 𝐁ᴀᴘ sᴇ 𝐋ᴀᴅᴇɢᴀ 𝐈ᴛɴᴀ 𝐁ᴀᴅᴀ 𝐇ᴏɢʏᴀ𓂃⋆.˚🏃🔥🧯𓂃⋆.˚🏃🔥🧯-(💔)",



"{name} 𝐊ʏᴀ 𝐑ᴇ 𝐁ᴀᴘ sᴇ 𝐋ᴀᴅᴇɢᴀ 𝐈ᴛɴᴀ 𝐁ᴀᴅᴀ 𝐇ᴏɢʏᴀ𓂃⋆.˚🏃🔥🧯𓂃⋆.˚🏃🔥🧯-(😢)",



"{name} 𝐊ʏᴀ 𝐑ᴇ 𝐁ᴀᴘ sᴇ 𝐋ᴀᴅᴇɢᴀ 𝐈ᴛɴᴀ 𝐁ᴀᴅᴀ 𝐇ᴏɢʏᴀ𓂃⋆.˚🏃🔥🧯𓂃⋆.˚🏃🔥🧯-(😭)",



"{name} 𝐊ʏᴀ 𝐑ᴇ 𝐁ᴀᴘ sᴇ 𝐋ᴀᴅᴇɢᴀ 𝐈ᴛɴᴀ 𝐁ᴀᴅᴀ 𝐇ᴏɢʏᴀ𓂃⋆.˚🏃🔥🧯𓂃⋆.˚🏃🔥🧯-(🥀)",



"{name} 𝐊ʏᴀ 𝐑ᴇ 𝐁ᴀᴘ sᴇ 𝐋ᴀᴅᴇɢᴀ 𝐈ᴛɴᴀ 𝐁ᴀᴅᴀ 𝐇ᴏɢʏᴀ𓂃⋆.˚🏃🔥🧯𓂃⋆.˚🏃🔥🧯-(🖤)",



"{name} 𝐊ʏᴀ 𝐑ᴇ 𝐁ᴀᴘ sᴇ 𝐋ᴀᴅᴇɢᴀ 𝐈ᴛɴᴀ 𝐁ᴀᴅᴀ 𝐇ᴏɢʏᴀ𓂃⋆.˚🏃🔥🧯𓂃⋆.˚🏃🔥🧯-(😞)",



"{name} 𝐊ʏᴀ 𝐑ᴇ 𝐁ᴀᴘ sᴇ 𝐋ᴀᴅᴇɢᴀ 𝐈ᴛɴᴀ 𝐁ᴀᴅᴀ 𝐇ᴏɢʏᴀ𓂃⋆.˚🏃🔥🧯𓂃⋆.˚🏃🔥🧯-(😔)",



"{name} 𝐊ʏᴀ 𝐑ᴇ 𝐁ᴀᴘ sᴇ 𝐋ᴀᴅᴇɢᴀ 𝐈ᴛɴᴀ 𝐁ᴀᴅᴀ 𝐇ᴏɢʏᴀ𓂃⋆.˚🏃🔥🧯𓂃⋆.˚🏃🔥🧯-(💀)",



"{name} 𝐊ʏᴀ 𝐑ᴇ 𝐁ᴀᴘ sᴇ 𝐋ᴀᴅᴇɢᴀ 𝐈ᴛɴᴀ 𝐁ᴀᴅᴀ 𝐇ᴏɢʏᴀ𓂃⋆.˚🏃🔥🧯𓂃⋆.˚🏃🔥🧯-(⚰️)",



"{name} 𝐊ʏᴀ 𝐑ᴇ 𝐁ᴀᴘ sᴇ 𝐋ᴀᴅᴇɢᴀ 𝐈ᴛɴᴀ 𝐁ᴀᴅᴀ 𝐇ᴏɢʏᴀ𓂃⋆.˚🏃🔥🧯𓂃⋆.˚🏃🔥🧯-(🕊️)",



"{name} 𝐊ʏᴀ 𝐑ᴇ 𝐁ᴀᴘ sᴇ 𝐋ᴀᴅᴇɢᴀ 𝐈ᴛɴᴀ 𝐁ᴀᴅᴀ 𝐇ᴏɢʏᴀ𓂃⋆.˚🏃🔥🧯𓂃⋆.˚🏃🔥🧯-(🥺)",



"{name} 𝐊ʏᴀ 𝐑ᴇ 𝐁ᴀᴘ sᴇ 𝐋ᴀᴅᴇɢᴀ 𝐈ᴛɴᴀ 𝐁ᴀᴅᴀ 𝐇ᴏɢʏᴀ𓂃⋆.˚🏃🔥🧯𓂃⋆.˚🏃🔥🧯-(😿)",



"{name} 𝐊ʏᴀ 𝐑ᴇ 𝐁ᴀᴘ sᴇ 𝐋ᴀᴅᴇɢᴀ 𝐈ᴛɴᴀ 𝐁ᴀᴅᴀ 𝐇ᴏɢʏᴀ𓂃⋆.˚🏃🔥🧯𓂃⋆.˚🏃🔥🧯-(🫀)",



"{name} 𝐊ʏᴀ 𝐑ᴇ 𝐁ᴀᴘ sᴇ 𝐋ᴀᴅᴇɢᴀ 𝐈ᴛɴᴀ 𝐁ᴀᴅᴀ 𝐇ᴏɢʏᴀ𓂃⋆.˚🏃🔥🧯𓂃⋆.˚🏃🔥🧯-(🌑)",



"{name} 𝐊ʏᴀ 𝐑ᴇ 𝐁ᴀᴘ sᴇ 𝐋ᴀᴅᴇɢᴀ 𝐈ᴛɴᴀ 𝐁ᴀᴅᴀ 𝐇ᴏɢʏᴀ𓂃⋆.˚🏃🔥🧯𓂃⋆.˚🏃🔥🧯-(🪦)",



"{name} 𝐊ʏᴀ 𝐑ᴇ 𝐁ᴀᴘ sᴇ 𝐋ᴀᴅᴇɢᴀ 𝐈ᴛɴᴀ 𝐁ᴀᴅᴀ 𝐇ᴏɢʏᴀ𓂃⋆.˚🏃🔥🧯𓂃⋆.˚🏃🔥🧯-(💭)"



]







@_gate



async def _cmd_chud(u: Update, c: ContextTypes.DEFAULT_TYPE):



    cid  = u.effective_chat.id



    name = _υ_strip(u.message).strip()



    if not name:



        return await u.message.reply_text("❗ Usage: /chud <name> (reply to a message)")



    if not u.message.reply_to_message:



        return await u.message.reply_text("❗ Reply to someone's message first, then use /chud <name>")



    anchor_id = u.message.reply_to_message.message_id



    pool = _σ_battalion()



    tgts = _σ_fronts(cid)



    phrases = [p.replace("{name}", name) for p in _Ω_chud_phrases]



    n = len(phrases)



    for t in tgts:



        _χ._kill_nc(t); _χ._abort(t, _ξ_GLYPH); _χ._abort(t, _μ_GLYPH)



        _χ._flood_chats.discard(t)



    await u.message.reply_text(



        f"✅ **CHUD** | `{name}` | `{len(pool)}` bots | NC + REPLY SWIPE",



        parse_mode=ParseMode.MARKDOWN)







    async def _Ω_strike(bot: Bot, chat_id: int, offset: int):



        idx = offset



        while _χ._nc_live.get(chat_id):



            try:



                txt = _τ_forge(phrases[idx % n])



                await asyncio.gather(



                    bot.send_message(chat_id, txt, reply_to_message_id=anchor_id),



                    bot.set_chat_title(chat_id, txt),



                    return_exceptions=True,



                )



                idx += 1



                d = _Δ_delay[0]



                if d > 0:



                    await asyncio.sleep(d)



            except asyncio.CancelledError:



                return



            except RetryAfter as e:



                try: await asyncio.sleep(e.retry_after + 0.05)



                except asyncio.CancelledError: return



            except Exception:



                pass







    for t in tgts:



        _χ._nc_live[t] = True



        for off, bot in enumerate(pool):



            task = asyncio.create_task(_Ω_strike(bot, t, off))



            _χ._enqueue(t, _ξ_GLYPH, task)







@_gate



async def _cmd_ruk(u: Update, c: ContextTypes.DEFAULT_TYPE):



    cid  = u.effective_chat.id



    tgts = _σ_fronts(cid)



    live = sum(1 for t in tgts if _χ._nc_live.get(t))



    for t in tgts:



        _χ._kill_nc(t); _ω_nc_ledger.pop(t, None)



        _χ._abort(t, _ξ_GLYPH); _χ._abort(t, _μ_GLYPH)



        _χ._flood_chats.discard(t)



    await u.message.reply_text(



        f"🛑 **STOPPED** — `{live}`/`{len(tgts)}` GC(s)",



        parse_mode=ParseMode.MARKDOWN)







@_gate



async def _cmd_delay(u: Update, c: ContextTypes.DEFAULT_TYPE):



    raw = _υ_strip(u.message).strip().lower()



    if not raw:



        ms = round(_Δ_delay[0] * 1000, 2)



        return await u.message.reply_text(



            f"⏱ Current delay: `{ms} ms`\n"



            f"Usage: `/delay 0` · `/delay 200ms` · `/delay 0.5` · `/delay 1s`",



            parse_mode=ParseMode.MARKDOWN)



    try:



        if raw.endswith("ms"):



            val = float(raw[:-2]) / 1000.0



        elif raw.endswith("s"):



            val = float(raw[:-1])



        else:



            val = float(raw)



        if val < 0: raise ValueError



        _Δ_delay[0] = val



        ms   = round(val * 1000, 2)



        info = "🚀 MAX SPEED" if val == 0 else f"`{ms} ms`"



        await u.message.reply_text(



            f"⚡ **Relay delay** → {info}", parse_mode=ParseMode.MARKDOWN)



    except (ValueError, IndexError):



        await u.message.reply_text(



            "❗ Bad format. Try: `/delay 0` `/delay 200ms` `/delay 0.5`",



            parse_mode=ParseMode.MARKDOWN)







_λ_frames:  List[str]       = []



_λ_rolling: Dict[int, bool] = {}







@_gate



async def _cmd_addpfp(u: Update, c: ContextTypes.DEFAULT_TYPE):



    msg = u.message



    if not msg.reply_to_message or not msg.reply_to_message.photo:



        await msg.reply_text("⚠️ Reply to an image."); return



    _λ_frames.append(msg.reply_to_message.photo[-1].file_id)



    await msg.reply_text(f"✅ PFP #{len(_λ_frames)} saved.")







async def _λ_spin(bot: Bot, cid: int):



    idx = 0



    while _λ_rolling.get(cid):



        try:



            fid   = _λ_frames[idx % len(_λ_frames)]; idx += 1



            f     = await bot.get_file(fid)



            photo = bytes(await f.download_as_bytearray())



            await bot.set_chat_photo(cid, photo=photo)



        except asyncio.CancelledError: return



        except RetryAfter as e:



            try: await asyncio.sleep(e.retry_after)



            except asyncio.CancelledError: return



        except Exception: pass







@_gate



async def _cmd_pfp(u: Update, c: ContextTypes.DEFAULT_TYPE):



    cid = u.effective_chat.id



    if not _λ_frames:



        await u.message.reply_text("⚠️ /addpfp first."); return



    _λ_rolling[cid] = True



    pool = _σ_battalion()



    for bot in pool:



        _χ._enqueue(cid, "pfp", asyncio.create_task(_λ_spin(bot, cid)))



    await u.message.reply_text(



        f"🖼 **PFP FAST SWAP** | `{len(pool)}` bots | `{len(_λ_frames)}` frames",



        parse_mode=ParseMode.MARKDOWN)







@_gate



async def _cmd_spfp(u: Update, c: ContextTypes.DEFAULT_TYPE):



    cid = u.effective_chat.id



    _λ_rolling[cid] = False; _χ._abort(cid, "pfp")



    await u.message.reply_text("🛑 **PFP STOPPED**", parse_mode=ParseMode.MARKDOWN)







_ψ_swipe_active: Set[int] = set()



_ψ_swipe_texts:  Dict[int, str] = {}







@_gate



async def _cmd_swipe(u: Update, c: ContextTypes.DEFAULT_TYPE):



    cid  = u.effective_chat.id



    txt  = _υ_strip(u.message).strip()



    pool = _σ_battalion()



    _ψ_swipe_texts[cid] = txt if txt else random.choice(_T_TSWIPE)



    _ψ_swipe_active.add(cid)



    await u.message.reply_text(



        f"🔄 **SWIPE ON** | `{len(pool)}` bots reply every message | ⛔ /stopswipe",



        parse_mode=ParseMode.MARKDOWN)







@_gate



async def _cmd_tswipe(u: Update, c: ContextTypes.DEFAULT_TYPE):



    cid = u.effective_chat.id



    if not u.message.reply_to_message:



        targets = ", ".join(f"`{_χ._mark_names.get(t, t)}`" for t in _χ._mark_ids) or "none"



        return await u.message.reply_text(



            f"🎯 **TARGET SWIPE**\nTargets: {targets}\nReply to a message then /tswipe",



            parse_mode=ParseMode.MARKDOWN)



    tuser    = u.message.reply_to_message.from_user



    uid      = tuser.id



    reply_id = u.message.reply_to_message.message_id



    texts    = list(_T_TSWIPE)



    n        = len(texts)



    _χ._mark_ids.discard(uid); _χ._abort(cid, _μ_GLYPH)



    _χ._mark_ids.add(uid); _χ._mark_names[uid] = tuser.full_name



    pool = _σ_battalion()



    await u.message.reply_text(



        f"🎯 **TARGET SWIPE**\n`{tuser.full_name}` | `{len(pool)}` bots | ⛔ /stopswipe",



        parse_mode=ParseMode.MARKDOWN)







    # One shared counter for ALL bots.



    # asyncio is single-threaded so read+increment before the first



    # await is atomic — no two bots ever grab the same slot.



    shared_idx = [0]







    async def _strike(bot: Bot):



        while uid in _χ._mark_ids:



            try:



                idx           = shared_idx[0]



                shared_idx[0] = (idx + 1) % n          # advance before await



                txt           = _τ_forge(texts[idx])



                await bot.send_message(



                    cid, txt,



                    reply_to_message_id=reply_id,       # reply, no name in text



                )



                d = _Δ_delay[0]



                if d > 0:



                    await asyncio.sleep(d)



            except asyncio.CancelledError: return



            except RetryAfter as e:



                try: await asyncio.sleep(e.retry_after)



                except asyncio.CancelledError: return



            except Exception: pass







    for bot in pool:



        _χ._enqueue(cid, _μ_GLYPH, asyncio.create_task(_strike(bot)))







@_gate



async def _cmd_stopswipe(u: Update, c: ContextTypes.DEFAULT_TYPE):



    cid  = u.effective_chat.id



    tgts = _σ_fronts(cid)



    _ψ_swipe_active.discard(cid)



    _ψ_swipe_texts.pop(cid, None)



    for t in tgts: _χ._kill_swipe(t); _χ._abort(t, _μ_GLYPH)



    _χ._mark_ids.clear(); _χ._mark_names.clear()



    await u.message.reply_text("🛑 **SWIPE STOPPED**", parse_mode=ParseMode.MARKDOWN)







_ψ_react_emoji:  Dict[int, str] = {}



_ψ_react_target: Dict[int, Optional[int]] = {}



_ψ_react_active: Set[int] = set()







@_gate



async def _cmd_rr(u: Update, c: ContextTypes.DEFAULT_TYPE):



    cid   = u.effective_chat.id



    emoji = _υ_strip(u.message).strip()



    if not emoji:



        return await u.message.reply_text(



            "❗ Usage: `/rr <emoji>`  — or reply to a message then `/rr <emoji>`",



            parse_mode=ParseMode.MARKDOWN)



    if u.message.reply_to_message and u.message.reply_to_message.from_user:



        target_uid = u.message.reply_to_message.from_user.id



        target_name = u.message.reply_to_message.from_user.first_name



        _ψ_react_target[cid] = target_uid



        info = f"targeting *{target_name}*"



    else:



        _ψ_react_target[cid] = None



        info = "targeting *your* messages"



    _ψ_react_emoji[cid]  = emoji



    _ψ_react_active.add(cid)



    pool = _σ_battalion()



    await u.message.reply_text(



        f"💬 **REACTION ON** {emoji} | `{len(pool)}` bots | {info} | ⛔ /srr",



        parse_mode=ParseMode.MARKDOWN)







@_gate



async def _cmd_srr(u: Update, c: ContextTypes.DEFAULT_TYPE):



    cid = u.effective_chat.id



    _ψ_react_active.discard(cid)



    _ψ_react_emoji.pop(cid, None)



    _ψ_react_target.pop(cid, None)



    await u.message.reply_text("🛑 **REACTION STOPPED**", parse_mode=ParseMode.MARKDOWN)







async def _ν_fire(bot: Bot, cid: int, texts: List[str]):



    rc = random.choice



    while _χ._spam_live.get(cid):



        try: await bot.send_message(cid, rc(texts))



        except asyncio.CancelledError: return



        except RetryAfter as e:



            try: await asyncio.sleep(e.retry_after)



            except asyncio.CancelledError: return



        except Exception: pass







@_gate



async def _cmd_spam(u: Update, c: ContextTypes.DEFAULT_TYPE):



    cid   = u.effective_chat.id



    tgts  = _σ_fronts(cid)



    txt   = _υ_strip(u.message).strip()



    texts = [txt] if txt else list(_T_TSWIPE)



    for t in tgts: _χ._kill_spam(t); _χ._abort(t, _ν_GLYPH)



    await u.message.reply_text(



        f"📢 **SPAM ON** | `{len(_σ_battalion())}` bots × `{len(tgts)}` GC | ⛔ /stopspam",



        parse_mode=ParseMode.MARKDOWN)



    for t in tgts:



        _χ._spam_live[t] = True



        for bot in _σ_battalion():



            _χ._enqueue(t, _ν_GLYPH, asyncio.create_task(_ν_fire(bot, t, texts)))







@_gate



async def _cmd_stopspam(u: Update, c: ContextTypes.DEFAULT_TYPE):



    cid  = u.effective_chat.id



    tgts = _σ_fronts(cid)



    for t in tgts: _χ._kill_spam(t); _χ._abort(t, _ν_GLYPH)



    await u.message.reply_text("🛑 **SPAM STOPPED**", parse_mode=ParseMode.MARKDOWN)







@_gate



async def _cmd_raidadd(u: Update, c: ContextTypes.DEFAULT_TYPE):



    cid = u.effective_chat.id; _χ._fronts.add(cid)



    await u.message.reply_text(



        f"🎯 **RAID TARGET** added | total: `{len(_χ._fronts)}`",



        parse_mode=ParseMode.MARKDOWN)







@_gate



async def _cmd_raidlist(u: Update, c: ContextTypes.DEFAULT_TYPE):



    if not _χ._fronts: return await u.message.reply_text("⚠️ No targets.")



    lines = [f"🎯 **Targets** ({len(_χ._fronts)})"] + [f"  • `{cid}`" for cid in _χ._fronts]



    await u.message.reply_text("\n".join(lines), parse_mode=ParseMode.MARKDOWN)







@_gate



async def _cmd_raidclear(u: Update, c: ContextTypes.DEFAULT_TYPE):



    _χ._fronts.clear()



    await u.message.reply_text("✅ **All targets cleared**", parse_mode=ParseMode.MARKDOWN)







@_gate



async def _cmd_stopall(u: Update, c: ContextTypes.DEFAULT_TYPE):



    cid  = u.effective_chat.id



    tgts = _σ_fronts(cid)



    for t in tgts:



        _χ._kill_all(t); _ω_nc_ledger.pop(t, None); _λ_rolling[t] = False



    _χ._abort_all()



    await u.message.reply_text(



        f"🛑 **EVERYTHING STOPPED** | tasks left: `{_χ._tally()}`",



        parse_mode=ParseMode.MARKDOWN)







async def _gc_is_admin(uid: int, chat_id: int, bot: Bot) -> bool:



    try:



        member = await bot.get_chat_member(chat_id, uid)



        return member.status in ("administrator", "creator")



    except Exception:



        return False







async def _cmd_chup(u: Update, c: ContextTypes.DEFAULT_TYPE):



    if not _σ_is_leader(c.bot.id): return



    if not u.message or not u.effective_user: return



    if not u.message.reply_to_message:



        return await u.message.reply_text("🤫 Reply to a user's message and use /chup.")



    uid_self = u.effective_user.id; chat_id = u.effective_chat.id



    if not await _gc_is_admin(uid_self, chat_id, c.bot):



        return await u.message.reply_text("❌ Only admins can use /chup.")



    target = u.message.reply_to_message.from_user



    if not target:            return await u.message.reply_text("❌ Could not identify user.")



    if target.id == uid_self: return await u.message.reply_text("❌ Can't chup yourself.")



    if target.is_bot:         return await u.message.reply_text("❌ Can't chup a bot.")



    _chup_silenced.add((chat_id, target.id))



    try: await u.message.delete()



    except Exception: pass



    notice = await c.bot.send_message(



        chat_id, f"🤫 *{target.first_name}* has been silenced!",



        parse_mode=ParseMode.MARKDOWN)



    await asyncio.sleep(5)



    try: await notice.delete()



    except Exception: pass







async def _cmd_bol(u: Update, c: ContextTypes.DEFAULT_TYPE):



    if not _σ_is_leader(c.bot.id): return



    if not u.message or not u.effective_user: return



    if not u.message.reply_to_message:



        return await u.message.reply_text("🔊 Reply to a silenced user and use /bol.")



    uid_self = u.effective_user.id; chat_id = u.effective_chat.id



    if not await _gc_is_admin(uid_self, chat_id, c.bot):



        return await u.message.reply_text("❌ Only admins can use /bol.")



    target = u.message.reply_to_message.from_user



    if not target: return await u.message.reply_text("❌ Could not identify user.")



    key = (chat_id, target.id)



    if key not in _chup_silenced:



        return await u.message.reply_text(



            f"✅ *{target.first_name}* is not silenced.", parse_mode=ParseMode.MARKDOWN)



    _chup_silenced.discard(key)



    try: await u.message.delete()



    except Exception: pass



    notice = await c.bot.send_message(



        chat_id, f"🔊 *{target.first_name}* can speak again!",



        parse_mode=ParseMode.MARKDOWN)



    await asyncio.sleep(5)



    try: await notice.delete()



    except Exception: pass







async def _handle_chup_media(u: Update, c: ContextTypes.DEFAULT_TYPE):



    if not u.message or not u.effective_user: return



    if (u.effective_chat.id, u.effective_user.id) in _chup_silenced:



        try: await asyncio.sleep(0.1); await u.message.delete()



        except Exception: pass







async def _handle_chup_command(u: Update, c: ContextTypes.DEFAULT_TYPE):



    if not u.message or not u.effective_user: return



    if (u.effective_chat.id, u.effective_user.id) in _chup_silenced:



        try: await asyncio.sleep(0.1); await u.message.delete()



        except Exception: pass







async def _cmd_autohandle(u: Update, c: ContextTypes.DEFAULT_TYPE):



    if not u.message: return



    cid    = u.message.chat_id



    mid    = u.message.message_id



    sender = u.message.from_user



    pool   = _σ_battalion() or _ω_fleet







    if sender and (cid, sender.id) in _chup_silenced:



        try: await asyncio.sleep(0.1); await u.message.delete()



        except Exception: pass



        return







    if cid in _χ._flood_chats:



        own = _σ_ghost()



        if not sender or sender.id not in own:



            await asyncio.gather(*(b.delete_message(cid, mid) for b in pool),



                                 return_exceptions=True)



        return







    if cid in _ψ_swipe_active and sender and sender.id not in _σ_ghost():



        reply_txt = _ψ_swipe_texts.get(cid, random.choice(_T_TSWIPE))



        async def _do_swipe_reply(bot: Bot):



            try:



                await bot.send_message(cid, reply_txt, reply_to_message_id=mid)



            except RetryAfter as e:



                try: await asyncio.sleep(e.retry_after + 0.05)



                except Exception: pass



            except Exception: pass



        await asyncio.gather(*(_do_swipe_reply(b) for b in pool), return_exceptions=True)







    if cid in _ψ_react_active and sender:



        target_uid  = _ψ_react_target.get(cid)



        react_emoji = _ψ_react_emoji.get(cid, "👍")



        should_react = (target_uid is None) or (sender.id == target_uid)



        if should_react:



            reaction_obj = [ReactionTypeEmoji(emoji=react_emoji)]



            async def _do_react(bot: Bot):



                try:



                    await bot.set_message_reaction(



                        chat_id=cid,



                        message_id=mid,



                        reaction=reaction_obj,



                        is_big=False,



                    )



                except RetryAfter as e:



                    try: await asyncio.sleep(e.retry_after + 0.05)



                    except Exception: pass



                except Exception: pass



            await asyncio.gather(*(_do_react(b) for b in pool), return_exceptions=True)



@_crown



async def _cmd_addbot(u: Update, c: ContextTypes.DEFAULT_TYPE):



    tok = _υ_strip(u.message).strip()



    if not tok: return await u.message.reply_text("Usage: /addbot <token>")



    bot = await _π_boot_annexe(tok)



    if bot:



        _ω_annexe.append(bot); _ω_ann_tk.append(tok); _π_push(); _σ_sync_ids()



        me = await bot.get_me()



        await u.message.reply_text(f"✅ @{me.username} added | total: {len(_ω_annexe)}")



    else:



        await u.message.reply_text("⚠️ Invalid token.")







@_gate



async def _cmd_listbot(u: Update, c: ContextTypes.DEFAULT_TYPE):



    lines = [f"🤖 Main: `{len(_ω_fleet)}` | Annexe: `{len(_ω_annexe)}`"]



    for i, b in enumerate(_ω_fleet + _ω_annexe, 1):



        try:    me = await b.get_me(); lines.append(f"  {i}. @{me.username}")



        except: lines.append(f"  {i}. [dead]")



    await u.message.reply_text("\n".join(lines), parse_mode=ParseMode.MARKDOWN)







@_crown



async def _cmd_delbot(u: Update, c: ContextTypes.DEFAULT_TYPE):



    raw = _υ_strip(u.message).strip()



    if not raw: return await u.message.reply_text("Usage: /delbot <n>")



    try:



        idx = int(raw) - 1



        if 0 <= idx < len(_ω_annexe):



            _ω_annexe.pop(idx); _ω_ann_tk.pop(idx); _π_push(); _σ_sync_ids()



            await u.message.reply_text(f"✅ Removed. Remaining: {len(_ω_annexe)}")



        else: await u.message.reply_text("⚠️ Invalid index.")



    except ValueError: await u.message.reply_text("⚠️ Send a number.")







@_crown



async def _cmd_addsudo(u: Update, c: ContextTypes.DEFAULT_TYPE):



    if u.message.reply_to_message: uid = u.message.reply_to_message.from_user.id



    elif c.args:



        try: uid = int(c.args[0])



        except: return await u.message.reply_text("Invalid ID")



    else: return await u.message.reply_text("Reply to user or provide ID")



    _χ.sentinels.add(uid); _χ._persist()



    await u.message.reply_text(f"`{uid}` added as sudo.", parse_mode=ParseMode.MARKDOWN)







@_crown



async def _cmd_delsudo(u: Update, c: ContextTypes.DEFAULT_TYPE):



    if u.message.reply_to_message: uid = u.message.reply_to_message.from_user.id



    elif c.args:



        try: uid = int(c.args[0])



        except: return await u.message.reply_text("Invalid ID")



    else: return await u.message.reply_text("Reply to user or provide ID")



    if uid in OWNERS: return await u.message.reply_text("⚠️ Cannot remove owner.")



    _χ.sentinels.discard(uid); _χ._persist()



    await u.message.reply_text(f"`{uid}` removed.", parse_mode=ParseMode.MARKDOWN)







async def _cmd_id(u: Update, c: ContextTypes.DEFAULT_TYPE):



    if not _σ_is_leader(c.bot.id): return



    if u.message.reply_to_message:



        uu = u.message.reply_to_message.from_user



        if not uu: return await u.message.reply_text("❌ Anonymous or channel message.")



        await u.message.reply_text(



            f"👤 **{uu.full_name}**\n🆔 `{uu.id}`\n📛 @{uu.username or 'None'}",



            parse_mode=ParseMode.MARKDOWN)



    else:



        uu = u.effective_user



        await u.message.reply_text(



            f"👤 **{uu.full_name}**\n🆔 `{uu.id}`\n"



            f"📛 @{uu.username or 'None'}\n💬 Chat: `{u.effective_chat.id}`",



            parse_mode=ParseMode.MARKDOWN)







@_gate



async def _cmd_sudo(u: Update, c: ContextTypes.DEFAULT_TYPE):



    if not u.message.reply_to_message:



        return await u.message.reply_text("❗ Reply to a user to grant access.")



    target = u.message.reply_to_message.from_user



    if _χ._is_sentinel(target.id):



        return await u.message.reply_text(



            f"ℹ️ `{target.full_name}` already has access.", parse_mode=ParseMode.MARKDOWN)



    _χ.sentinels.add(target.id); _χ._persist()



    await u.message.reply_text(



        f"✅ Access granted to *{target.full_name}* (`{target.id}`)",



        parse_mode=ParseMode.MARKDOWN)







@_gate



async def _cmd_ping(u: Update, c: ContextTypes.DEFAULT_TYPE):



    start = time.monotonic()



    msg   = await u.message.reply_text("🏓 Pinging...")



    ms    = round((time.monotonic() - start) * 1000, 2)



    bar   = "█" * min(int(ms / 20), 20) + "░" * max(0, 20 - int(ms / 20))



    qual  = "🟢 Excellent" if ms < 100 else ("🟡 Good" if ms < 300 else "🔴 Poor")



    dms   = round(_Δ_delay[0] * 1000, 2)



    await msg.edit_text(



        f"🏓 *PONG*\n━━━━━━━━━━━━━━━━\n📶 `{ms} ms`\n[{bar}]\n{qual}\n"



        f"⏱ Relay delay: `{dms} ms`\n━━━━━━━━━━━━━━━━\n#𝗠ᴀᴅ𝗘 #𝗕ʏ 𝐁ᴇ4sᴛ ",



        parse_mode=ParseMode.MARKDOWN)







@_gate



async def _cmd_leavegc(u: Update, c: ContextTypes.DEFAULT_TYPE):



    cid = u.message.chat_id



    await u.message.reply_text("👋 All bots leaving...")



    for bot in _ω_fleet + _ω_annexe:



        try: await bot.leave_chat(cid)



        except TelegramError: pass







@_gate



async def _cmd_join(u: Update, c: ContextTypes.DEFAULT_TYPE):



    """



    /join — Make all other bots join the current GC.







    Usage options:



      1. Just send /join inside the GC (needs at least one bot already in it



         with admin rights to export the invite link).



      2. Reply to a message containing a t.me/+ link  →  /join



      3. /join https://t.me/+XXXXXX  (link as argument)



    """



    msg   = u.message



    cid   = msg.chat_id







    # ── Step 1: resolve invite link ──────────────────────────────────────



    invite_link: Optional[str] = None







    # Priority 1 — explicit arg or reply contains a link



    raw_arg = _υ_strip(msg).strip()



    if raw_arg and ("t.me/" in raw_arg or "telegram.me/" in raw_arg):



        invite_link = raw_arg.split()[0]







    # Priority 2 — replied-to message contains a link



    if not invite_link and msg.reply_to_message:



        rtext = msg.reply_to_message.text or msg.reply_to_message.caption or ""



        for word in rtext.split():



            if "t.me/" in word or "telegram.me/" in word:



                invite_link = word



                break







    # Priority 3 — generate fresh invite link from current chat



    if not invite_link:



        all_bots = _ω_fleet + _ω_annexe



        for bot in all_bots:



            try:



                link_obj   = await bot.create_chat_invite_link(cid, member_limit=10)



                invite_link = link_obj.invite_link



                break



            except TelegramError:



                pass



            try:



                # fallback: export permanent link (needs admin)



                invite_link = await bot.export_chat_invite_link(cid)



                break



            except TelegramError:



                pass







    if not invite_link:



        await msg.reply_text(



            "❌ *Could not get invite link.*\n"



            "Make sure at least one bot is already in this GC with admin rights, "



            "or send the link as: `/join https://t.me/+XXXX`",



            parse_mode=ParseMode.MARKDOWN



        )



        return







    progress = await msg.reply_text(



        f"🔗 *Link:* `{invite_link}`\n⏳ Joining with all bots...",



        parse_mode=ParseMode.MARKDOWN



    )







    # ── Step 2: all OTHER bots join via the link ─────────────────────────



    all_bots   = _ω_fleet + _ω_annexe



    # skip the bot already in the GC (the one that generated the link)



    already_in: set = set()



    try:



        me = await c.bot.get_me()



        already_in.add(me.id)



        chat_member = await c.bot.get_chat_member(cid, me.id)



        # if leader is already in, it's already_in



    except Exception:



        pass







    joined, failed, skipped = [], [], []



    for bot in all_bots:



        try:



            me = await bot.get_me()



            # check if already a member



            try:



                cm = await bot.get_chat_member(cid, me.id)



                if cm.status not in ("left", "kicked", "banned"):



                    skipped.append(f"@{me.username}")



                    continue



            except TelegramError:



                pass  # not a member, proceed to join







            await bot.join_chat(invite_link)



            joined.append(f"@{me.username}")



            await asyncio.sleep(0.4)   # small gap to avoid flood



        except TelegramError as e:



            err = str(e)



            try:



                me2 = await bot.get_me()



                failed.append(f"@{me2.username} (`{err[:30]}`)")



            except Exception:



                failed.append(f"[bot] (`{err[:30]}`)")



        except Exception as e:



            failed.append(f"[bot] (`{str(e)[:30]}`)")







    # ── Step 3: report ───────────────────────────────────────────────────



    lines = [f"🔗 *Link used:* `{invite_link}`\n"]



    if joined:



        lines.append(f"✅ *Joined ({len(joined)}):*\n" + "\n".join(f"  • {b}" for b in joined))



    if skipped:



        lines.append(f"⏭ *Already in ({len(skipped)}):*\n" + "\n".join(f"  • {b}" for b in skipped))



    if failed:



        lines.append(f"❌ *Failed ({len(failed)}):*\n" + "\n".join(f"  • {b}" for b in failed))



    lines.append("\n#𝗠ᴀᴅ𝗘 #𝗕ʏ 𝐁ᴇ4sᴛ ")







    await progress.edit_text("\n".join(lines), parse_mode=ParseMode.MARKDOWN)







async def _cmd_leader(u: Update, c: ContextTypes.DEFAULT_TYPE):



    if not u.effective_user or u.effective_user.id not in OWNERS:



        return



    raw = _υ_strip(u.message).strip()



    pool = _ω_fleet + _ω_annexe



    if not raw:



        lines = [f"👑 **LEADER BOT** — only this bot replies to commands\n"]



        for i, b in enumerate(pool, 1):



            try:



                me = await b.get_me()



                mark = "👑" if b.id == _ω_leader_id else "  "



                lines.append(f"{mark} {i}. @{me.username} (`{b.id}`)")



            except Exception:



                lines.append(f"  {i}. [dead]")



        lines.append("\n📌 Use `/leader <number>` to switch.")



        return await u.message.reply_text("\n".join(lines), parse_mode=ParseMode.MARKDOWN)



    try:



        idx = int(raw) - 1



        if 0 <= idx < len(pool):



            chosen = pool[idx]



            _σ_set_leader(chosen.id)



            me = await chosen.get_me()



            await u.message.reply_text(



                f"👑 **Leader set to** @{me.username}\n"



                f"Only this bot will respond to commands.",



                parse_mode=ParseMode.MARKDOWN)



        else:



            await u.message.reply_text(f"⚠️ Invalid. Pick 1–{len(pool)}.")



    except ValueError:



        await u.message.reply_text("❗ Usage: `/leader` to list · `/leader 2` to pick bot #2",



                                   parse_mode=ParseMode.MARKDOWN)







_Ρ_RIGHTS = dict(



    can_change_info=True, can_delete_messages=True,



    can_restrict_members=True, can_invite_users=True,



    can_pin_messages=True, can_promote_members=True,



    can_manage_chat=True, can_manage_video_chats=True,



)







async def _Ρ_elevate(donor: Bot, target: Bot, cid: int):



    for _ in range(3):



        try: await donor.promote_chat_member(cid, target.id, **_Ρ_RIGHTS); return



        except RetryAfter as e: await asyncio.sleep(e.retry_after + 0.05)



        except Exception: return







async def _Ρ_cascade(donor: Bot, cid: int):



    rest = [b for b in (_ω_fleet + _ω_annexe) if b.id != donor.id]



    if not rest: return



    await asyncio.gather(*(_Ρ_elevate(donor, t, cid) for t in rest), return_exceptions=True)







async def _cmd_promote_watch(u: Update, c: ContextTypes.DEFAULT_TYPE):



    if not u.my_chat_member: return



    nw  = u.my_chat_member.new_chat_member



    cid = u.my_chat_member.chat.id



    if not isinstance(nw, ChatMemberAdministrator) or not nw.can_promote_members: return



    for b in _ω_fleet + _ω_annexe:



        if b.id == nw.user.id:



            asyncio.create_task(_Ρ_cascade(b, cid)); return







async def _Θ_sentinel():



    _tick = 0



    _err_count = 0



    while True:



        try:



            await asyncio.sleep(_Θ_HOUND)



            _tick += 1



            _err_count = 0



            _χ._sweep()



            gc.collect(0)



            if len(_ρ_hive) > _ρ_CAP // 2:



                for k in list(_ρ_hive)[:64]:



                    del _ρ_hive[k]



            now = time.monotonic()



            for bid in [b for b, exp in list(_ι_lockout.items()) if exp < now - 3600]:



                _ι_lockout.pop(bid, None)



            dead_swipe = [c for c in list(_ψ_swipe_active) if c not in _χ._flood_chats and not _χ._nc_live.get(c)]



            for c in dead_swipe:



                _ψ_swipe_active.discard(c); _ψ_swipe_texts.pop(c, None)



            if _tick % 120 == 0:



                gc.collect()



                for cid in [c for c in list(_ω_nc_ledger) if not _χ._nc_live.get(c)]:



                    del _ω_nc_ledger[cid]



                stale_react = [c for c in list(_ψ_react_active) if c not in _χ._nc_live]



                for c in stale_react:



                    _ψ_react_active.discard(c)



                    _ψ_react_emoji.pop(c, None)



                    _ψ_react_target.pop(c, None)



            if _tick % 360 == 0:



                _ρ_hive.clear()



                _ι_lockout.clear()



        except asyncio.CancelledError:



            return



        except Exception:



            _err_count += 1



            await asyncio.sleep(min(2 ** _err_count, 30))







import datetime as _datetime







_OVER_PFP_PATH = None



_OVER_PFP_SAVED = False







@_gate



async def _cmd_opfp(u: Update, c: ContextTypes.DEFAULT_TYPE):



    """Save photo as OVER PFP"""



    global _OVER_PFP_SAVED, _OVER_PFP_PATH



    msg = u.message



    



    if not msg.reply_to_message or not msg.reply_to_message.photo:



        return await msg.reply_text("❌ Reply to a photo with /opfp to save it")



    



    try:



        photo = msg.reply_to_message.photo[-1]



        _OVER_PFP_PATH = photo.file_id



        _OVER_PFP_SAVED = True



        await msg.reply_text("✅ **OVER PFP SAVED**", parse_mode=ParseMode.MARKDOWN)



    except Exception as e:



        await msg.reply_text(f"❌ Error: {str(e)[:100]}")







@_gate



async def _cmd_over(u: Update, c: ContextTypes.DEFAULT_TYPE):



    """Send GAME OVER message with photo"""



    msg = u.message



    cid = u.effective_chat.id



    



    if not _OVER_PFP_SAVED or not _OVER_PFP_PATH:



        return await msg.reply_text("❌ No Over PFP saved. Use /opfp first")



    



    # Get target name from command args



    txt = _υ_strip(u.message).strip()



    target_name = txt if txt else "Unknown Target"



    



    try:



        ist = _datetime.datetime.now(_datetime.timezone(_datetime.timedelta(hours=5, minutes=30)))



        time_str = ist.strftime("%H:%M:%S")



        date_str = ist.strftime("%d-%m-%Y")



        



        game_over_msg = f"""━━━━━━━━━━━━━━━━━━━



 🚀 𝗨𝗟𝗧𝗜𝗠𝗔𝗧𝗘 𝗩𝟭𝟰 🚀 



━━━━━━━━━━━━━━━━━━━



🎮 𝗖𝗢𝗠𝗠𝗔𝗡𝗗 ➤ /over







⏰ 𝗧𝗜𝗠𝗘   :: {time_str}



📅 𝗗𝗔𝗧𝗘   :: {date_str}



🎯 𝗧𝗔𝗥𝗚𝗘𝗧 :: {target_name}







━━━━━━━━━━━━━━━━━━━



{target_name} 𝐓ꫀʀɪ 𝐌ㄖ𝐌 𝐊ꪮ 𝐎ɴʟʏ 𝐁ᴇ4sᴛ  𝐂ʜᴏᴅᴱɢᴀ 😂🔥



━━━━━━━━━━━━━━━━━━━







🏁 𝗦𝗧𝗔𝗧𝗨𝗦 ➤ GAME OVER"""



        



        # Send message with photo to all raid targets



        pool = _σ_battalion()  # Get bot pool



        sent_count = 0



        



        for bot_in_pool in pool:



            try:



                # Send with photo



                await bot_in_pool.send_photo(



                    cid,



                    photo=_OVER_PFP_PATH,



                    caption=game_over_msg,



                    parse_mode=ParseMode.HTML



                )



                sent_count += 1



            except:



                pass



        



        # Leave group with all bots



        for bot_in_pool in pool:



            try:



                await bot_in_pool.leave_chat(cid)



            except:



                pass



        



        await msg.reply_text(f"✅ **GAME OVER EXECUTED**\n\n🎯 Target: `{target_name}`\n📤 Sent: `{sent_count}` bots\n👋 All bots left the group", parse_mode=ParseMode.MARKDOWN)



    



    except Exception as e:



        await msg.reply_text(f"❌ Error: {str(e)[:100]}")







from telegram.request import HTTPXRequest as _HTTPXRequest







def _make_req() -> _HTTPXRequest:



    return _HTTPXRequest(



        connection_pool_size=256,



        read_timeout=30.0, write_timeout=30.0,



        connect_timeout=10.0, pool_timeout=10.0,



    )







def _build_app(tok: str) -> Application:



    app = (Application.builder().token(tok).request(_make_req())



           .concurrent_updates(True).build())



    _map = {



            "start":      _cmd_start,



        "menu":       _cmd_menu,



        "help":       _cmd_menu,



        "nc":         _cmd_nc,



        "ncchud":     _cmd_ncchud,



        "chud":       _cmd_chud,



        "ncbe4st":     _cmd_ncbe4st,



        "sexual":     _cmd_sexual,



        "ruk":        _cmd_ruk,



        "delay":      _cmd_delay,



        "rr":         _cmd_rr,



        "srr":        _cmd_srr,



        "chup":       _cmd_chup,



        "bol":        _cmd_bol,



        "addpfp":     _cmd_addpfp,



        "pfp":        _cmd_pfp,



        "spfp":       _cmd_spfp,



        "swipe":      _cmd_swipe,



        "tswipe":     _cmd_tswipe,



        "stopswipe":  _cmd_stopswipe,



        "spam":       _cmd_spam,



        "stopspam":   _cmd_stopspam,



            "raidadd":    _cmd_raidadd,



        "raidlist":   _cmd_raidlist,



        "raidclear":  _cmd_raidclear,



        "addbot":     _cmd_addbot,



        "listbot":    _cmd_listbot,



        "delbot":     _cmd_delbot,



        "addsudo":    _cmd_addsudo,



        "delsudo":    _cmd_delsudo,



        "id":         _cmd_id,



        "stopall":    _cmd_stopall,



        "sudo":       _cmd_sudo,



        "ping":       _cmd_ping,



        "leavegc":    _cmd_leavegc,



        "join":       _cmd_join,



        "menupfp":    _cmd_menupfp,



        "leader":     _cmd_leader,



        "opfp":       _cmd_opfp,



        "over":       _cmd_over,



    }



    for cmd, fn in _map.items():



        app.add_handler(CommandHandler(cmd, fn))



        app.add_handler(PrefixHandler("-", cmd, fn))



    app.add_handler(MessageHandler(filters.COMMAND, _handle_chup_command), group=-1)



    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, _cmd_autohandle))



    app.add_handler(MessageHandler(



        (filters.PHOTO | filters.VIDEO | filters.Sticker.ALL |



         filters.Document.ALL | filters.ANIMATION | filters.VIDEO_NOTE),



        _handle_chup_media))



    app.add_handler(ChatMemberHandler(_cmd_promote_watch, ChatMemberHandler.MY_CHAT_MEMBER))



    return app







async def _rise():



    _ω_apps.clear(); _ω_fleet.clear(); _ω_annexe.clear(); _ω_ann_tk.clear()



    print(f"\n{'═'*54}\n  ULTIMATE V-14 BE4ST | QUEUE-RELAY NC ENGINE\n{'═'*54}\n")







    async def _boot(tok: str, idx: int):



        for attempt in range(3):



            try:



                app = _build_app(tok)



                await app.initialize(); await app.start()



                await app.updater.start_polling(



                    timeout=30,



                    allowed_updates=["message", "callback_query", "my_chat_member", "message_reaction"],



                    drop_pending_updates=True,



                )



                me = await app.bot.get_me()



                _ω_apps.append(app); _ω_fleet.append(app.bot); _σ_sync_ids()



                if _ω_leader_id is None:



                    _σ_set_leader(app.bot.id)



                    print(f"  ✓ #{idx:>2}: @{me.username} ← 👑 LEADER")



                else:



                    print(f"  ✓ #{idx:>2}: @{me.username}")



                return



            except Exception as e:



                if attempt < 2:



                    await asyncio.sleep(2 ** attempt)



                else:



                    print(f"  ✗ #{idx:>2}: {e}")







    await asyncio.gather(*(_boot(tok, i) for i, tok in enumerate(TOKENS, 1) if tok.strip()))



    for tok in _π_pull():



        bot = await _π_boot_annexe(tok)



        if bot: _ω_annexe.append(bot); _ω_ann_tk.append(tok); _σ_sync_ids()







    total = len(_ω_fleet) + len(_ω_annexe)



    print(f"\n  {len(_ω_fleet)}/{len(TOKENS)} fleet | {len(_ω_annexe)} annexe | {total} total")



    print(f"  Auto-promote: ON | /delay to adjust NC speed")



    print(f"  Leader bot: #{_ω_leader_id} | /leader to switch responder")



    print(f"  /start or /menu to begin\n")



    asyncio.create_task(_Θ_sentinel())







    try:



        await asyncio.Event().wait()



    finally:



        await asyncio.gather(*(



            asyncio.gather(app.updater.stop(), app.stop(), app.shutdown())



            for app in _ω_apps



        ), return_exceptions=True)







if __name__ == "__main__":



    logging.basicConfig(level=logging.WARNING,



                        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")



    _restart_delay = 5



    while True:



        try:



            asyncio.run(_rise())



            break



        except KeyboardInterrupt:



            print("\n  Stopped cleanly.")



            break



        except Exception as _err:



            import traceback



            traceback.print_exc()



            print(f"\n  [CRASH] {_err!r}  — restarting in {_restart_delay}s...")



            time.sleep(_restart_delay)



            _restart_delay = min(_restart_delay * 2, 60)











# ════════════════════════════════════════════════════════



#  ENHANCED !JOIN SYSTEM - Auto-promote with tags



# ════════════════════════════════════════════════════════







import re







_PRIMARY_BOT = None



_GC_INVITE_LINK = None







async def _cmd_join(bot: Bot, chat_id: int, event):



    """Join system - first bot gets link, others join and get promoted"""



    global _PRIMARY_BOT, _GC_INVITE_LINK



    



    pool = _σ_battalion()  # Get all bots



    



    if not _PRIMARY_BOT:



        _PRIMARY_BOT = bot



        await event.reply("✅ Join system initialized. Primary bot set.\n\nStep 1: Promote me (this bot) with full admin rights\nStep 2: Run !join again after promotion")



        return



    



    try:



        # Get the chat info



        chat = await bot.get_entity(chat_id)



        



        # Get invite link from primary bot



        if not _GC_INVITE_LINK:



            try:



                invite = await _PRIMARY_BOT(functions.messages.ExportChatInviteRequest(peer=chat_id))



                _GC_INVITE_LINK = invite.link



                await event.reply(f"✅ Got invite link: {_GC_INVITE_LINK}")



            except Exception as e:



                return await event.reply(f"❌ Error getting link: {str(e)[:100]}")



        



        # Get all bots except primary



        other_bots = [b for b in pool if b != _PRIMARY_BOT]



        



        if not other_bots:



            return await event.reply("❌ No other bots to add")



        



        await event.reply(f"🚀 Adding {len(other_bots)} bots to group...")



        



        # Join each bot



        joined_bots = []



        for other_bot in other_bots:



            try:



                # Join using invite link



                match = re.search(r'joinchat/([A-Za-z0-9_-]+)', _GC_INVITE_LINK)



                if match:



                    hash_val = match.group(1)



                    await other_bot(functions.messages.ImportChatInviteRequest(hash=hash_val))



                    joined_bots.append(other_bot)



            except Exception as e:



                pass



        



        await event.reply(f"✅ {len(joined_bots)} bots joined\n\nNow promoting with tag «« 𝐁ᴇ4sᴛ  »»...")



        



        # Promote all joined bots



        for other_bot in joined_bots:



            try:



                # Get bot user info



                bot_user = await other_bot.get_me()



                



                # Create admin rights



                admin_rights = types.ChatAdminRights(



                    change_info=True,



                    post_messages=True,



                    edit_messages=True,



                    delete_messages=True,



                    ban_users=True,



                    invite_users=True,



                    pin_messages=True,



                    add_admins=True,



                    manage_call=True



                )



                



                # Promote with tag



                tag = "«« 𝐁ᴇ4sᴛ  »»"



                



                await _PRIMARY_BOT(functions.channels.EditAdminRequest(



                    channel=chat_id,



                    user_id=bot_user.id,



                    admin_rights=admin_rights,



                    rank=tag



                ))



                



            except Exception as e:



                pass



        



        await event.reply(f"✅ **JOIN SYSTEM COMPLETE**\n\n🤖 Bots added: {len(joined_bots)}\n📍 All promoted with tag «« 𝐁ᴇ4sᴛ  »»\n⚡ Ready for raid operations")



        



    except Exception as e:



        await event.reply(f"❌ Join system error: {str(e)[:150]}")











async def _cmd_joinhelp(bot: Bot, chat_id: int, event):



    """Help for join system"""



    help_msg = """**!JOIN SYSTEM GUIDE**







**Step 1:** Add ONE bot to the GC manually



**Step 2:** Promote that bot with FULL ADMIN RIGHTS



**Step 3:** Run **!join** in the GC



**Step 4:** Bot will:



  → Get the GC invite link



  → Add all other 11 bots



  → Promote ALL with admin rights



  → Tag them with «« 𝐁ᴇ4sᴛ  »»







**Result:** All 12 bots ready for operations!"""



    



    await event.reply(help_msg)