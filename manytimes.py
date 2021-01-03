from transforms import *
import shutil


transforms = ['border', 'brightness', 'crop', 'framerate', 'logo', 'resolution', 'rotate', 'flip', 'grayscale']
level = ['Light']
times = 8
video_list = glob.glob('/nfs_shared_/hkseok/SIMULATED_DATASET/videos/original_SD')

def transform(option, input, output, level):
    if option == transforms[0]:
        add_border(input, output, *video_info(input), level=level)
    elif option == transforms[1]:
        brightness(input, output, *video_info(input), level=level)
    elif option == transforms[2]:
        crop(input, output, *video_info(input), level=level)
    elif option == transforms[3]:
        framerate(input, output, *video_info(input), level=level)
    elif option == transforms[4]:
        add_logo(input, output, *video_info(input), level=level)
    elif option == transforms[5]:
        resolution(input, output, *video_info(input), level=level)
    elif option == transforms[6]:
        rotate(input, output, *video_info(input), level=level)
    elif option == transforms[7]:
        flip(input, output, *video_info(input), level=level)
    elif option == transforms[8]:
        grayscale(input, output, *video_info(input), level=level)


for i in range(1, times+1):
    if not os.path.isdir(os.path.join('test', str(i))):
        os.makedirs(os.path.join('test', str(i)))


for v in video_list:
    transform_temp = transforms.copy()
    videoname = os.path.basename(v)
    inputpath = v
    for i in range(1, times+1):
        outputpath = os.path.join('test', str(i), videoname)
        choice = random.choice(transform_temp)
        transform_temp.remove(choice)

        transform(choice, inputpath, outputpath, level[0])

        inputpath = outputpath