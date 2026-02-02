import matplotlib.pyplot as plt
import mne
import matplotlib
import os
import pandas as pd
matplotlib.use('TkAgg')
# 数据文件存放地址
# os.chdir('D:\\test-Python\\mne-test\\')

evoked_path=r'D:\pythonProject\RZG_ERP&EEG\ERP\evoked'
evoked_txt=r'D:\pythonProject\RZG_ERP&EEG\ERP\evoked_txt'

if os.path.exists(evoked_txt):
    pass
else:
    os.mkdir(evoked_txt)

mark = ['1', '5', '9',  '13', '17', '21']
raw_fname=os.listdir(evoked_path)

for i in range(0, len(raw_fname)):
    path = os.path.join(evoked_path,raw_fname[i])
    if os.path.isfile(path):
        name = path[path.rfind('\\') + 1:path.rfind('_')]
        print(name)
        evoked = mne.read_evokeds(path)
        evoked_df = evoked[0].to_data_frame()
        evoked_df.to_csv(evoked_txt + '\\{}.txt'.format(name), sep='\t', index=False)