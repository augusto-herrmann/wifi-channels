import re
import subprocess

find_channel = re.compile(r'\(Channel (\d{1,2})\)')
command = 'iwlist wlan0 scan'

process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error  = process.communicate()

if error is None:
    output = output.decode('utf-8')
    channels = find_channel.findall(output)
else:
    raise ValueError(error.decode('utf-8'))

def band(channel):
    if channel < 4:
        return 1
    elif channel > 8:
        return 11
    else:
        return 6

bands = list(map(band, map(int, channels)))

print(f'''
    Band 1-3: {bands.count(1)}
    Band 4-8: {bands.count(6)}
    Band 9-13: {bands.count(11)}
''')

