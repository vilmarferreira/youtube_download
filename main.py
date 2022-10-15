import youtube_dl

input_link = input("Insira o link do vídeo:")

link = [input_link]

with youtube_dl.YoutubeDL() as ydl:
    ydl.download(link)
