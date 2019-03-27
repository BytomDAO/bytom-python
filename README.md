pybtm
======

- [1 Installation](#1-installation)
- [2 Usage](#2-usage)
  - [2.1 Create entropy](#21-create-entropy)
  - [2.2 Create mnemonics](#22-create-mnemonics)
  - [2.3 Create seed](#23-create-seed)
  - [2.4 Create root expanded private key](#24-create-root-expanded-private-key)
  - [2.5 Create expanded public key](#25-create-expanded-public-key)

Python3 implementation of the Bytom protocol.

## 1 Installation

```
$ pip install pybtm
```

## 2 Usage

### 2.1 Create entropy

get_entropy() create 128 bits entropy.

```python
>>> from pybtm import key
>>> key.get_entropy()
'100e2704b431f914e3262926bdba6fce'
```

### 2.2 Create mnemonics

get_mnemonic create 12 new mnemonics.

```python
>>> key.get_mnemonic('089fe9bf0cac76760bc4b131d938669e')
'ancient young hurt bone shuffle deposit congress normal crack six boost despair'
```

If no paramater is specified, it will return 12 new random mnemonics.

```python
>>> from pybtm import key
>>> key.get_mnemonic()
'nothing gate perfect glide wink lizard journey negative load quote wrong reason'
```

### 2.3 Create seed

get_seed create 512 bits seed from 12 mnemonics.

```python
>>> from pybtm import key
>>> key.get_seed('ancient young hurt bone shuffle deposit congress normal crack six boost despair')
'afa3a86bbec2f40bb32833fc6324593824c4fc7821ed32eac1f762b5893e56745f66a6c6f2588b3d627680aa4e0e50efd25065097b3daa8c6a19d606838fe7d4'
```

### 2.4 Create root expanded private key

get_root_xprv create root expanded private key.

```python
>>> from pybtm import key
>>> key.get_root_xprv('afa3a86bbec2f40bb32833fc6324593824c4fc7821ed32eac1f762b5893e56745f66a6c6f2588b3d627680aa4e0e50efd25065097b3daa8c6a19d606838fe7d4')
'302a25c7c0a68a83fa043f594a2db8b44bc871fced553a8a33144b31bc7fb84887c9e75915bb6ba3fd0b9f94a60b7a5897ab9db6a48f888c2559132dba9152b0'
```

### 2.5 Create expanded public key

get_xpub create expanded public key.

```python
>>> from pybtm import key
>>> key.get_xpub('c003f4bcccf9ad6f05ad2c84fa5ff98430eb8e73de5de232bc29334c7d074759d513bc370335cac51d77f0be5dfe84de024cfee562530b4d873b5f5e2ff4f57c')
'1b0541a7664cee929edb54d9ef21996b90546918a920a77e1cd6015d97c56563d513bc370335cac51d77f0be5dfe84de024cfee562530b4d873b5f5e2ff4f57c'
```