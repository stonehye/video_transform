import subprocess
import os
import glob


def ffmpeg_extractframes(videopath):
	filename = os.path.basename(videopath)
	videopath = videopath.replace('\\', '/')
	savedir = filename.split('_')[0] + '/' + filename + '/'

	if not os.path.isdir(savedir):
		os.makedirs(savedir)

	command = 'ffmpeg -i ' + videopath + ' -r 1 ' + savedir + filename + '-%03d.jpg'
	print(command)
	subprocess.call(command, shell=True)


if __name__=='__main__':
	dirlist = glob.glob('../newdata/*')

	for dir in dirlist:
		filelist = glob.glob(os.path.join(dir, '*'))
		for file in filelist:
			ffmpeg_extractframes(file)
		break