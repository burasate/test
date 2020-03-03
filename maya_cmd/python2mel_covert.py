#Convert Python To Mel Script
def PythonToMel (file_path):
    file = open(file_path, 'r')
    line_list = file.readlines()
    mel_line = []
    mel_line.append('python(\"\\n\\')
    for i in line_list:
        mel_line.append(i.replace('\n','\\n\\'))
    mel_line.append('\");')

    print ('\n'.join(mel_line))