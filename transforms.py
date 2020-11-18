import subprocess
import os
import cv2
import random
import glob

from moviepy.video.io.VideoFileClip import VideoFileClip


def resolution(inputpath, outputpath, height=320, width=225):
	command = 'ffmpeg -i ' + inputpath + ' -vf scale=' + str(width) + ':' + str(height) + ' ' + outputpath
	print(command)
	subprocess.call(command, shell=False)


def framerate(inputpath, outputpath, fps=25):
	command = 'ffmpeg -y -i ' + inputpath + ' -vf "setpts=1.25*PTS" -r ' + str(fps) + ' ' + outputpath
	print(command)
	subprocess.call(command, shell=False)


def format(inputpath, outputpath, src_format = 'flv', dst_format='avi'):
	command = ''
	if dst_format=='avi':
		command = 'ffmpeg -i ' + inputpath + ' -ar 22050 -b 2048k ' + outputpath
	elif dst_format == 'mp4':
		command = 'ffmpeg -i ' + inputpath + ' -codec copy ' + outputpath
	print(command)
	subprocess.call(command, shell=False)


def crop(inputpath, outputpath, height, width, x, y):
	command = 'ffmpeg -i ' + inputpath + ' -filter:v "crop= ' + str(width) + ':' + str(height) + ':' + str(x) + ':' + str(y) + '" ' + outputpath
	print(command)
	subprocess.call(command, shell=False)


def video_info(videopath):
	width, height, fps = None, None, None
	vcap = cv2.VideoCapture(videopath)
	if vcap.isOpened():
		width = vcap.get(3)
		height = vcap.get(4)
		# fps = vcap.get(5)
	video = VideoFileClip(videopath)

	return width, height, round(video.fps)


def add_border(videopath, outputpath, height, width):
	reheight = str(height * 1.3)
	rewidth = str(width)
	height = str(height)
	width = str(width)
	command = 'ffmpeg -i ' + videopath + ' -vf "scale=\'min(' + rewidth + ',iw)\':min\'(' + reheight + ',ih)\':force_original_aspect_ratio=decrease,pad=' + rewidth + ':' + reheight + ':(ow-iw)/2:(oh-ih)/2" ' + outputpath
	print(command)
	subprocess.call(command, shell=False)
	command = 'ffmpeg -y -i ' + outputpath + ' -vf scale=' + str(width) + ':' + str(height) + ' ' + outputpath
	print(command)
	subprocess.call(command, shell=False)


def add_logo(videopath, outputpath, logopath, height=None, width=None):
	command = 'ffmpeg -y -i ' + videopath + ' -i ' + logopath+ ' -filter_complex "overlay=10:10" ' + outputpath
	subprocess.call(command, shell=False)


def main(videopath, output_name, option):
	# videopath = '../newdata/13/13_130_Y.flv'
	# output_name = '../newdata/13/13_r_5.flv'

	width, height, fps = video_info(videopath)
	print(width, height)
	random_number = random.choice([2.0, 2.1, 2.2, 2.3, 2.4, 2.5])
	re_width = width * random_number
	re_height = height * random_number
	re_fps = 25 if round(fps) == 30 else 30
	crop_width = width * 0.7
	crop_height = height * 0.7
	crop_x = width * 0.15
	crop_y = height * 0.15
	height_margin = random.uniform(1.3, 2)
	width_margin = random.uniform(1.14, height_margin)
	logopath = './logo.png'

	if option == 'resolution':
		resolution(videopath, output_name, height=re_height, width=re_width)
	if option == 'framerate':
		framerate(videopath, output_name, fps=re_fps)
	if option == 'format':
		format(videopath, output_name, dst_format='avi')
	if option == 'crop':
		crop(videopath, output_name, crop_height, crop_width, crop_x, crop_y)
	if option == 'add_border':
		add_border(videopath, output_name, height, width)
	if option == 'add_logo':
		add_logo(videopath, output_name, logopath)


if __name__ == '__main__':
	option_list = ['resolution', 'framerate', 'format', 'crop', 'add_border', 'add_logo']
	video_list = [x for x in glob.glob('./*') if x.endswith('.flv')]

	for video in video_list:
		temp = os.path.splitext(video)
		# for option in option_list:
		# 	output_name = temp[0] + '_' + option + temp[1]
		# 	main(video, output_name, option)
		output_name = temp[0] + '_topborder' + temp[1]
		main(video, output_name, 'add_border')
