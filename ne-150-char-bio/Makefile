CONV=python tools/subword2char.py
DEV_RAW=../raw-sent/dev-raw-sent.txt
TRAIN_RAW=../raw-sent/train-raw-sent.txt
DEV_SUBWORD=ne-150-subword-bio/ne-dev-150-subword-bio.txt
TRAIN_SUBWORD=ne-150-subword-bio/ne-train-150-subword-bio.txt

all: dev train

dev: ne-dev-150-char-bio.txt

train: ne-train-150-char-bio.txt

valid: dev-valid train-valid

dev-valid: ne-dev-150-char-bio-valid.txt

train-valid: ne-train-150-char-bio-valid.txt

ne-dev-150-char-bio.txt: $(DEV_RAW) $(DEV_SUBWORD)
	$(CONV) conv $(DEV_RAW) $(DEV_SUBWORD) > $@

ne-train-150-char-bio.txt: $(TRAIN_RAW) $(TRAIN_SUBWORD)
	$(CONV) conv $(TRAIN_RAW) $(TRAIN_SUBWORD) > $@

ne-dev-150-char-bio-valid.txt: $(DEV_RAW) $(DEV_SUBWORD)
	$(CONV) valid $(DEV_RAW) $(DEV_SUBWORD) > $@

ne-train-150-char-bio-valid.txt: $(TRAIN_RAW) $(TRAIN_SUBWORD)
	$(CONV) valid $(TRAIN_RAW) $(TRAIN_SUBWORD) > $@

