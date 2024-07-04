from dataclasses import dataclass

from model.Album import Album


@dataclass
class Connessione:
    v1: Album
    v2: Album
    #peso: int

    def __str__(self):
        return (f"Arco: {self.v1.albumId} - "
                f"{self.v2.albumId}")