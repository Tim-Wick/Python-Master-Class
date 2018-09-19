##Tuples are similar to lists but are immutable###

t = "a", "b", "c"
print(t)

print("a", "b", "c")
print(("a", "b", "c"))

##First answer returned in parenthesis, signifying a tuple###

welcome = "Welcome to my nightmare", "Alice Cooper", 1975
bad = "Bad Company" "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

# metallica[0] = "Master of puppets"
imdelda = imelda[0], "Imelda May", imelda[2]
print(imdelda)
###Contents of tuples are immutable, but you can still update the varable to correct mistakes###

metallica2 = ["Ride the Lightning", "Metallica", 1984]
print(metallica2)
metallica2[0] = "Master of Puppets"
print(metallica2)
##Lists are mutable###
##Tuples are useful for dictionaries as they're immutable###
## Lists are intended to hold items of the same type, tuples intended to hold items of different types.
EG; album names and years###

welcome = "Welcome to my nightmare", "Alice Cooper", 1975
bad = "Bad Company" "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Imilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

metallica2 = ["Ride the Lightning", "Metallica", 1984]
print(metallica2)

# title, artist, year = imelda
# print(title)
# print(artist)
# print(year)

metallica2.append("Rock")
title, artist, year = metallica2
print(title)
print(artist)
print(year)
### Lists won't work as well with unpacking ###

imelda.append("Jazz")
### Can't use append with tuples ###

welcome = "Welcome to my nightmare", "Alice Cooper", 1975
bad = "Bad Company" "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Imilda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

print(imelda)

title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)

imelda = "More Mayhem", "Imilda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

title, artist, year, tracks = imelda

print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print("\tTrack number{0}, Title: {1}".format(track, title))

### Lists in a tuple can be changed ###

imelda = "More Mayhem", "Imilda May", 2011, (
    [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")])

print(imelda)

imelda[3].append((5, "All For You"))

title, artist, year, tracks = imelda
tracks.append((6, "Eternity"))
print(title)
print(artist)
print(year)
for song in tracks:
    track, title =  song
    print("\tTrack #{0}, Title: {1}".format(track, title))
