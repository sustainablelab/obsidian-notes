# Open the documentation

`F1` within a vault opens the documentation.

The documentation is also here: https://help.obsidian.md

On Windows, this Obsidian help vault is located in the `AppData\Roaming\obsidian` folder.

That folder contains lots of interesting stuff:

- `obsidian.json` is the list of registered vaults
- `obsidian.log` is a log of all of the things Obsidian does behind the scenes to maintain itself
# Rename an internal link

I use internal links `[[like-this]]` as nodes to define
connections. These are empty files.

To rename the link:

- click on the node in graph view
    - this creates a file
    - the file is opened in a new pane
- edit the file title
    - this updates all internal links
- delete the file
- close the pane

# Shortcut to open vault

I setup two shortcuts to launch Obsidian with whatever vault is
in my *present working directory* (`pwd`).

Vim shortcut using the directory of the active buffer:

```vim
nnoremap <leader>oh :!powershell.exe 'Start-Process obsidian:///"$(cygpath -ma %:p:h)"'<CR>
```

Bash alias using the pwd:

```bash
alias obsidian='powershell.exe "Start-Process obsidian:///$(cygpath -ma .)"'
```

Read the details of this in [[open-vault-by-uri]].

