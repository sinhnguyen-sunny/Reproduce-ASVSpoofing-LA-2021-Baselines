from gmm import scoring


# scores file to write
scores_file = 'scores-lfcc-asvspoof21-LA.txt'

# configs
features = 'lfcc'
dict_file = 'gmm_lfcc_asvspoof21_la.pkl'
db_folder = '/media/SSD/sinhnta/'  # put your database root path here
# eval_folder = db_folder + 'LA/ASVspoof2021_LA_eval/flac/'
# eval_ndx = db_folder + 'LA/ASVspoof2021_LA_cm_protocols/ASVspoof2021.LA.cm.eval.trl.txt'
eval_folder = db_folder + 'ASVspoof2021_LA_eval/flac/'
eval_ndx = db_folder + 'ASVspoof2021_LA_eval/ASVspoof2021.LA.cm.eval.trl.txt'

audio_ext = '.flac'

# run on ASVspoof 2021 evaluation set
scoring(scores_file=scores_file, dict_file=dict_file, features=features,
        eval_ndx=eval_ndx, eval_folder=eval_folder, audio_ext=audio_ext,
        features_cached=True)
