import json
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
from collections import defaultdict

# --- Open Files & Setup ---
melodyIndex = defaultdict(dict)
RefSegsTrue = defaultdict(dict)
PerSegsTrue = defaultdict(dict)
PerSegsFalse = defaultdict(dict)

# -- Import Json Files --
# array of json files, split into training and testing at around 80-20 %
json_files_all = ["511.json","512.json","521.json","522.json","531.json","532.json","541.json","542.json","551.json","552.json","561.json","562.json","571.json","572.json","581.json","582.json","5101.json","5102.json","611.json","612.json","621.json","622.json","631.json","632.json","641.json","642.json","651.json","652.json","661.json","662.json","671.json","672.json","681.json","682.json", "691.json", "692.json", "6101.json","6102.json"]

index = 0
for filenum in json_files_all:	# open json files for training
    with open(filenum, 'r') as file:
        data = file.read()
        # Make a dictionary with keys: melodyIndex | RefSegsTrue | PerSegsTrue | PerSegsFalse
        this_dict = json.loads(data)
        # Extract data from json fileinto separate variables
        melodyIndex[index] = this_dict['melodyIndex']
        RefSegsTrue[index] = this_dict['RefSegsTrue']
        PerSegsTrue[index] = this_dict['PerSegsTrue']
        PerSegsFalse[index] = this_dict['PerSegsFalse']
        index = index + 1

# Make a dictionary with keys:
#	melodyIndex | RefSegsTrue | PerSegsTrue | PerSegsFalse
this_dict = json.loads(data)

# Extract into separate variables
melodyIndex = this_dict['melodyIndex']
RefSegsTrue = this_dict['RefSegsTrue']
PerSegsTrue = this_dict['PerSegsTrue']
PerSegsFalse = this_dict['PerSegsFalse']

# --- Plot & Observe Data ---
plt.plot(RefSegsTrue[1],'-b', label='A Ref Seg')
plt.plot(PerSegsTrue[1],'-r', label='A Perf Seg (True)')
plt.plot(PerSegsFalse[1],'-g', label='A Perf Seg (False)')
plt.legend(loc='best')
plt.ylabel('Pitch (Cents)')
plt.xlabel('Time')
plt.show()

# ---- Analysis using Statistics----
# Pearson r, Compare true to refs, false to refs
true_max_inds = []
for pst in PerSegsTrue:
	corr_inds = [pearsonr(a,pst)[0] for a in RefSegsTrue]
	true_max_inds.append(max(corr_inds))

print("True Min:", min(true_max_inds))
print("True Max:", max(true_max_inds))
print("True Mean:", np.mean(true_max_inds))
print("True Median:", np.median(true_max_inds))

false_max_inds = []
for psf in PerSegsFalse:
	corr_inds = [pearsonr(a,psf)[0] for a in RefSegsTrue]
	false_max_inds.append(max(corr_inds))

print("False Min:", min(false_max_inds))
print("False Max:", max(false_max_inds))
print("False Mean:", np.mean(false_max_inds))
print("False Median:", np.median(false_max_inds))



