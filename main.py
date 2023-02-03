class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def play_songs(self):
        for song in self.songs:
            print(f"Playing song: {song}")

class PopPlaylist(Playlist):
    def __init__(self):
        super().__init__(["Shape of You - Ed Sheeran", "Girls Like You - Maroon 5", "Sugar - Maroon 5"])

class HipHopPlaylist(Playlist):
    def __init__(self):
        super().__init__(["I Gotta Feeling - Black Eyed Peas", "Can't Hold Us - Macklemore & Ryan Lewis", "Kiss - Prince"])

class RockPlaylist(Playlist):
    def __init__(self):
        super().__init__(["Bohemian Rhapsody - Queen", "Stairway to Heaven - Led Zeppelin", "Sweet Child o' Mine - Guns N' Roses"])

class ElectronicPlaylist(Playlist):
    def __init__(self):
        super().__init__(["Levels - Avicii", "Summertime Sadness - Lana Del Rey", "Adrenaline - Moby"])

class JazzPlaylist(Playlist):
    def __init__(self):
        super().__init__(["Take the A Train - Duke Ellington", "In a Sentimental Mood - Duke Ellington", "Misty - Erroll Garner"])

class BluesPlaylist(Playlist):
    def __init__(self):
        super().__init__(["Sweet Home Chicago - Robert Johnson", "Crossroads - Robert Johnson", "Hellhound on My Trail - Robert Johnson"])

class CountryPlaylist(Playlist):
    def __init__(self):
        super().__init__(["Don't Stop Believin' - Journey", "Living on a Prayer - Bon Jovi", "Walking on Sunshine - Katrina and The Waves"])

# Usage example:
pop_playlist = PopPlaylist()
pop_playlist.play_songs()

hip_hop_playlist = HipHopPlaylist()
hip_hop_playlist.play_songs()

rock_playlist = RockPlaylist()
rock_playlist.play_songs()

electronic_playlist = ElectronicPlaylist()
electronic_playlist.play_songs()

jazz_playlist = JazzPlaylist()
jazz_playlist.play_songs()

blues_playlist = BluesPlaylist()
blues_playlist.play_songs()

country_playlist = CountryPlaylist()
country_playlist.play_songs()

