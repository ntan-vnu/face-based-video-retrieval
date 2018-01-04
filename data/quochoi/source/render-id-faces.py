import glob
import os
import cv2

NUM_PID = 69

video_captures = {
	'NA170605AM1':cv2.VideoCapture('../videos/NA170605AM1.mp4'),
	'NA170615AM2':cv2.VideoCapture('../videos/NA170615AM2.mp4'),
	'NA170614AM1':cv2.VideoCapture('../videos/NA170614AM1.mp4'),
	'NA170614AM2':cv2.VideoCapture('../videos/NA170614AM2.mp4'),
	'NA170605AM2':cv2.VideoCapture('../videos/NA170605AM2.mp4')
}

fps = {
	'NA170605AM1':video_captures['NA170605AM1'].get(cv2.CAP_PROP_FPS),
	'NA170615AM2':video_captures['NA170615AM2'].get(cv2.CAP_PROP_FPS),
	'NA170614AM1':video_captures['NA170614AM1'].get(cv2.CAP_PROP_FPS),
	'NA170614AM2':video_captures['NA170614AM2'].get(cv2.CAP_PROP_FPS),
	'NA170605AM2':video_captures['NA170605AM2'].get(cv2.CAP_PROP_FPS)
}

print video_captures
print fps

f = open('id-faces.txt')
g = open('id-time.txt', 'wt')
error = 0
for line in f:
	ind, vd_name, nframe = line.strip().split('\t')
	print ind, vd_name, nframe
	nframe = float(nframe)
	tt = nframe / round(fps[vd_name])

	hh = tt / 3600
	mm = (tt % 3600) / 60
	ss = tt % 60
	g.write('%s\t%s\t%02d:%02d:%02d\n'%(ind, vd_name, hh, mm, ss))
	continue
	video_captures[vd_name].set(cv2.CAP_PROP_POS_FRAMES, round(nframe))
	ret, img = video_captures[vd_name].read()
	if not ret:
		print ind
		error += 1
	else:
		cv2.imwrite('id-frames/%s.jpg'%(ind), img)
		print '.'

print 'error', error
g.close()
f.close()