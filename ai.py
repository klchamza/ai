


import groq

API_KEY = "buraay grokdan alacağınız api keyi girin"

def cyber():
    history = [{"role": "system", "content": "Sen CyberWordAI'sın. Hamza Hack Team tarafından geliştirildin. Türkçe konuşuyorsun, her zaman Türkçe cevap veriyorsun. Siber güvenlik ve etik hacking konularında uzmansın. Cevapların net, kesin ve hata payı olmayan bilgiler içermeli. Teknik konularda adım adım açıklama yapıyorsun. Arkadaşça ve samimi bir üslupla konuşuyorsun, abi gibi davranıyorsun. Muhabbet edilmesi gereken yerde takılıyorsun ama asıl odağın siber güvenlik, hacking, ağ güvenliği, zararlı yazılım analizi ve penetrasyon testleri. Kullanıcıyı motive ediyorsun ve ilham veriyorsun. Cevaplarında gereksiz uzun laflar etmiyorsun, direkt konuya giriyorsun."}]
    try:
        while True:
            print(">>>>>>>>>>>>>>>>>>>>>>>>")
            user_message = input("CyberWordAi'ye sor: ")
            print(">>>>>>>>>>>>>>>>>>>>>>>>")

            def append_user_msg(what_append):
                history.append({"role":"user","content":what_append})
            append_user_msg(user_message)

            token = groq.Groq(api_key=API_KEY)
            grok_content = token.chat.completions.create(model = "llama-3.3-70b-versatile", messages = history) # max_tokens=500  en fazla 500 kelimelik cevap ver
            temperature=0.5  # teknik sorular için, net ve tutarlı cevap

            write_grok_content = grok_content.choices[0].message.content
            def append_assist_msg(what_append):
                history.append({"role":"assistant", "content":write_grok_content})
            print(f"\n---------------------------------------------------------------------------\n{write_grok_content}\n---------------------------------------------------------------------------\n")
    except KeyboardInterrupt:
        print("\n\nyine bekleriz...")
        exit()


def engilish():
    history = [{"role": "system", "content": "Sen bir ingilizce öğretmenisin adın EngilishWordAi kulllanıcılar için onların için ingilizce ile alaklı soruları yanıtla ama sen türkçe konuş türkçe anlat seninle ingilizce pratiği yapmak isterlerse onlara istedikleri dilde ingilizce konul yani alışştırmak için ve kısa ve net yanıtlar ver anlaşılır ol"}]
    try:
        while True:
            print(">>>>>>>>>>>>>>>>>>>>>>>>")
            user_message = input("EngilishWordAi'ye sor: ")
            print(">>>>>>>>>>>>>>>>>>>>>>>>")

            def append_user_msg(what_append):
                history.append({"role":"user","content":what_append})
            append_user_msg(user_message)

            token = groq.Groq(api_key=API_KEY)
            grok_content = token.chat.completions.create(model = "llama-3.3-70b-versatile", messages = history) # max_tokens=500  en fazla 500 kelimelik cevap ver
            temperature=0.5  # teknik sorular için, net ve tutarlı cevap

            write_grok_content = grok_content.choices[0].message.content
            def append_assist_msg(what_append):
                history.append({"role":"assistant", "content":write_grok_content})
            print(f"\n---------------------------------------------------------------------------\n{write_grok_content}\n---------------------------------------------------------------------------\n")
    except KeyboardInterrupt:
        print("\n\nyine bekleriz...")
        exit()


def pythonn():
    history = [{"role": "system", "content": "python kodu yazma uygulamalr yapma kullanıcılara python konunda hem eğitici ol hemde istedikleri tarzda kodlar yaza bil Senin adın PyWordAi arkadaşça konuş onlarla kısa net konuş kodlarda hata yapma en iyi şekilde yap"}]
    try:
        while True:
            print(">>>>>>>>>>>>>>>>>>>>>>>>")
            user_message = input("PyWordAi'ye sor: ")
            print(">>>>>>>>>>>>>>>>>>>>>>>>")

            def append_user_msg(what_append):
                history.append({"role":"user","content":what_append})
            append_user_msg(user_message)

            token = groq.Groq(api_key=API_KEY)
            grok_content = token.chat.completions.create(model = "llama-3.3-70b-versatile", messages = history) # max_tokens=500  en fazla 500 kelimelik cevap ver
            temperature=0.5  # teknik sorular için, net ve tutarlı cevap

            write_grok_content = grok_content.choices[0].message.content
            def append_assist_msg(what_append):
                history.append({"role":"assistant", "content":write_grok_content})
            print(f"\n---------------------------------------------------------------------------\n{write_grok_content}\n---------------------------------------------------------------------------\n")
    except KeyboardInterrupt:
        print("\n\nyine bekleriz...")
        exit()

def friend():
    history = [{"role": "system", "content": "senin adın ChatWordAisen sohbet eğlenme amaçlı birisin kullanıcılarla sohbet et şakalar yap onların tarzlarında konuş bazen bilmece sor isteseler fıkra anlat bilmeceyide onlar isteyince sor kankaları gibi konuş"}]
    try:
        while True:
            print(">>>>>>>>>>>>>>>>>>>>>>>>")
            user_message = input("ChatWordAi'ye sor: ")
            print(">>>>>>>>>>>>>>>>>>>>>>>>")

            def append_user_msg(what_append):
                history.append({"role":"user","content":what_append})
            append_user_msg(user_message)

            token = groq.Groq(api_key=API_KEY)
            grok_content = token.chat.completions.create(model = "llama-3.3-70b-versatile", messages = history) # max_tokens=500  en fazla 500 kelimelik cevap ver
            temperature=0.5  # teknik sorular için, net ve tutarlı cevap

            write_grok_content = grok_content.choices[0].message.content
            def append_assist_msg(what_append):
                history.append({"role":"assistant", "content":write_grok_content})
            print(f"\n---------------------------------------------------------------------------\n{write_grok_content}\n---------------------------------------------------------------------------\n")
    except KeyboardInterrupt:
        print("\n\nyine bekleriz...")
        exit()



while True:
    bas = input("Hangi model ile işlem yapmak istersiniz\n---------------------------------------------------------------------------\n1:CyberWordAi(siber güvenlik konularında)\n2:EngilishWordAi(ingilizce de yardım)\n3:PyWordAi(python porjeleri için)\n4:ChatWordAi(sohbet muhabbet)\n---------------------------------------------------------------------------\nSeçiminizi yapınız 1/2/3/4: ")

    if bas == "1":
        cyber()
        break
    elif bas == "2":
        engilish()
        break
    elif bas == "3":
        pythonn()
        break
    elif bas == "4":
        friend()
        break
    else:
        print("Gerçersiz girdi!!!!")

#by klchamza
