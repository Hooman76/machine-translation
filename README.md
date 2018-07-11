# machine-translation

machine translation subject:
  converting hafez poems to more understandable text

I used openNMT for training, preprocessing and testing my data.

I used crawler.py to gather hafez poems and OCR for gathering its meanings.

I used val_generator.py to generate val files which are used to validate target and source data.

A demo-model_step_5000.pt was created ( since 80 hours was needed to propperly train the model I only trained my model for the first
5000 steps ) this model is then used to test my data.

In order to use openNMT you first need to download or clone into openNMT.

for preprocessing data:
  python preprocess.py -train_src data/src-train.txt -train_tgt data/tgt-train.txt -valid_src data/src-val.txt -valid_tgt data/tgt-val.txt -save_data data/demo

for training data:
  python train.py -data data/demo -save_model demo-model

for testing:
  python translate.py -model demo-model_XYZ.pt -src data/src-test.txt -output pred.txt -replace_unk -verbose
