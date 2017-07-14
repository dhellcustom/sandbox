import os, sys
from PIL import Image

def filter(img_src, filter_mode):
    img_dst = Image.new('RGB', img_src.size)
    src = img_src.load()
    dst = img_dst.load()

    mean_f = (1./9, 1./9, 1./9, 1./9, 1./9, 1/9, 1./9, 1./9, 1./9)
    #sharpen_f = (0, -1, 0, -1, 5, -1, 0, -1, 0)
    sharpen_f = (-1./8, -1./8, -1./8, -1./8, 2., -1./8, -1./8, -1./8, -1./8)

    if filter_mode == '1' : filter_weight = mean_f
    elif filter_mode == '2' : filter_weight = sharpen_f

    for y in range(img_src.size[1]):
        for x in range(img_src.size[0]):
            r_val = rgb_cal(0, src, x, y, img_src.size, filter_weight)
            g_val = rgb_cal(1, src, x, y, img_src.size, filter_weight)
            b_val = rgb_cal(2, src, x, y, img_src.size, filter_weight)
            dst[x,y] = (r_val, g_val, b_val)
    return img_dst


def rgb_cal(rgb, src, x, y, size, filter_weight):
    cal_result = 0.0
    for i in range (-1,2):
        for j in range (-1,2):
            if x+i < 0 or x+i == size[0] or y+j < 0 or y+j == size[1]: continue
            cal_result += (src[(x+i,y+j)][rgb] * filter_weight[i+j+2])
    return int(cal_result)


for infile in sys.argv[1:]:
    print("1. mean filter")
    print("2. sharpen filter")
    filter_mode = input("필터를 선택해주세요 : ")

    if filter_mode == '1' : rename = '_mean.jpg'
    elif filter_mode == '2' : rename = '_sharpen.jpg'

    outfile = os.path.splitext(infile)[0] + rename
    if infile != outfile:
        try:
            im = Image.open(infile)
            im = filter(im, filter_mode)
            im.save(outfile, "JPEG")
        except IOError:
            print("Error", infile)