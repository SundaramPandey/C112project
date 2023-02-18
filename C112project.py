import os
import shutil

source="C:/Users/slane/OneDrive/Documents/whjr python"
destination="C:/Users/slane/OneDrive/Documents/whjr python/docx"

list_of_docx=os.listdir(source)
for a in list_of_docx:
    name,extensions=os.path.splitext(a)
    if extensions == '':
        continue
    if extensions in ['.ppt','.docx','.txt','.pdf']:
        path1=source+'/'+a
        path2=destination
        path3=destination+'/'+a

        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            shutil.move(path1,path3)