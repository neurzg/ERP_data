import matplotlib.pyplot as plt
import mne
import matplotlib
import os
import pandas as pd
matplotlib.use('TkAgg')

epochs_clean_path=r'D:\pythonProject\RZG_ERP&EEG\ERP\epochs_clean_path'
evoked_path=r'D:\pythonProject\RZG_ERP&EEG\ERP\evoked'
select_epoch_path=r'D:\pythonProject\RZG_ERP&EEG\ERP\select_epoch_path'

if os.path.exists(evoked_path):
    pass
else:
    os.mkdir(evoked_path)

if os.path.exists(select_epoch_path):
    pass
else:
    os.mkdir(select_epoch_path)

mark = ['1', '5', '9',  '13', '17', '21']
raw_fname=os.listdir(epochs_clean_path)

for i in range(0, len(raw_fname)):
    path = os.path.join(epochs_clean_path,raw_fname[i])
    print(path)
    if os.path.isfile(path):
        name = path[path.rfind('\\') + 1:path.rfind('.')][0:3]
        print(name)
        epochs = mne.read_epochs(path, preload=True)
        epochs = epochs.apply_baseline(baseline=(-0.2, 0))
        for ma in mark:
            epoch_d=epochs[(epochs.metadata['event_name'] == '{}'.format(ma))]
            evoked_d=epoch_d.average()
            epoch_d.save(select_epoch_path + '\\{}_{}_epo.fif'.format(name,ma))
            evoked_d.save(evoked_path + '\\{}_{}_ave.fif'.format(name,ma))
