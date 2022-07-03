CONV=python tools/subword2char.py
DEV_RAW=../raw-sent/dev-raw-sent.tsv
TRAIN_RAW=../raw-sent/train-raw-sent.tsv
DEV_SUBWORD=ne-150-subword-bio/ne-dev-150-subword-bio.tsv
TRAIN_SUBWORD=ne-150-subword-bio/ne-train-150-subword-bio.tsv

all: dev train

dev: ne-dev-150-char-bio.tsv

train: ne-train-150-char-bio.tsv

valid: dev-valid train-valid

dev-valid: ne-dev-150-char-bio-valid.tsv

train-valid: ne-train-150-char-bio-valid.tsv

ne-dev-150-char-bio.tsv: $(DEV_RAW) $(DEV_SUBWORD)
	$(CONV) conv $(DEV_RAW) $(DEV_SUBWORD) > $@

ne-train-150-char-bio.tsv: $(TRAIN_RAW) $(TRAIN_SUBWORD)
	$(CONV) conv $(TRAIN_RAW) $(TRAIN_SUBWORD) > $@

ne-dev-150-char-bio-valid.tsv: $(DEV_RAW) $(DEV_SUBWORD)
	$(CONV) valid $(DEV_RAW) $(DEV_SUBWORD) > $@

ne-train-150-char-bio-valid.tsv: $(TRAIN_RAW) $(TRAIN_SUBWORD)
	$(CONV) valid $(TRAIN_RAW) $(TRAIN_SUBWORD) > $@

