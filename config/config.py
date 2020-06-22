import os

__all__ = ['model_config', 'data_config', 'ENGINE']

ENGINE = 'xgb'

default_model_config = {
    'tree_method': 'hist',
    'auto__max_bin': [256, 512],
    'booster': 'gbtree',
    'objective': 'rank:pairwise',
    'eta': 0.1,
    'auto__gamma': [0.5, 1.0],
    'min_child_weight': 5,
    'max_depth': 8,
    'eval_metric': ['map', 'ndcg@2', 'ndcg@4', 'ndcg@6', 'ndcg'],
    'nthread': 32}

train_data_dir = '/home/zhangxian05/data/latest/train/'
valid_data_dir = '/home/zhangxian05/data/latest/valid/'

default_data_config = {
    'train': {
        'gt': {
            'gt_file': os.path.join(train_data_dir, "gt.txt"),
            'separator': '\t',
            'rank_label_column': 0,
            'query_session_column': -1
        },
        'features': [{  # topic features, each line contains a photo's text and query joint features.
            'feat_file': os.path.join(train_data_dir, "topic_features.txt"),
            'attach_column': [2, 1],
            'feat_length': 21,
            'feat_format': 'topic',
            'separator': '\t',
            'feat_type': float,
            'categorical_feature': []
        }]
    }
}

if valid_data_dir:
    default_data_config.update({
        'valid': {
            'gt': {
                'gt_file': os.path.join(valid_data_dir, "gt.txt"),
                'separator': '\t',
                'rank_label_column': 0,
                'query_session_column': -1
            },
            'features': [{  # topic features, each line contains a photo's text and query joint features.
                'feat_file': os.path.join(valid_data_dir, "topic_features.txt"),
                'attach_column': [2, 1],
                'feat_length': 21,
                'feat_format': 'topic',
                'separator': '\t',
                'feat_type': float,
                'categorical_feature': []
            }]
        }})

model_config = default_model_config
data_config = default_data_config
