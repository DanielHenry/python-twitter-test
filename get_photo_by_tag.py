import twitter;
import os;

api = twitter.Api(
    consumer_key=getenv('CONSUMER_KEY'),
    consumer_secret=getenv('CONSUMER_SECRET'),
    access_token_key=getenv('ACCESS_TOKEN_KEY'),
    access_token_secret=getenv('ACCESS_TOKEN_SECRET')
);

#print api.VerifyCredentials();
print "###############";
trends = api.GetTrendsCurrent();
print "###############";
for trend in trends:
    print trend.name;
print "###############";
my_followers = api.GetFollowers();
for user in my_followers:
    print user.name;
print "###############";
all_status_mention_me = api.GetMentions();
for status_mention_me in all_status_mention_me:
    if (status_mention_me.media==None): continue;
    for foto in status_mention_me.media:
        print foto.media_url;
        os.system("wget " + foto.media_url);
print "###############";
counter = 0;
all_pyconid2017_status = api.GetSearch(raw_query="q=%23pyconid2017");
print all_pyconid2017_status;
'''for pyconid2017_status in all_pyconid2017_status:
    if (pyconid2017_status.media==None): continue;
    for foto in pyconid2017_status.media:
        print str(counter) + " " + foto.media_url;
        counter += 1;
print "###############";
'''