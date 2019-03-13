all_txt = ''    # バッファを用意
with open( 'sample.txt' ) as f:
	line = f.readline()    # ファイルから一行読み込む
	while line:    # ファイルが続くかぎり繰り返す
		all_txt += line    # バッファに一行追加
		line = f.readline()    # ファイルから一行読み込む
all_list = []    # バッファを用意
with open( 'sample.txt' ) as f:
	line = f.readline()    # ファイルから一行読み込む
	while line:    # ファイルが続くかぎり繰り返す
		all_list.append( line )    # バッファに一行追加
		line = f.readline()    # ファイルから一行読み込む

all_txt = ''.join( all_list )    # バッファ内の文字列を繋げる
