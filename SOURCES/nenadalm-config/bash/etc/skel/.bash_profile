
[[ -f ~/.bashrc ]] && . ~/.bashrc

export PATH=$PATH:$HOME/.local/bin:$HOME/bin

eval $(ssh-agent)

[[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && exec startx

