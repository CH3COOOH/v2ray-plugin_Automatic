COL_ENABLE = 0
COL_SERVER = 1
COL_LA = 2
COL_HOST = 3
COL_PATH = 4
COL_PL = 5
COL_SL = 6
COL_TLS = 7
ROW_FROM = 1

import sys
import os

def isCorrectParam():
	## Command should be like:
	## $ python vpa.py ./v2ray-plugin vp-profile.csv'
	if len(sys.argv) == 3:
		return True
	else:
		return False


if __name__ == '__main__':
	if isCorrectParam == False:
		print('$ python vpa.py ./v2ray-plugin vp-profile.csv')
		exit()
	
	x_v2ray = sys.argv[1]
	f_profile = sys.argv[2]
	
	with open(f_profile, 'r') as o:
		ctr = 0
		while True:
			if ctr >= ROW_FROM:
				t_line = o.readline()
				
				if t_line[:3] == 'EOF':
					break

				_ = t_line.split(',')
				t_cmd = None
				
				if _[COL_ENABLE] == '1':
					if _[COL_SERVER] == '1':
						t_cmd = '%s -localAddr %s -server -host %s -path %s -localPort %s -remotePort %s' % \
						(x_v2ray, _[COL_LA], _[COL_HOST], _[COL_PATH], _[COL_PL], _[COL_SL])
						if _[COL_TLS] == '1':
							t_cmd += ' -tls'
							
					elif _[COL_SERVER] == '0':
						t_cmd = '%s -localAddr %s -localPort %s -remoteAddr %s -remotePort %s -host %s -path %s' % \
						(x_v2ray, _[COL_LA], _[COL_PL], _[COL_HOST], _[COL_SL], _[COL_HOST], _[COL_PATH])
						if _[COL_TLS] == '1':
							t_cmd += ' -tls'
							
					print(t_cmd)
			ctr += 1	
			
		
	
	
