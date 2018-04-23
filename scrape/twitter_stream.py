import tweepy
import json
import hashlib
import re
#import couchdb
from tweepy.utils import import_simplejson

#Define Database connection creds
server = "localhost:8091"
admin_username = "Administrator"
admin_password = ""

#Twitter auth stuff
#Get yours by registering an app at dev.twitter.com
consumer_key = 'Q8hQiSt4axb7o70bJNg6a4ixr'
consumer_secret = 'KbGdxmWmcFXJbsQU3whDKcmDaHjcKTqOcTVYB3PiHdb1ud0XSK'
access_token_key = '229680192-8EZxdsi87czPXa94f2jK2voMbgH6jYnMUu77tGGl'
access_token_secret = 'o5oiMY7jcITktKlPuZTcY9wWZSCM5Npoef7Fwu2tivkPm'

#Define filter terms
filterTerms = [
### politcs  
'#political','#parties','#politicalparty','#american','#politicalcorrectness','#leaders','#time','#power','#history','#views','#government','#career','#vote','#country','#class','#support','#system','#politicalleaders','#party','#people','#news','#world','#twitter','#politics','#today',

### lifestyle
'#lifestyle','#fashion','#love','#fitness','#health','#luxury','#blog','#life','#weightloss','#yoga','#photography','#app','#business','#healthylifestyle','#change','#brand','#living','#diet','#likedvideo','#morning','#image','#welcome','#designer','#lot',

### music
'#music','#vide','#love','#pop','#newmusic','#rock','#life','#dance','#live','#work','#musicvideo','#songs','#officialmusic','#song','#musiclife','#nowlistening','#playing','#trap','#voice','#shine','#playlist',

### arts & culture


### technology
'#technology','#security','#blockchain','#iphone','#education','#tech','#socialmedia','#information','#microsoft','#windows','#blockchaintechnology','#media','#future','#phone','#year','#application','#innovation','#management','#surface','#launch','#year','#reality','#company','#kind',

### fun 
'#fun','#kids','#havefun','#having','#fact','#funfact','#havingfun','#night','#watching','#time','#group','#friday','#thanks','#looking','#hadfun','#doin','#playing','#play',

###  news
'#bitcoin','#breaking','#breakingnews','#foxnews','#wine','#howto','#nbc','#fox','#nbcnews','#foxnews','#cnn','#cnnnews','#missle','#media','#channel','#abc','#abcnews','#updates',

###  science
'#science','#data','#life','#school','#health','#job','#datascience','#fiction','#sciencefiction','#math','#computer','#computerscience','#grade','#according','#museum','#theory',

###  non-profit
'#facebook','#nra','#tips','#home','#business','#organizations','#organization','#nonprofit','#fundraising','#donors','#study','#charity','#program','#year','#board','#care','#community','#event','#professionals','#coaching',

### sports
'#sports','#football','#anime','#girls','#game','#cricket','#skysports','#sky','#nfl','#russian','#team','#teams','#season','#week','#thanks','#center','#luck','#nbcsports','#foxsports','#espn','#','#','#','#','#','#',
### gaming
'#gaming','#giveaway','#win','#fortnite','#stream','#xbox','#laptop','#disorder','#gamingchair','#gamers','#channel','#core','#playstation','#retrogaming','#gamingchannel','#xboxone','#headset','#gostei','#gamingheadset','#videogamin'
]

json = import_simplejson()
#try:
#    couchclient = couchdb.Server()
#except:
#    print "Cannot find CouchDB Server ... Exiting\n"
#    print "----_Stack Trace_-----\n"
#    raise

#Try to use the twitter bucket or else switch to use default bucket
#try:
#    db = couchclient['mydatabase']
#    print "Using mydatabase bucket"
#except:
#    db = couchclient['default']
#    print "Using default bucket"

#OAuth
auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth1.set_access_token(access_token_key, access_token_secret)

class StreamListener(tweepy.StreamListener):
    json = import_simplejson()

    def on_status(self, tweet):
        print 'Ran on_status'

    def on_error(self, status_code):
        return False

    def on_data(self, data):
        print data
        with open('fetched_tweets.txt','a') as tf:
            tf.write(data)
            return True
#        if data[0].isdigit():
#            pass
#        else:
#            jdata = json.loads(data)
#            db.save(jdata)

l = StreamListener()
streamer = tweepy.Stream(auth=auth1, listener=l)
streamer.filter(track=filterTerms)
