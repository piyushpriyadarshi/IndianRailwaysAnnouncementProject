import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS


def generateSkeleton():
    # 1 generating kripya dhyan dijiye
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 88000
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("dhyandijiye_hindi.mp3", format="mp3")
    # 2 generating from city

    # 3 generate se chalkar
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("sechalkar_hindi.mp3", format="mp3")
    # 4 generate via city

    # 5 generate ke raste
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("keraste_hindi.mp3", format="mp3")
    # 6 generate to city

    # 7 generate ko jane wali
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("kojanewaligadi_hindi.mp3", format="mp3")

    # 8 generate Train No and Name

    # 9 generate Kuch hi samy me platform shankhya
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("kuchhisamayme_hindi.mp3", format="mp3")
    # 10 generate Platform No

    # 11 generate aa rahi h
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 109000
    finish = 112050
    audioProcessed = audio[start:finish]
    audioProcessed.export("aarahih_hindi.mp3", format="mp3")
    pass


def generateAnnouncement(filenName):
    df = pd.read_excel(filenName)
    print(df)
    for index, item in df.iterrows():
        print(item)

    pass


if __name__ == "__main__":
    print("Generating Skeleton ......")
    generateSkeleton()
    generateAnnouncement("announce_hindi.xlsx")
