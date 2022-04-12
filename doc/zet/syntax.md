# Internal link

Anything in double square brackets, anywhere it occurs, is an
internal link:

```
[[i-am-an-internal-link]]
```

https://help.obsidian.md/How+to/Internal+link

Also see:

- https://help.obsidian.md/How+to/Internal+link#Link+to+headings
- https://help.obsidian.md/How+to/Link+to+blocks

# Tag

## Tags start with `#`
Anything with a single `#` prefix is a tag:

```
#i-am-a-tag
# i-am-not-a-tag
##i-too-am-not-a-tag
```

Use tags for "central nodes", don't use links to empty files for "central nodes".

## Nested tags use `/`
Create nested tags:

```
#fpga/learn/verilog-syntax
#fpga/dev-brd/digilent
```

Why?

This shows up in tags pane as a folder tree.

So what?

Now I can organize tags. That means I can organize my content by organizing tags. I use vimgrep to quickly update the tags in all the files as I play with the organization.

## What can I do with nested tags?

Nested tags impose a hierarchy for filtering the graph view.

### Filter nodes by nested tags

Searching for the parent of a nested tag gives all tags with that parent.

- Example, I have these two nested tags:
    - `#fpga/learn/verilog-syntax`
    - `#fpga/learn/start-here` 
- I click on `learn` in the **Tags** window
    - All nodes with the two tags above are listed in the **Search** window.
- I then paste that **Search** expression in the graph view **Filter**:
    - the graph only shows nodes that match the search
    - or if I put a `-` sign in front, I can make the graph *exclude* only the nodes that match the search

### Do not impose node hierarchy this way

Impose a hierarchy. Doesn't that defeat the point of the second brain? No. It's true I don't want to be forced to organize until I'm ready. But I also don't want to be prevented from organizing.

*I experimented with giving tags a parent node following the form `-1-`, `-2-`, etc. as parents for nodes I want to put in a hierarchy. I decided it was better to impose this structure with files.*

For the experiment, I have:

```
#-1-/fpga
#-1-/design
```

These are hierarchical, top-level nodes. 

I was originally using links to non-existent files for this purpose. But there is no filter based on non-existent files. And there is filtering for tags. Hence this. And the nesting feature makes this nice.

I also like that this lets free-form nodes sit side-by-side with hierarchical nodes. The hierarchy helps by giving me a way to control the graph. But it does so without getting in the way because it doesn't force me to decide where things belong in the hierarchy.

The trouble with this approach is that there is no way to impose links between tags.

So use tags for what they are good for: searching and filtering. Use files for what they are good for: imposing a structure in the links.
    
# Control node placement     

- Example, I have these two nested tags:
    - `#fpga/learn/verilog-syntax`
    - `#fpga/learn/start-here` 
- Sharing the same parent **does not** imply a connection or physical closeness on the graph.
- I decide I would like these nodes to connect and be close on the graph.
- ~~Control how nodes cluster by tagging them with the parent.~~
- ~~But if that is something I want, I can additionally tag all of those files with the parent: `#fpga/learn`.~~
- Control how nodes cluster by creating a file of links
    - create a file called `_2_FPGA-LEARN.md`
    - put links to the files I want to connect inside this file
        - do a search for `#fpga/learn`
        - use the "Copy" feature in the **Search** window to generate a list of links for all the matching files
        - paste this list into `_2_FPGA-LEARN.md`
    - this is better than tagging the files individually because it is quicker to change the name of one file than it is to change the link in many files
    - and it represents a hierarchy I am consciously imposing
        - I have to add new files to the list in `_2_FPGA-LEARN.md`
        - this is work, but the work is good:
            - I only need automatic linking for the connections I *don't* know are there
            - think of it like my stamp of approval on this connection
            - the connection is already implied by the nested tags in the search
            - adding the files to the list just adds the graph edges
    - and it is still consistent with the rest of what I say next (beacuse it doesn't matter if the node is a tag or a file)
- Now they all connect to a node called ~~`#fpga/learn`~~ `_2_FPGA-LEARN`, so there is the graph edge.
- But because of the full tag (the child), these nodes are bundled in a way that still keeps them physically separate.
- So now they are physically close on the graph, obviously connected, but also separated by their child tags.


## Impose node hierarchy

Name the files with the prefix.
To get a high-level view of the graph, do a filter with this expression:

```
file:("_1_" OR "_2_" OR "_3")
```

`;oQ` - open vault in pwd and do this search
`;oq` - open vault in pwd and search word under cursor; if it's a tag, search for the tag

Then for `;oQ` or `;oq`, open graph view, click **Filter** and paste with Ctrl-v.