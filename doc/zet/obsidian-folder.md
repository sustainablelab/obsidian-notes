The **_.obsidian_** folder goes at the same level as the **_.git_** folder.  
  
For example, here is my [obsidian-template](https://github.com/sustainablelab/obsidian-template) Git repository:

```
$ tree ../obsidian-template/ -a
../obsidian-template/
├── .git <----------------- GIT
│   ├── COMMIT_EDITMSG
│  ...
│   └── refs
│       ├── heads
│       │   └── master
│       ├── remotes
│       │   └── origin
│       │       └── master
│       └── tags
├── .obsidian <------------ OBSIDIAN
│   ├── app.json
│   ├── appearance.json
│   ├── backlink.json
│   ├── core-plugins.json
│   ├── graph.json
│   ├── hotkeys.json
│   ├── themes
│   │   └── Obsidian gruvbox.css
│   └── workspace
├── graph.md
├── hotkeys.md
├── plugins.md
├── README.md
├── screen.md
├── settings.md
├── theme.md
└── usage.md
```