import mne
import matplotlib
from mne.preprocessing import ICA
import os
from matplotlib import pyplot as plt
from autoreject import AutoReject

matplotlib.use('TkAgg')

ica_path=r'D:\pythonProject\ERP\ica'
metadata_path=r'D:\pythonProject\ERP\metadata'
epochs_ica_path=r'D:\pythonProject\ERP\epochs_ica_path'
epochs_path=r'D:\pythonProject\ERP\epochs_path'
epochs_clean_path=r'D:\pythonProject\ERP\epochs_clean_path'

if os.path.exists(ica_path):
    pass
else:
    os.mkdir(ica_path)

if os.path.exists(metadata_path):
    pass
else:
    os.mkdir(metadata_path)

if os.path.exists(epochs_ica_path):
    pass
else:
    os.mkdir(epochs_ica_path)

if os.path.exists(epochs_path):
    pass
else:
    os.mkdir(epochs_path)

if os.path.exists(epochs_clean_path):
    pass
else:
    os.mkdir(epochs_clean_path)

locs_info_path = 'standard.elp'
montage = mne.channels.read_custom_montage(locs_info_path)

Participate=['01', '02', '03', '04', '05', '06', '07', '08', '09','10',
             '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
             '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
             '31', '32', '33', '34', '35', '36', '37']
# Participate = ['01']
for par in Participate:
    par_name='P{}'.format(par)
    print(par_name)
    path = r'D:\ERP\{}\Acquisition 01.dat'.format(par)
    raw = mne.io.read_raw_curry(path, preload=True)

    raw.drop_channels('Trigger')
    raw.set_channel_types({'HEO': 'eog', 'VEO': 'eog'})

    raw = mne.add_reference_channels(raw, ref_channels=['M1'])
    raw = raw.set_eeg_reference(ref_channels=['M1', 'M2'])
    raw.set_montage(montage)

    raw = raw.resample(sfreq=250)

    raw = raw.notch_filter(freqs=(50))
    raw = raw.filter(l_freq=0.1, h_freq=30)
    raw.drop_channels(['M1','M2'])

    events, event_id = mne.events_from_annotations(raw)
    metadata_tmin, metadata_tmax = 0, 1.5
    row_events = ['1', '5', '9',  '13', '17', '21']

    metadata, events, event_id = mne.epochs.make_metadata(
        events=events, event_id=event_id,
        tmin=metadata_tmin, tmax=metadata_tmax, row_events=row_events,sfreq=raw.info['sfreq'])
    df_metadata=metadata.copy()
    df_metadata['name']= par_name

    df_metadata.to_csv(metadata_path + '\\{}.txt'.format(par_name),sep='\t')

    epochs_tmin, epochs_tmax = -0.2, 1
    baseline = (0, 0)

    epochs = mne.Epochs(raw=raw, tmin=epochs_tmin, tmax=epochs_tmax,
                        baseline=baseline,
                        events=events, event_id=event_id, metadata=metadata,
                        preload=True)
    epochs.save(epochs_path + '\\{}_epo.fif'.format(par_name), overwrite=True)

    ica = ICA(max_iter='auto')
    raw_for_ica = epochs.copy().filter(l_freq=1, h_freq=None)
    ica.fit(raw_for_ica)
    ica.exclude = []
    eog_indices, eog_scores = ica.find_bads_eog(raw_for_ica)
    ica.exclude = eog_indices
    ica.detect_artifacts(raw_for_ica)
    ica.apply(epochs)
    ica.save(ica_path + '\\{}ica.fif'.format(par_name), overwrite=True)
    epochs.save(epochs_ica_path + '\\{}ica_epo.fif'.format(par_name), overwrite=True)

    ar = AutoReject()
    epochs_clean = ar.fit_transform(epochs)
    epochs_clean.save(epochs_clean_path + '\\{}epo.fif'.format(par_name), overwrite=True)

