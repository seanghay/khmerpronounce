## Khmer Pronounce

A Khmer pronounciation toolkit trained on KhmerDictionary 2022 by Royal Academy of Cambodia (RAC) with Phonetisaurus.

```shell
pip install khmerpronounce
```

```python
from khmerpronounce import pronounce

result = pronounce("សម្ដេចបវរធិបតី")
# => ['សំ', 'ដាច់', 'ប', 'វ៉', 'ធិ', 'ប៉ៈ', 'ដី']

result = pronounce("មករា")
# => ['មៈ', 'កៈ', 'រ៉ា']
```