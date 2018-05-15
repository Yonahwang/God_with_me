import json
import pandas as pd

df = pd.DataFrame()
filetypes = []
for i in range(257,301):
    filepath = 'VirusShare_00'+str(i)+'.zip.exiftool.json'
    f = open(filepath,'r')
    jsons = json.loads(f.read())
    f.close()
    for data in jsons:
        try:
            filetype = data['exifinfo']['File:FileType']
            if filetype == 'ZIP' and data['exifinfo']['ZIP:ZipFileName'] == 'META-INF/MANIFEST.MF':
                filetype = 'APK'
        except:
            filetype = 'unknow file type'
        filetypes.append(filetype)
    print(filepath)
df['filetype'] = filetypes
df['count'] = 1
df = df.groupby('filetype').sum()
print(df)
