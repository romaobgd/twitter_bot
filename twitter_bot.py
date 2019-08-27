import tweepy
import time

#print('test bot')

# Keys
CONSUMER_KEY = 'we7XkBnJTVHxdnyRE0y94TsAz'
CONSUMER_SECRET = 'l5KxpzZTBvEAvlZnZ1CCMctl16COFOEJNstZPK5LBJZkJbfmjU'
ACCESS_KEY = '1166063418144673793-IrpqG40d0eXkVSQrqChCF1xqRslEkM'
ACCESS_SECRET = 'sHxZfVtBsUKWKvdjP0NLX1vnWJe8MmPMANmhn6FO6ArfS'


# autenticando
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

##
FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def favorite():
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    #print(str(last_seen_id))
    search = api.search(q='naruto', count=15, since_id=last_seen_id)

    for searches in reversed(search):
        if 'naruto' in searches.text.lower():
            try:
                api.create_favorite(searches.id)
                print('Found naruto!\n' + str(searches.id) + ' - '
                              + searches.text + '\n')
            except tweepy.TweepError as e:
                print(str(e) + '\n')
        last_seen_id = searches.id
        store_last_seen_id(last_seen_id, FILE_NAME)

while True:
    favorite()
    time.sleep(20)


