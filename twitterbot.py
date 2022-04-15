from twitter import Twitter, OAuth, TwitterHTTPError
import os
import json
import itertools
import random 
import time

API_KEY=""
API_KEY_SECRET=""
ACCESS_TOKEN=""
ACCESS_TOKEN_SECRET=""

TWITTER_HANDLE=""    #twitterusername here ex:"@twitter"

languages=["en"]

t = Twitter (auth=OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY, API_KEY_SECRET))

class Followbot():
        def main(self):
            pass

        #follow number 1    user by twitter id
        def follow_user(self, follow_log, twitter_id):
            try:
                t.friendship.create(user_id=twitter_id, follow=True)
                except TwitterHTTPError as e:
                    if 'blocked' in str(e).lower():
                    #this user is blocked
                    logging.info('Ignoring "blocked" exception')
                    logging.exception(e)
                    #else:
                    #follow_log.save_follow(twitter_id, reason)
        
        def follow_all_followers(self, max=5, result_type"recent"):
            to_follow = set()

            #here is to get the users that you are following
        
        followingIds    = set(t.friends.ids(screen_name=TWITTER_HANDLE)["ids"])
        print(f"fetching {max} of user {TWITTER_HANDLE}'s following list...")
        for i, userId in enumerate(random.sample(followingIds, max)):
        print(f"Checking {i+1}'th user of followed list.")
        thisFollowingIds = set(t.friends.ids(user_id=userId)["ids"])
        print(f"Found {len(thisfollowing)} users on {i+1}/max followed user.")

        #add this user to id to list to follow
        len_before = len(to_follow)
        to_follow = followingIds
        len_after = len(to_follow)
        print(f"Removed { len_before - len_after } users already being followed from to-follow list.")
        print(f"Beginning following {len_after} users:")

        for twitterId in to_follow
            print(f"following user: {twitter_id}")
            time.sleep(0.1)
            self.follow_user(follow_log=None, twitter_id=twitter_id)

    if __name__ == "__main__":
        followbot = Followbot()
        followbot.follow_all_followers()