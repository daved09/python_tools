#!/usr/bin/fish
set VENV (dirname (status -f))/.venv/bin

if not test -d $VENV
    python -m venv .venv
    chmod -R +x .venv
end

source $VENV/activate.fish