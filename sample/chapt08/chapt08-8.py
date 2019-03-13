import tweepy
 # 「Consumer API keys」のところにあるキー
api = 'AAAAAAAAAAAAAAAAAAAAAA'
api_s = 'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB'
# 「Access token & access token secret」のところにあるキー
acc = '00000001-YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'
acc_s = 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ'

# OAuthの認証を作成
auth = tweepy.OAuthHandler( api, api_s )
auth.set_access_token( acc, acc_s )
# TwitterのWebAPIに接続
twitter = tweepy.API( auth )

# タイムラインのデータを取得
tweets = twitter.home_timeline()
for t in tweets:
	print( t.text )    # タイムラインを表示
