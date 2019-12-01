'''
Given a map Map<String, List<String>> userSongs with user names as keys and a 
list of all the songs that the user has listened to as values.
Also given a map Map<String, List<String>> songGenres, with song genre as keys 
and a list of all the songs within that genre as values. The song can only 
belong to only one genre.
The task is to return a map Map<String, List<String>>, where the key is a user 
name and the value is a list of the user's favorite genre(s). Favorite genre is
 the most listened to genre. A user can have more than one favorite genre if 
 he/she has listened to the same number of songs per each of the genres.

Example 1:
Input:
userSongs = {  
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
},
songGenres = {  
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}
Output: {  
   "David": ["Rock", "Techno"],
   "Emma":  ["Pop"]
}
Explanation:
David has 2 Rock, 2 Techno and 1 Jazz song. So he has 2 favorite genres.
Emma has 2 Pop and 1 Dubstep song. Pop is Emma's favorite genre.
'''

def initialize():
    userSongs = {  
       "David": ["song1", "song2", "song3", "song4", "song8"],
       "Emma":  ["song5", "song6", "song7"]
    }
    songGenres = {  
       "Rock":    ["song1", "song3"],
       "Dubstep": ["song7"],
       "Techno":  ["song2", "song4"],
       "Pop":     ["song5", "song6"],
       "Jazz":    ["song8", "song9"]
    }
    return userSongs, songGenres

class Solution:
    def favGenres(self, userSongs, songGenres):
        favGenre = {}
        generDict = {}
        songDict = {}

        # When userSongs is empty. userSongs = {}
        # return empty dict {}
        if not userSongs:
            return favGenre

        # When songGenres is empty. songGenres = {} 
        # return {user: []}
        # eg. {'David': [], 'Emma': []} 
        if not songGenres:
            for key in userSongs:
                del userSongs[key][:]
            return userSongs
        
        # Creat generDict = {gener: 0}
        # eg. {'Rock': 0, 'Dubstep': 0, 'Techno': 0, 'Pop': 0, 'Jazz': 0}
        for gener in songGenres:
            generDict[gener] = 0

        # print("generDict ", generDict)

        # Creat songDict = {song: gener}
        # eg. {'song1': 'Rock', 'song3': 'Rock', 'song7': 'Dubstep', 
        # 'song2': 'Techno', 'song4': 'Techno', 'song5': 'Pop', 
        # 'song6': 'Pop', 'song8': 'Jazz', 'song9': 'Jazz'}
        for gener in songGenres:
            for song in songGenres[gener]:
                songDict[song] = gener

        # print("songDict ", songDict)

        # For case when songGeners has empty lists 
        # songGenres = {"Rock": [], "Dubstep": [], "Techno": [], "Pop": [], "Jazz": []}
        # return {user: []} 
        # eg. {'David': [], 'Emma': []}
        if not songDict:
            for key in userSongs:
                del userSongs[key][:]
            return userSongs

        # Create favGenre dict {user: {gener: count}}  
        # eg. {'David': {'Rock': 2, 'Dubstep': 0, 'Techno': 2, 'Pop': 0, 'Jazz': 1}, 
        # 'Emma': {'Rock': 0, 'Dubstep': 1, 'Techno': 0, 'Pop': 2, 'Jazz': 0}}
        for user in userSongs:
            generDict = dict.fromkeys(generDict, 0)
            for song in userSongs[user]:
                generDict[songDict[song]] += 1
            favGenre[user] = generDict

        # print("favGenre ", favGenre) 

        # Find max count genres for each user and create dict of the form
        # {user: [favGenre1, favGenre2]}
        # eg. {'David': ['Rock', 'Techno'], 'Emma': ['Pop']}
        for user in favGenre:
            generList = []
            maxValue = max(favGenre[user].items(), key = lambda x: x[1])
            for gener, value in favGenre[user].items():
                if maxValue[1] > 0 and value == maxValue[1]:
                    generList.append(gener)
            favGenre[user] = generList

        # print("favGenre ", favGenre) 

        return favGenre

if __name__ == "__main__":
    userSongs, songGenres = initialize()
    sol = Solution()
    result = sol.favGenres(userSongs, songGenres)
    print(result)


'''
def initialize():
    userSongs = {  
       "David": ["song1", "song2", "song3", "song4", "song8"],
       "Emma":  ["song5", "song6", "song7"]
    }
    songGenres = {  
       "Rock":    ["song1", "song3"],
       "Dubstep": ["song7"],
       "Techno":  ["song2", "song4"],
       "Pop":     ["song5", "song6"],
       "Jazz":    ["song8", "song9"]
    }
    return userSongs, songGenres

def favGenres(userSongs, songGenres):
    output = {}
    for user in userSongs:
        song_list = userSongs[user]
        count = {}

        for song in song_list:
            for genre in songGenres:
                if(genre not in count):
                    count[genre] = 0
                if(song in songGenres[genre]):
                    count[genre] += 1

        output[user] = [key for key, val in count.items() if val == max(count.values())]
    
    return output

if __name__ == '__main__':
    userSongs, songGenres = initialize()
    print(favGenres(userSongs, songGenres))
'''