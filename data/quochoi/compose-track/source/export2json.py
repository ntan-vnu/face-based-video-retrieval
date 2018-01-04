#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import json

NUM_PID = 69

fds = glob.glob('tracklets_*/')
fds.sort()
vd_names = []
for i in range(len(fds)):
	vd_names.append(fds[i].split('_')[1])
	print vd_names[i]

yt_urls = {
	"NA170605AM1":"https://www.youtube.com/watch?v=UQjYImoclB0",
	"NA170605AM2":"https://www.youtube.com/watch?v=rt2pgCSSh8Y",
	"NA170614AM1":"https://www.youtube.com/watch?v=bLOOilXA44g",
	"NA170614AM2":"https://www.youtube.com/watch?v=6tm_GJ95hu8",
	"NA170615AM2":"https://www.youtube.com/watch?v=GGKbiH_Jdds"
}

fname = open('/media/an/9E34C58E34C56A3B/Users/an/Desktop/detected-5vd/avatars/uid.txt')
db_names = fname.readlines()
fname.close()
for i in range(NUM_PID):
	db_names[i] = db_names[i].strip()

meta = {}
for i in range(NUM_PID):
	meta['%d'%(i)] = {'name':db_names[i],
						'avatar':"/images/avatars/%d.jpg"%(i),
						'tracklets':[] }
for i_fd in range(len(fds)):
	print fds[i_fd]
	for pid in range(NUM_PID):
		f = open('%s/%d.txt'%(fds[i_fd], pid))
		count = 0
		for line in f:
			st = line.strip().split('\t')[0]
			meta['%d'%(pid)]['tracklets'].append({
				'title':vd_names[i_fd] + '_%03d'%(count),
				'url':yt_urls[vd_names[i_fd]],
				'time':st,
				'thumnail':'/images/thumnails/%s_%03d_%03d.jpg'%(vd_names[i_fd], pid, count)
				})
			count += 1

		f.close()

for i in range(NUM_PID):
	print i, len(meta['%d'%(i)]['tracklets'])

order2write = [18, 0, 22, 23, 65, 1, 30, 33, 11, 14, 19, 20, 27, 28, 48, 49, 54, 64, 68, 2, 3, 4, 5, 6, 7, 8, 12, 13, 15, 21, 24, 25, 26, 29, 31, 32, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 46, 47, 50, 51, 52, 53, 57, 58, 59, 60, 61, 66, 67, 9, 10, 16, 17, 41, 45, 55, 56, 62, 63]

fout = open('quochoi.json', 'w')
for i in range(NUM_PID):
	#json.dump(meta['%d'%(i)], fout, indent=4, sort_keys=True)
	json.dump(meta['%d'%(order2write[i])], fout, sort_keys=True, ensure_ascii=False)
	fout.write('\n')
fout.close()