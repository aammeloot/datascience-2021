critics = {
    'Lisa Rose': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'Superman Returns': 3.5,
        'You, Me and Dupree': 2.5,
        'The Night Listener': 3.0,
    },
    'Gene Seymour': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 1.5,
        'Superman Returns': 5.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 3.5,
    },
    'Michael Phillips': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.0,
        'Superman Returns': 3.5,
        'The Night Listener': 4.0,
    },
    'Claudia Puig': {
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'The Night Listener': 4.5,
        'Superman Returns': 4.0,
        'You, Me and Dupree': 2.5,
    },
    'Mick LaSalle': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'Just My Luck': 2.0,
        'Superman Returns': 3.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 2.0,
    },
    'Jack Matthews': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'The Night Listener': 3.0,
        'Superman Returns': 5.0,
        'You, Me and Dupree': 3.5,
    },
    'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0,
             'Superman Returns': 4.0},
}



#print('Print out the entire data set')
#print(critics)

#print('Reviews from a selected critic')
#print(critics['Lisa Rose'])

#print('Print review from select film for selected')
#print(critics['Lisa Rose']['Lady in the Water'])

#print('Print all the critics')
#for c in critics:
#    print(c)

#print('Print list of all reviews by a critic')
#for c in critics:
#    print(critics[c])

#print('Print list of all films reviewed')
#for c in critics:
#    for f in critics[c]:
#        print(f)

#print('List of critics and films reviewed')
#print('Print list of all reviews by a critic')
#for c in critics:
#    for f in critics[c]:
#        print(c,f)


#print('List of critics and films reviewed')
#print('Print list of all reviews by a critic')
#for c in critics:
#    for f in critics[c]:
#        print(c,f,critics[c][f])

print('Rebuild the data set as a dictionary of films')

films = {}
t = {}
for c in critics:
    for f in critics[c]:
        critic = c
        film = f
        rating = critics[c][f]
        if film in films:
            t = films[film]
            t[critic]=rating
        else:
            films[film] = {}
            t = films[film]
            t[critic]=rating

print(films)

