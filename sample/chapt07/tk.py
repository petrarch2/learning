from tkinter import Tk, ttk

# ウィンドウを作成
win = Tk()
# ウィンドウの設定
win.title( 'Hello Paint' )
win.geometry( '600x400' )

# ラベルを作成
lbl = ttk.Label( win, text='太さ:' )
# ラベルの位置
lbl.place( x=15, y=20 )

# 入力エリアを作成
ent = ttk.Entry( win, width=3 )
# ラベルの設定と位置
ent.insert( 0, '5' )
ent.place( x=15, y=50 )

# ラジオボタンのグループを作成
from tkinter import StringVar
grp = StringVar()
# ラジオボタンを作成
grp.set('lin')
lin = ttk.Radiobutton( win, text='線', variable=grp, value='lin' )
brs = ttk.Radiobutton( win, text='ブラシ', variable=grp, value='brs' )
ers = ttk.Radiobutton( win, text='消ゴム', variable=grp, value='ers' )
# ラジオボタンの位置
lin.place( x=15, y=100 )
brs.place( x=15, y=130 )
ers.place( x=15, y=160 )

# ボタンを作成
btn = ttk.Button( text='新規', width=3 )
# ボタンの位置
btn.place( x=15, y=200 )

# キャンバスを作成
from tkinter import Canvas
cvs = Canvas( win, width=475, height=350 )
# キャンバスの位置
cvs.place( x=100, y=25 )

# キャンバス上のマウスのハンドリング
bef = None    # 一つ前のマウスの位置

def mouseOn( ev ):    # ボタンを押しながらマウスが移動
	global bef
	if not bef:
		bef = ev
	wd = float( ent.get() )    # 太さを実数値で取得
	tp = grp.get()    # ラジオボタンの値を取得
	if tp == 'lin':    # 線を描写
		cvs.create_line( bef.x, bef.y, ev.x, ev.y, width=wd )
	elif tp == 'brs':    # 円を描写
		cvs.create_oval( ev.x, ev.y, ev.x + wd, ev.y + wd, width=1 )
	elif tp == 'ers':    # 白い円を塗りつぶす
		cvs.create_oval( ev.x, ev.y, ev.x + wd, ev.y + wd, width=0, fill='white' )
	bef = ev
	
def mouseOff( ev ):    # ボタンの位置をクリア
	global bef
	bef = None
	
# キャンバスにマウスイベントを設定
cvs.bind( '<B1-Motion>', mouseOn )
cvs.bind( '<ButtonRelease-1>', mouseOff )
cvs.bind( '<Leave>', mouseOff )

# ボタンが押されたときの処理
def btnHandle( ev ):
	for id in cvs.find_all():
		cvs.delete( id )
# ボタンにマウスイベントを設定
btn.bind( '<Button-1>', btnHandle )

# ウィンドウのメイン処理
win.mainloop()


