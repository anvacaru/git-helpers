.gitconfig

```
[alias]
	p = push
	st = status -sb
	ll = log --oneline
	last = log -1 HEAD --stat
	cm = commit -m
	rv = remote -v
    smu = submodule update --init --recursive
	rst = !git clean -xfd                                    \
	   && git submodule foreach --recursive git clean -xfd   \
	   && git reset --hard                                   \
	   && git submodule foreach --recursive git reset --hard \
	   && git submodule update --init --recursive
[user]
	email = andrei.vacaru@runtimeverification.com
	name = Andrei
```

- [selector](./scripts/selector): computes the selector of a Solidity function using [getSelector.py](./scripts/python/bin/getSelector.py).
Requirements:
```
pip3 install pycryptodome
```

- [readBytes](./scripts/readBytes): takes a string of bytes and displays them in Int and Hexadecimal format using [readBytes.py](./scripts/python/bin/readBytes.py).
- [build-kontrol](./build-kontrol): locally building kontrol according to the [readme](https://github.com/runtimeverification/kontrol#build-from-source) instructions.