.gitconfig

```
[alias]
	p = push
	st = status -sb
	ll = log --oneline
	lg = log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
	last = log -1 HEAD --stat
	cm = commit -m
	ucm = reset --soft HEAD~1
	ac = !git add -A && git commit -m
	rv = remote -v
	smu = submodule update --init --recursive
	rst = !git clean -xfd                                    \
	   && git submodule foreach --recursive git clean -xfd   \
	   && git reset --hard                                   \
	   && git submodule foreach --recursive git reset --hard \
	   && git submodule update --init --recursive
	amend = commit --amend --no-edit

	# Clean up branches that have been merged into master.
	clean-branches = !git branch --merged master | grep -v 'master$' | xargs -n 1 git branch -d

	#Worktrees
	wa = worktree add
	wl = worktree list
	wr = "!f() { git worktree remove \"$1\" && rm -rf \"$1\"; }; f"

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