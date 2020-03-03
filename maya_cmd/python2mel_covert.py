#Convert Python To Mel Script
def PythonToMel (file_path):
    file = open(file_path, 'r')
    line_list = file.readlines()
    mel_line = []
    mel_line.append('python(\"\\n\\')
    for i in line_list:
        text = i.replace('\n','')
        text = text.replace('\"','\\"')
        text = text+'\\n\\'
        mel_line.append(text)
    mel_line.append('\");')

    print ('\n'.join(mel_line))
