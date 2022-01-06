# Command history tweaks:
# - Append history instead of overwriting
#   when shell exits.
# - When using history substitution, do not
#   exec command immediately.
# - Do not save to history commands starting
#   with space.
# - Do not save duplicated commands.
shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth

# Default command line prompt.
PROMPT_DIRTRIM=2
#PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '
PS1='\[\e[38;5;9m\]\[\e[1m\]┌─[\[\e[38;5;14m\]\[\e[1m\]<———(••\[\e[0m\]\[\e[38;5;9m\] \[\e[3m\]\[\e[1m\]SWEET\[\e[0m\]\[\e[38;5;202m\]\[\e[3m\]\[\e[1m\]ERROR\[\e[0m\]\[\e[38;5;203m\]\[\e[3m\]\[\e[1m\]404\[\e[0m\] \[\e[38;5;14m\]\[\e[1m\]••)———>\[\e[0m\]\[\e[38;5;9m\]]─[\[\e[38;5;46m\]\e[1m\]\e[3m\]\w\[\e[0m\]\[\e[38;5;9m\]\e[1m\]]\n\[\e[38;5;9m\]└──╼ \[\e[38;5;11m\]\$\[\e[0m\] '

# Handles nonexistent commands.
# If user has entered command which invokes non-available
# utility, command-not-found will give a package suggestions.
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
	command_not_found_handle() {
		/data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
	}
fi
clear
