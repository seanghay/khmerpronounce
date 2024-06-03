import re
from sosap import Model
import csv
import os

pat = re.compile(r"[^\u1780-\u17ff]+")
model_path = os.path.join(os.path.dirname(__file__), "model.fst")
lexicon_path = os.path.join(os.path.dirname(__file__), "lexicon.tsv")
model = Model(model_path)

with open(lexicon_path) as fp:
  reader = csv.reader(fp, delimiter="\t")
  lexicon_dict = {item[0]: item[1].split() for item in reader}

def pronounce(text: str):
  text = pat.sub("", text).strip()
  if text in lexicon_dict:
    return lexicon_dict[text]
  return model.phoneticize(text)
