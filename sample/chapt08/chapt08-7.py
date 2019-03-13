# 送信先アドレス 
to = 'target@yourserver.com'

#メールアカウント
addr = 'myname@server.com'
pazz = 'XXXXXXXX'
 
#SMTPサーバの設定
host = 'mail.server.com'
port = 587

mail = """
こんにちは！
メールの文面です
"""

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

# メールのデータを作成する
msg = MIMEMultipart( 'alternative' )
msg[ 'Subject' ] = Header( 'メールのタイトル', 'utf-8' )
msg[ 'From' ] = addr
msg[ 'To' ] = to
# メールデータに本文のデータを添付する
msg.attach( MIMEText( mail, 'plain', 'utf-8' ) )

import smtplib

# SMTPサーバーに接続する
s = smtplib.SMTP( host=host, port=port )
s.login( addr, pazz )
# メールを送信して切断する
s.sendmail( addr, [ to ], msg.as_string() )
s.quit()
