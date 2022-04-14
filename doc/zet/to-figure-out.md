# Base workspace

How do I set up my Obsidian vault to behave like the
three-pane vault template here:
https://help.obsidian.md/Start+here

Specifically, I like the behavior of the three panes:

- there's a vault-wide toc on left
- there's a local graph and local toc on right
- whatever I click, it loads into the middle pane

Solved:

Use the Outline plugin. Start with a graph view, pin it, click on a Node, this opens the file in another pane, right-click on the Node to open the Outline, right-click again to open the Local Graph, reposition all these, then finally use Link pane to link the outline and the local graph to the file. 

Now turn on the Workspaces plug-in. Use workspaces to flip between a few different setups like this.

# Graph workspace

Now what I want is:

- a global graph view where:
    - when I click on a node I get the local graph view for that node
    - and when I click on another node, it loads its local graph view into that same local graph view pane