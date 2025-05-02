import os

os.system("CUDA_VISIBLE_DEVICES=0 python run.py \
        --output_dir=../saved_models/MutantEq\
        --config_name=microsoft/unixcoder-base\
        --model_name_or_path=microsoft/unixcoder-base \
        --tokenizer_name=microsoft/unixcoder-base\
        --requires_grad 0 \
        --do_test \
        --code_db_file=../../dataset/EFSM_single/code_db.csv \
        --train_data_file=../../dataset/EFSM_single/pairwise_train.csv \
        --eval_data_file=../../dataset/EFSM_single/pairwise_test.csv \
        --test_data_file=../../dataset/EFSM_single/pairwise_test.csv 2>&1")
