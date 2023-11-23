
from moviepy.editor import VideoFileClip, AudioFileClip
import moviepy.video.fx.all as vfx
import argparse, os, cv2, shutil
import matplotlib.pyplot as plt
from colorizers import *
from PIL import Image

def step1():
	try:
		shutil.rmtree('vid_out')
	except:
		pass

	try:
		os.mkdir('vid_out')
	except:
		pass

	try:
		os.mkdir('vid')
	except:
		pass

	file_name = 'vid/oldsong.mp4'
	vidcap = cv2.VideoCapture(file_name)
	success,image = vidcap.read()
	count = 0

	while success:
		cv2.imwrite(f"vid_out/{str(count).zfill(6)}.jpg", image)     # save frame as JPEG file      
		success,image = vidcap.read()
		print(f'Read {count+1} frame: ', success)
		count += 1

def step2():
	try:
		shutil.rmtree('bw_vid_out')
	except:
		pass

	try:
		os.mkdir('bw_vid_out')
	except:
		pass

	def magic(input_path, output_path):
		parser = argparse.ArgumentParser()
		parser.add_argument('--use_gpu', action='store_true', help='whether to use GPU')
		opt = parser.parse_args()

		colorizer_eccv16 = eccv16(pretrained=True).eval()
		colorizer_siggraph17 = siggraph17(pretrained=True).eval()
		if(opt.use_gpu):
			colorizer_eccv16.cuda()
			colorizer_siggraph17.cuda()

		img = load_img(input_path)
		(tens_l_orig, tens_l_rs) = preprocess_img(img, HW=(256,256))
		if(opt.use_gpu):
			tens_l_rs = tens_l_rs.cuda()

		img_bw = postprocess_tens(tens_l_orig, torch.cat((0*tens_l_orig,0*tens_l_orig), dim=1))
		out_img_eccv16 = postprocess_tens(tens_l_orig, colorizer_eccv16(tens_l_rs).cpu())
		plt.imsave(output_path, out_img_eccv16)

	images = [img for img in os.listdir('vid_out')
				if img.endswith(".jpg") or
					img.endswith(".jpeg") or
					img.endswith("png")]

	for i in images:
		print('Processing for frame : ', i)
		magic(f'vid_out/{i}', f'bw_vid_out/{i}')

def step3():
	mean_height = 0
	mean_width = 0

	path = 'bw_vid_out'
	num_of_images = len(os.listdir('bw_vid_out'))
	print(f'num_of_images = {num_of_images}')

	for file in os.listdir('bw_vid_out'):
		im = Image.open(os.path.join(path, file))
		width, height = im.size
		mean_width += width
		mean_height += height

	mean_width = int(mean_width / num_of_images)
	mean_height = int(mean_height / num_of_images)

	for file in os.listdir('bw_vid_out'):
		if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"):
			im = Image.open(os.path.join(path, file))

			width, height = im.size
			imResize = im.resize((mean_width, mean_height), Image.Resampling.LANCZOS)
			imResize.save(os.path.join(path, file), 'JPEG', quality = 95)
			print(im.filename.split('\\')[-1], " is resized")

	def generate_video():
		image_folder = 'bw_vid_out'
		video_name = 'mygeneratedvideo.avi'
		
		images = [img for img in os.listdir(image_folder)
				if img.endswith(".jpg") or
					img.endswith(".jpeg") or
					img.endswith("png")]
		
		frame = cv2.imread(os.path.join(image_folder, images[0]))
		height, width, layers = frame.shape
		video = cv2.VideoWriter(os.path.join('vid', video_name), 0, 1, (width, height))

		for image in images:
			print('Writing for ', image)
			video.write(cv2.imread(os.path.join(image_folder, image)))
		
		cv2.destroyAllWindows()
		video.release()

	generate_video()

def step4():
	in_loc = 'vid/mygeneratedvideo.avi'
	out_loc = 'vid/coloured.mp4'

	clip = VideoFileClip(in_loc)
	clip = clip.set_fps(clip.fps * 30)
	final = clip.fx(vfx.speedx, 30)

	audioclip = AudioFileClip("vid/oldsong.mp4")
	videoclip = final.set_audio(audioclip)
	videoclip.write_videofile(out_loc)

step1()
step2()
step3()
step4()
