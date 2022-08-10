# Animal Language

Customize a word set, and then use the words in this set to represent any sentence.

Also provide a JavaScript version to play online. See [动物语翻译器](https://chnzzh.github.io/animal-language). 

JS code in [docs/alcore.js](./docs/alcore.js)

## Install

```
pip install --upgrade animal-language
```

## Usage

To encode a sentence with these characters and words:

`m, oo, b, aa, z`

(or use moo, baa, zzz, but it will increase the encoded string's length)


### 1) Create a Translater

```python
from animal_language import ALTranslater

translater = ALTranslater(['m', 'oo', 'b', 'aa', 'z'])
```

### 2) Encode Any String

use the translater to encode any string you want.

```python
encoded_str = translater.encode('hello, this is a test')
```

The encoded_str will be like :

`oooombbooboozmmbaabbmooaaoobaambzzooaaaaaazmbmbooaam`

### 3) Decode the Encoded String

Also use the translater to decode the encoded_str.

```python
decoded_str = translater.decode(encoded_str)
```

The decoded_str is equal to the string you encoded


## Other Information

+ The word list must be like "prefix codes", lists like `['a', 'ab']` will not supported.
+ You can set the encoding of the input string.
+ JUST HAVE FUN AND ENJOY THIS bmoooombaaooooaambooz !