import youtube_dl

url = [input("Insira o link do vídeo: ")]

with youtube_dl.YoutubeDL() as ydl:
    if "shorts" in url[0]:
        url[0] = url[0].replace("shorts/", "watch?v=")
        ydl.download(url)
    else:
        ydl.download(url)
