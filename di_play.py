from subprocess import call
import json
import urllib2
import sys



data = urllib2.urlopen('http://listen.di.fm/public2/')
json_object = json.load(data)

stations = []

# Append json item to List
# This loop will run only once
for song in json_object:
    # now song is a dictionary
    playlist = song['playlist']
    key = song['key']
    name = song['name']
    stations.append([name, playlist, key])

def print_table(lst):
    table = ''
    half = len(lst) / 2
    for x1 in xrange(half):
        x2 = x1 + half
        col1 = '(%s) %s' % (x1 + 1, lst[x1][0])
        col2 = '(%s) %s\n' % (x2 + 1, lst[x2][0])
        table += col1.ljust(30) + col2
    print "=" * 70
    print "{:10} {:19} {:10} {}".format("No.", "Station","No.", "Station")
    print "=" * 70
    print table


while True:
    print_table(stations)
    num = raw_input("Select station to play or enter 'quit' to stop:")
    if num.lower() == ('quit' or 'q'):
        print 'Bye!'
        break
    else:
        try:
            val = int(num)
            print(stations[val][0])
            url = "http://pub1.diforfree.org:8000/di_{}_hi".format(stations[val][2])
            call("mplayer " + url, shell=True )

            # reset index
            index = 1
        except ValueError:
            print("You must input only number of station!")
