#!/bin/bash

tar zxvf datasets.tar.gz

[ -d './.venv/' ] && python3 -m venv .venv/

. .venv/bin/activate
python3 -m pip install -r ./requirements
python3 extract_lists.py
python3 make_training_dataset.py
python3 train_model.py

tar zcvf out.tar.gz symptoms_list.txt disease_list.txt model.bin
