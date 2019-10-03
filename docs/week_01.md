# Week 01: Non-trivial preparation

## Store what you learn with Markdown
Markdown is a markup-style language which makes writting technical documents conveniently.  

### Styling
To italicize text, add one asterisk or underscore before and after a *word* or _phrase_.

To bold text, add two asterisks or underscores before and after a **word** or __phrase__.

To emphasize text with bold and italics at the same time, add three asterisks or underscores before and after a ***word*** or ___phrase___.

To create a blockquote, add a > in front of a paragraph to create something like this:
> To create a blockquote, add a > in front of a paragraph.

Blockquotes can be nested. Add a >> in front of the paragraph you want to nest.
> We said that: 
>> They said @#$%&, and it is not what we want to be corrected in the contract.

### Make a header
Header can be made using different numbers of #-symbol, i.e. # or ## or ### and so on. 

### Insert a code
We can use the pair `` to highlight a code or a code block.

For example, if we want to highly `variable = 9` we can just use a pair of `. But for a code block, we need a pair of ``` as follows:
```python
for i in range(10):
    print(i)
```
To define the above code block is Python-code, we need to put `python` right after the first block of ```.

### Insert a mathematical formula
To insert a formula, we actually need to insert the latex-interpretation of the formula. This can be done easily online with tool such as https://www.codecogs.com/latex/eqneditor.php.

After receiving a latex code for our formular, we just need to put it inside the pair $$...$$ to make it visible in your mardown document.

$$\sum_{n=1}^{10}\left( x^{n} + \frac{x}{n} \right)$$

### Lists
We can organize items into ordered or unordered lists. 

#### Ordered lists
To create an ordered list, add line items with numbers followed by periods. The numbers don’t have to be in numerical order, but the list should start with the number one.
1. first
1. second
1. third

#### Unordered lists
To create an unordered list, add dashes (-), asterisks (*), or plus signs (+) in front of line items. Indent one or more items to create a nested list.
- first
    * first first
    * first second 
        + first second third
- second
- third


