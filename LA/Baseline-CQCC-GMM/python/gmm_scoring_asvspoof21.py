from gmm import scoring


# scores file to write
scores_file = 'scores-cqcc-asvspoof21-LA.txt'

# configs
features = 'cqcc'
dict_file = 'gmm_cqcc_asvspoof21_la.pkl'

db_folder = '/home/sinhnta/ASV/Dataset/ASVspoof2021_LA_eval/'  # put your database root path here
eval_folder = db_folder + 'flac/'
eval_ndx = db_folder + 'ASVspoof2021.LA.cm.eval.trl.txt'

audio_ext = '.flac'

# run on ASVspoof 2021 evaluation set
scoring(scores_file=scores_file, dict_file=dict_file, features=features,
        eval_ndx=eval_ndx, eval_folder=eval_folder, audio_ext=audio_ext,
        features_cached=True)
