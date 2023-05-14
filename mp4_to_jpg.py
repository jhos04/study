# Date: 2023. 05. 14
# Writer: Jee Hoseong
# convert mp4 file to jpg files

from glob import glob
from subprocess import Popen, PIPE

def mp4_to_jpg(src_path, dst_path):
    files = glob(f'{src_path}\\*.mp4')
    print(files)
    for file in files:
        out_f = file.split('.')[0]
        cmd = f'ffmpeg -i {file} -vf fps=30 {out_f}_%04d.jpg'
        Popen(cmd, shell=True)

if __name__=='__main__':
    src_path = 'D:\\DataSet\\CCTV\\2022'
    dst_path = 'D:\\DataSet\\CCTV\\2022\\image'

    mp4_to_jpg(src_path, dst_path)
