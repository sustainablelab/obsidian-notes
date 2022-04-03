# Shortcut to open vault

I setup two shortcuts to launch Obsidian with whatever vault is
in my *present working directory* (`pwd`).

## What problem this solves

Launching Obsidian opens the last used vault. From there I have
to go `Open another vault`, then scroll the list of vaults.

I use a lot of vaults, so this method is unacceptable. I want a
keyboard shortcut or a cmdline command to launch a specific
vault.

### Why do I use so many vaults?

I have one vault per Git repository. See file: [[graph-view-animation]].

### What does a typical repo-with-vault look like?

I put my .obsidian vault folder at the same level as my .git
folder. See file: [[obsidian-folder]].


## Solution is to use the Obsidian URI

- I describe the shortcut functionality I want
- then I give some examples using the URI
- then finally I show how I setup shortcuts with the URI

### Functionality Sketch

The ideal way for me to open an Obsidian vault is like this:

- I am in Vim or bash
- the `pwd` (present working directory) is somewhere within a Git
  repository
- the repository has my `.obsidian` vault
- I hit my shortcut:
    - Vim shortcut `;oh` (pneumonic: *Obsidian Here*)
    - or bash alias `obsidian`
- the Obsidian vault opens up *for the project I am inside of*

### How to use the Obsidian URI

Use the custom URI protocol to interact with Obsidian from
PowerShell (or any cmdline). The URI protocol is an address that
starts like this:

```uri-base-address
obsidian://
```

The address then has:

- an action
    - "open", "search", "new", or "hook-get-address"
    - parameters for the action, like this:

    ```uri-action-param-syntax
    obsidian://action?param1=value&param2=value
    ```

- or the URI address is just a folder-path or file-path
    - in this case, the URI uses the default "open" action

And this *just-a-path* form of the URI has two forms:

- it can use a short-hand Obsidian path (note the two slashes):

```
obsidian://vault/name-of-my-vault
```

- or an absolute path (note the three slashes):

```
obsidian:///absolute/path/to/name-of-my-vault
```

When opening a path, the path can be to a vault folder:

- this opens a new instance of Obsidian with that vault
- or, if that vault is already open, the OS switches to that open vault

Or the path can be to a specific file

- *I haven't tried but I'm guessing this opens the file in
  whatever vault is currently open?*

See the documentation: https://help.obsidian.md/Advanced+topics/Using+obsidian+URI

### Examples opening vaults by URI

On Windows, I could only figure out one way to use the Obsidian URI.

From PowerShell, I use the `Start-Process` cmdlet:

```powershell
Start-Process "obsidian://"
```

This example (using the empty URI) is equivalent to running
`Obsidian.exe`, i.e., it just opens the last-used file.

Not particularly useful. But this example shows the basic idea: pass the URI as a string to the Start-Process cmdlet.

Great, but I don't do much from PowerShell. I launch Cygwin bash and do everything from there. So how do I call PowerShell cmdlets from within Cygwin?

