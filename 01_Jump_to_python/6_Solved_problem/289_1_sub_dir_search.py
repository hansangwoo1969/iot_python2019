import os

with open("sub_dir_filename.txt", 'w', encoding='UTF-8') as f:
    for (path, dir, files) in os.walk("c:/"):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.py':
                print("%s/%s"%(path, filename))
                f.write("%s/%s\n"%(path, filename))
