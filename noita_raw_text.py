from utils import catch_unique

text_1 = "Keskikesän kuikka lenteli suon yllä ja laskeutui suuren puun juurelle. " \
         "Vesilintu muni kolme munaa. " \
         "Ensimmäinen munista vierähti pesästä ja halkesi. " \
         "Halkeamasta vuosi verta seitsemän päivää ja seitsemän yötä. " \
         "Verestä muodostui elämä ja kuolema."

text_2 = "Valkuainen valui länteen ja siitä " \
         "muodostui kylmyys ja jää. Kuoresta " \
         "muodostuivat maat ja vuoret."

text_3 = "Keltuainen valui itään ja " \
         "siitä muodostui lämpö ja tuli."

text_4 = "Viimein munasta kuoriutui Luonto. " \
         "Luonto loi lait luonnon, asetti eläimet, " \
         "niityt, joet, kummut ja vuoret."

text_5 = "Yötä ja päivää vierähti kertaa. " \
         "Luonto puuhasteli itsekseen. Luonto " \
         "katseli tekojaan ja oli tyytyväinen " \
         "luomuksiinsa. Maailmassa oli harmonia."

text_6 = "Toinen munista kuoriutui ja sieltä syntyi " \
         "Taikuus. Taikuus katseli Luonnon luomuksia " \
         "ja antoi niille sielun. Ei pelkästään " \
         "eläimille, vaan myös aineille."

text_7 = "Sielun paino jalosti ja kieroutti luonnon " \
         "luomuksia. Kullan jalous antoi sille hohdon. " \
         "Mudan saamattomuus antoi sille pistävän hajun."

text_8 = "Taikuus rikkoi luonnon lakeja. Luonto " \
         "ja Taikuus alkoivat riidellä siitä " \
         "miten maailman kuuluisi olla."

text_9 = "Munista viimeinen kuoriutui ja sieltä " \
         "syntyi teknologia. Teknologia antoi luonnon " \
         "eläimille kyvyn käyttää koneita ja laitteita."

def get_all_noita_text():
    return (text_1+" "+text_2+" "+text_3+" "+text_4+" "+text_5+" "+text_6+" "+text_7+" "+text_8+" "+text_9).upper()

def get_noita_text_as_list():
    text =  get_all_noita_text().upper()
    text = text.replace('.','')
    text = text.replace(',','')
    text = text.replace('\n', '')

    list_word = text.split(' ')
    list_word.sort()
    return list_word
