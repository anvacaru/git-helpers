
# export KERC=/home/anvacaru/rv/erc20-verification
# export IELE=/home/anvacaru/rv/iele-semantics

# KEVM
export KEVM=/home/anvacaru/rv/evm-semantics
export PATH=$KEVM/.build/usr/bin:$PATH

# Stack
export PATH=/home/anvacaru/.local/bin:$PATH

# Maven
# FOR OLD K VERSIONS export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export JAVA_HOME=/usr/lib/jvm/java-1.11.0-openjdk-amd64
export MAVEN_OPTS=-XX:+TieredCompilation

# Kiele
export PATH=/home/anvacaru/rv/k/k-distribution/target/release/k/bin:$PATH
# export PATH=/home/anvacaru/rv/iele-semantics:$PATH
# export OPAMROOT=/usr/lib/kframework/opamroot
# export PYTOHNPATH=/home/anvacaru/rv/iele-semantics
# export FIREFLY_TOKEN="Qkd4VTN6NTBDNThyYThybTMvNkVEVS9XTW5aNjZpZzZkNmVzdVhJdmRQaz0="

#ISOLC
#export PATH=/home/anvacaru/rv/solidity/build/solc:$PATH

# ERC20
#export PATH=/home/anvacaru/rv/erc20-verification/.build/usr/bin:$PATH

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# scripts
export PATH=/home/anvacaru/scripts:$PATH
alias time='command time'

#export PATH="$PATH:/home/anvacaru/.foundry/bin"


# git bisect utils
export PATH=/home/anvacaru/scripts/git/bin:$PATH
. "$HOME/.cargo/env"

#ALCHEMY API KEY
export ALCHEMY_API_KEY=R8t-v7z5oBm7IdOEI7iP8jdXW3tyTLc5
