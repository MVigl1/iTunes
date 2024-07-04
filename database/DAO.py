from database.DB_connect import DBConnect
from model.Album import Album
from model.connessioni import Connessione


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllObjects(durata):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select a.AlbumId as albumId, a.Title as title, a.ArtistId as artistId, sum(t.Milliseconds) as durata
                    from itunes.album a, itunes.track t 
                    where a.AlbumId = t.AlbumId
                    group by a.AlbumId"""

        cursor.execute(query, ())

        for row in cursor:
            if(int(row["durata"])>durata):
                result.append(Album(row["albumId"],
                                    row["title"],
                                    row["artistId"]))


        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioni(idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct t1.AlbumId as a1, t2.AlbumId as a2
                    from itunes.playlisttrack p1 , itunes.playlisttrack p2, itunes.track t1, itunes.track t2
                    where p1.trackId=t1.trackId and 
                    p2.trackId=t2.trackId and 
                    p1.playlistId = p2.playlistId and 
                    t1.AlbumId<t2.AlbumId  """

        cursor.execute(query, ())

        for row in cursor:
            if(row["a1"] in idMap and row["a2"] in idMap):
                result.append(Connessione(idMap[row["a1"]],
                                          idMap[row["a2"]]))
            else:
                pass

        cursor.close()
        conn.close()
        return result


