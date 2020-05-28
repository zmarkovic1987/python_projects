

songs = {'baobab': 5, 'osecam se dobro':4, 'disem':4, 'pustinja':5}

# for each in songs.keys():
#     if songs[each] == 5:
#         print(each)
#     else:
#         continue

#################
def replace(dicti, e, v):

    for each in dicti:
        if dicti[each] == e:
            dicti[each] = v
    # return dicti

replace(songs, 5, 10)
print(songs)

