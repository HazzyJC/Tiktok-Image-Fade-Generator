import os
import subprocess
import shlex

path = input("Enter your image path: ")
path = path.replace('\\', '/')
print(path)
command = shlex.split('ffmpeg -framerate 30 -loop 1 -t 8 -i {} -vf "fade=in:0:60, fade=out:210:30" -pix_fmt yuv420p {}.mp4'.format(path, path))
print(command)
subprocess.call(command,shell=True)