PowerShell cmdlets are not stand-alone executables; [they are
instances of .NET
classes](https://docs.microsoft.com/en-us/powershell/scripting/developer/cmdlet/cmdlet-overview?view=powershell-7.2).
This means I can't call `Start-Process` from Cygwin bash:

```bash
$ Start-Process "obsidian://"
-bash: Start-Process: command not found
```

But I can run a PowerShell script from Cygwin bash. Wait, what?
Yes, this blew my mind the first time I tried it. From PowerShell
I launch Cygwin bash. Then from my Cygwin bash terminal, I launch
PowerShell:

```bash
$ powershell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

For bash terminal applications like Vim: ctrl+z freezes to term, command fg resumes.
See --- >^.^< shortcuts >^.^< ---
Drive already SUBSTed
PS C:\cygwin64\home\mike> exit

$
```

What happened there? I was in Cygwin bash. I ran
`powershell.exe`. This started a PowerShell prompt inside Cygwin!
Then I exited back out to Cygwin bash.

If I *pass a string argument* to `powershell.exe` I get something
really useful.

Instead of opening a PowerShell prompt, now this command:

- starts up a new PowerShell process
- that process does whatever argument I say in the string
- then the process exits back to Cygwin bash

This is great. This means I can open an Obsidian vault using the
URI protocol *from within Cygwin* (i.e., at a bash cmdline or
within Vim).

For example, in my "programming" repository:

```bash
$ powershell.exe 'Start-Process "obsidian://vault/programming"'
For bash terminal applications like Vim: ctrl+z freezes to term, command fg resumes.
See --- >^.^< shortcuts >^.^< ---
Drive already SUBSTed
```

This usage of the URI is the "short form" (as described at the
end in the documentation). This is handy if I'm typing in the
command manually.

But to automate this (I eventually want it to use whatever path
I'm in), I need to use the absolute path syntax of the URI `open`
action:

```
$ powershell.exe 'Start-Process obsidian:///"$(cygpath -ma /cygdrive/c/cygwin64/home/mike/gitrepos/programming)"'
```

What is going on there? I'll explain this in detail, but first
see what the `$(blah)` expression evaluates to:

```bash
$ echo "$(cygpath -ma /cygdrive/c/cygwin64/home/mike/gitrepos/programming)"
C:/cygwin64/home/mike/gitrepos/programming
```

- `cygpath` is a utility that converts between POSIX-style and Windows-style paths
- the -a flag says "give me the absolute path"
- the -m flag says make the style "mixed":
    - get the Windows-style paths
    - but use forward slashes (POSIX-style) instead of
      backslashes (Windows-style)
    - normally I use -w to get the Windows-style path but
      Obsidian on Windows uses this mixed-style path
    - fwiw, I see this mixed-style flavor in Godot as well
- I use the string output of `cygpath` by wrapping the expression
  blah like this: `$(blah)`
- I put that in double-quotes in case the Windows-style path
  contains spaces
- that string just concatenates onto the `obsidian:///` URI
  address
    - use three forward slashes after `obsidian:` instead of two
      forward slashes
    - this indicates the URI address is an absolute path, not an
      Obsidian path

Before automating this for the `pwd`, I get a working version of
this shortcut to work *for this specific vault*.

### Shortcuts to a specific vault

*I make shortcuts to my `programming` vault.*

#### Vim

Vim shortcut (in my `.vimrc`):

```vim
nnoremap <leader>oh :!powershell.exe 'Start-Process obsidian:///"$(cygpath -ma /cygdrive/c/cygwin64/home/mike/gitrepos/programming)"'<CR>
```

#### Bash

Bash alias (in my `.bashrc`):

```bash
alias obsidian='powershell.exe "Start-Process obsidian:///$(cygpath -ma /cygdrive/c/cygwin64/home/mike/gitrepos/programming)"'
```

#### Dealing with quotes in aliases

The Vim shortcut worked on the first try because Vim shortcuts
don't require quotes.

But bash aliases do require quotes. I couldn't figure out how to
maintain the original two levels of quotes with one level used
up by the alias.

- the alias goes inside quotes
- so I had to drop the quotes around the `$(blah)`
- this means the alias will break if the string returned by
  `cygpath` contains spaces

**I don't put spaces in my folder names anyway, so this problem
should never come up.**

### Shortcuts to the vault in the pwd

Now just take the hardcoded path from the previous example and
replace with the syntax for the `pwd`.

#### Vim

*Vim shortcut using the `pwd`:*

```vim
nnoremap <leader>oh :!powershell.exe 'Start-Process obsidian:///"$(cygpath -ma %:p:h)"'<CR>
```
In Vim cmdline syntax, `%:p:h` is the absolute path to the `pwd`.
Test this with:

```vim
:echo expand("%:p:h")
```

#### Bash

Bash alias using the `pwd`:

```bash
alias obsidian='powershell.exe "Start-Process obsidian:///$(cygpath -ma .)"'
```

In bash (and every command line I've ever used), `.` refers to the `pwd`.

Using the bash alias looks like this:

```bash
$ cd gitrepos/programming/
$ obsidian
For bash terminal applications like Vim: ctrl+z freezes to term, command fg resumes.
See --- >^.^< shortcuts >^.^< ---
Drive already SUBSTed
```

### Initialize vault if shortcut fails

- If I'm in a folder with a **registered** `.obsidian` folder,
  the vault opens.
- If not, I get a pop-up window with an error message telling me
  **there is no vault here.**

What do I mean by *registered* `.obsidian` folder?

Merely having a `.obsidian` folder is not enough for Obsidian to
find it. Obsidian has a list of known vaults in:

```
AppData\Roaming\obsidian\obsidian.json
```

For example, here is that path on my computer:

```
C:\Users\mike\AppData\Roaming\obsidian\obsidian.json
```

I could check if the vault is in that file and then edit the
JSON. But I'm too lazy to create this fix.

For now, I **initialize** the vault like this:

- let the attempt to open the vault via the shortcut fail (get
  the error message)
- Obsidian will still open, but it will open on the last-used
  vault
- Click *Open another vault*
    - the vault will not be listed
    - set up the vault the usual way:
        - act as if creating a new vault from an existing folder
        - browse to the folder that contains the `.obsidian` folder
        - hit OK or whatever
- *that registers the vault in `AppData\Roaming\obsidian\obsidian.json`*
- now I can open the vault using my shortcuts


