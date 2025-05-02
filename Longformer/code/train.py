import os

os.system("CUDA_VISIBLE_DEVICES=0 python run_longformer.py \
        --output_dir=saved_models/MutantEq \
        --config_name=allenai/longformer-base-4096\
        --model_name_or_path=allenai/longformer-base-4096 \
        --tokenizer_name=allenai/longformer-base-4096\
        --requires_grad 0 \
        --do_train \
        --code_db_file=../../dataset/EFSM_single/code_db_full.csv \
        --train_data_file=../../dataset/EFSM_single/pairwise_train_full.csv \
        --eval_data_file=../../dataset/EFSM_single/pairwise_test_full.csv \
        --test_data_file=../../dataset/EFSM_single/pairwise_test_full.csv 2>&1")