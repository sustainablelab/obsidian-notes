I create one Obsidian vault per Git repository.

# Why one vault per Git repository?

Vaults evolve with the project, specifically, the graph view. I
track the `.obsidian` folder with Git. Now my graph view is under
version control. There are two reasons I care about version
control on the graph view:

1. restoring the graph view
2. animating project history

## Restore Graph View

If I play with the view (i.e., add new groups, hide/show stuff,
tweak physics settings), I can do it without fear of "messing up"
my preferred view. I easily discard those temporary changes with:

```bash
git checkout -f .obsidian/graph.json
```

## Animate Project History

I have an idea to set up a graph view over time, where each time
instance is a Git commit. The idea goes something like this:

1. open vault
1. get a working tree of the first commit:
    1. when I checkout the first commit, Git changes what's on
       disk to reflect the repository state at the first commit
    1. this updates the Obsidian graph view to go back in time to
       that initial graph view of the project (because Obsidian
       will shows whatever is on disk)
1. take a picture
    1. could be an actual screenshot
    1. but even better is to create a completely new file (not
       tracked by Git) that has all the information I need to
       recreate the graph view at a later time
1. repeat this process with each commit to generate all the
   pictures of the graph view
1. finally, open an animation view of these pictures where I can
   "step" through the commits
