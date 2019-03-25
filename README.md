pybtm
======

- [1 Installation](#1-installation)
- [2 Usage](#2-usage)
  - [2.1 Create entropy](#21-create-entropy)
  - [Create mnemonics](#create-mnemonics)

Python3 implementation of the Bytom protocol.

## 1 Installation

```
$ pip install pybtm
```

## 2 Usage

### 2.1 Create entropy

get_entropy() create 128bits entropy.

```python
>>> from pybtm import key
>>> key.get_entropy()
'100e2704b431f914e3262926bdba6fce'
```

### Create mnemonics

get_mnemonic create 12 new mnemonics, if no paramater is specified, it will return 12 new random mnemonics.

```python
>>> from pybtm import key
>>> key.get_mnemonic()
'nothing gate perfect glide wink lizard journey negative load quote wrong reason'
>>> key.get_mnemonic('089fe9bf0cac76760bc4b131d938669e')
'ancient young hurt bone shuffle deposit congress normal crack six boost despair'
```