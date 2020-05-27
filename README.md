
# DaVis_
## The W.H.Y

One of the biggest problems students face when taking advanced programming classes like data structures is the visualization of abstract structures. As a result, the students’ execution fails to demonstrate their knowledge or creates an unnecessary hurdle. The implementation of a simple programming language that would help in the visualization of the structures could be of great use. That's where DaVis comes in! Working around JFrame, it is an easy way to create models used by students or professors alike in the explanation, study or transformation of data structures like circular-singly-linked-list.

### The FEAT_ure.s
The language should be able to visualize different types of data structures.

1. Easy rendition of different Data Structures graphs with easy modification of ->
   * Dimensions
   * Color
   * Position
1. The visualization should be done with only three functions -> 
   * Canvas
   * Structure
   * Draw
1. The available structure visualizations ->
   * Array
   * Doubly Linked List With Dummy Header
   * Stack
   * Queue

## How to O.P.E.R.A.T.E 
1. Write or modify the three DaVis functions on the "test.davis" file
   1. Canvas
     * dimensions => two integers determining the size of the canvas screen
     * background color (bgColor) => one of **WHITE**, **BLACK**, **GREEN**, **YELLOW**, **RED**, **BLUE** 
     * position => two integers determining where the canvas starts on your screen
   1. Structure
     * structure name (struc) => one of **arrayStructure**, **doublyLinkedList**, **queue**, **stack**
     * data => an array with the integers in the structure
   1. Draw
     * penSize => an integer followed by the string "px"
     * penColor => one of **WHITE**, **BLACK**, **GREEN**, **YELLOW**, **RED**, **BLUE**
     * animation => boolean true or false
     * AN OPTIONAL ARGUMENT BEING THE PREVIOUS STRCUTURE FUNCTION => the string "funcStructures"
1. You need [python](https://www.python.org/downloads/) installed on your machine.
  * Open the terminal and go to the directory of the project
  * Run `python parser.py` on your temrinal 

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/FherRodz/davis-programming-language/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
