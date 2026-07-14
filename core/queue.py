from collections import deque

class MusicQueue:
    def __init__(self):
        self.queue = deque()

    def ekle(self, song):
        self.queue.append(song)

    def sonraki(self):
        if self.queue:
            return self.queue.popleft()
        return None

    def liste(self):
        return list(self.queue)

    def temizle(self):
        self.queue.clear()

    def bos_mu(self):
        return len(self.queue) == 0

music_queue = MusicQueue()