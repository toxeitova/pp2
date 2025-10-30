import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

songs = ["music/song1.mp3", "music/song2.mp3", "music/song3.mp3"]
current = 0
stopped = False

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

pygame.mixer.music.load(songs[current])
pygame.mixer.music.play()
print("Play:", songs[current])

cnt = 0
while True:
    if cnt % 100 == 0:
        print(cnt)

    screen.fill((100, 100, 200))
    pygame.display.update()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.load(songs[current])
                pygame.mixer.music.play()
                stopped = False
                print("Play:", songs[current])

            if event.key == pygame.K_s:
                pygame.mixer.music.stop()
                stopped = True
                print("Stop")

            if event.key == pygame.K_n:
                current = (current + 1) % len(songs)
                pygame.mixer.music.load(songs[current])
                pygame.mixer.music.play()
                stopped = False
                print("Next:", songs[current])

            if event.key == pygame.K_p:
                current = (current - 1) % len(songs)
                pygame.mixer.music.load(songs[current])
                pygame.mixer.music.play()
                stopped = False
                print("Previous:", songs[current])

            if event.key == pygame.K_ESCAPE:
                exit(0)

        if event.type == SONG_END and not stopped:
            current = (current + 1) % len(songs)
            pygame.mixer.music.load(songs[current])
            pygame.mixer.music.play()
            print("Song ended! Now playing:", songs[current])

    cnt += 1
