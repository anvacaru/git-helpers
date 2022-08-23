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

[selector](./scripts/selector): computes the selector of a Solidity function using [getSelector.py](./scripts/python/bin/getSelector.py)

requirements
```
pip3 install pycryptodome
```