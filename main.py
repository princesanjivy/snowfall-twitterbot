from PIL import Image
from io import BytesIO
import cv2, numpy, os, requests, moviepy.editor as mp

def image_to_video(image_url):

	req = requests.get(image_url)
	im = Image.open(BytesIO(req.content))
	im_name = "image.jpg"
	im.save(im_name, optimize=True, quality=85)

	images = []
	im = Image.open(im_name)
	if im.size[0] > im.size[1]:
		im_folder = 'Snowfall2/'
	else:
		im_folder = 'Snowfall3/'
	del im

	# pasting snow images on im_name
	for image in os.listdir(im_folder):
		im = Image.open(im_name)
		snow = Image.open(im_folder + image)
		im.paste(snow, (0, 0), snow)
		images.append(numpy.array(im))

	# save images array into avi video
	video_filename = "snowfall.avi"
	video_file = "snowfall.mp4"
	video = cv2.VideoWriter(video_filename,
							cv2.VideoWriter_fourcc(*'DIVX'),
							10,
							im.size)

	for im in images:
		im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
		video.write(im)

	video.release()	# release video

	# change avi to mp4 since opencv-python doesn't support H264 codec
	mp.VideoFileClip(video_filename).write_videofile(video_file)
	os.remove(im_name)
	os.remove(video_filename)

	return video_file

