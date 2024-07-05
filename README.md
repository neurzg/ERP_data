EEG data were processed using MNE, a python-based software for physiological signal analysis (Gramfort et al., 2013).
Initially, any faulty channels identified through visual inspection were interpolated based on the signals from neighboring sensors deemed as reliable. 
Subsequently, the continuous EEG data were re-referenced using the average of bilateral mastoid electrodes and filtered with a cutoff frequency ranging from 0.1 to 30 Hz. 
The EEG data from 200 ms before and 1000 ms after stimulus onset were extracted and segmented into epochs. 
To mitigate muscle artifacts present in the EEG signal, such as eye movements and blinks, independent component analysis was conducted (Ablin et al., 2018), and epochs with significant artifacts were identified using the autoreject package (Jas et al., 2017). 
The EEG data from -200 ms before the onset of stimulus were used as a baseline for correcting the epochs. 
Finally, the epochs were averaged to extract the time-locked ERPs of each participant for all stimuli.
To investigate specific components of interest, mean amplitudes of the N1 and P3 components were measured at the frontal and parietal/occipital regions, respectively. 
The N1 component was measured at the FP1, FPZ, FP2, F3, FZ, and F4 electrode sites in the 80–120 ms time window, 
whereas the P3 component was measured at the PO3, POZ, PO4, O1, OZ, and O2 electrode sites in the 200–400 ms time window. 
In addition, the N170 component was measured at the P8 electrode site in the 140–180 ms time window.
