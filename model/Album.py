from dataclasses import dataclass

@dataclass
class Album:
    albumId: int
    title: str
    artistId: int

    def __hash__(self):
        return hash(self.albumId)

    def __str__(self):
        return f"{self.title}"


