import glob
import os
import cv2

NUM_PID = 69

def getFrame(video_cap, frame):
	video_cap.set(cv2.CAP_PROP_POS_FRAMES, round(frame))
	ret, res = video_cap.read()
	return res
	

def compute_frame(st, et, fps):
	sm, ss = st.split(':')
	ist = int(sm) * 60 + int(ss)
	em, es = et.split(':')
	iet = int(em) * 60 + int(es)
	return (ist + iet) * fps / 2

fds = glob.glob('*_*/')
fds.sort()
vd_names = []
for i in range(len(fds)):
	vd_names.append(fds[i].split('_')[1])
	print vd_names[i]

yt_urls = {
	'NA170605AM1':'../videos//NA170605AM1.mp4',
	'NA170615AM2':'../videos//NA170615AM2.mp4',
	'NA170614AM1':'../videos//NA170614AM1.mp4',
	'NA170614AM2':'../videos//NA170614AM2.mp4',
	'NA170605AM2':'../videos//NA170605AM2.mp4'
}

if not os.path.exists('thumnails'):
	os.mkdir('thumnails')

for i_fd in range(len(fds)):
	video_cap = cv2.VideoCapture(yt_urls[vd_names[i_fd]])
	fps = video_cap.get(cv2.CAP_PROP_FPS)
	frame_count = video_cap.get(cv2.CAP_PROP_FRAME_COUNT)

	for pid in range(NUM_PID):
		print '...', pid
		f = open('%s/%d.txt'%(fds[i_fd], pid))
		count = 0
		for line in f:
			st, et = line.strip().split('\t')
			frame = compute_frame(et, st, fps)
			img = getFrame(video_cap, frame)
			tn_pth = 'thumnails/%s_%03d_%03d.jpg'%(vd_names[i_fd], pid, count)
			if img is None or (img.shape[0] < 100 or img.shape[1] < 100):
				img = cv2.imread('/media/an/9E34C58E34C56A3B/Users/an/Desktop/detected-5vd/avatars/id-frames/%d.jpg'%(pid))
			cv2.imwrite(tn_pth, cv2.resize(img, (0, 0), fx=0.5, fy=0.5))
			print frame, tn_pth
			count += 1

		f.close()
	print fds[i_fd]

