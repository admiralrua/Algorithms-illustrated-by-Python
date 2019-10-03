# Non-trivial preparation

## Markdown for quick-writting

Markdown is a markup-style language which makes writting technical documents conveniently.

### Make a header

Header can be made using different numbers of \#-symbol, i.e. \# or \#\# or \#\#\# and so on.

### Styling

To italicize text, add one asterisk (\*) or underscore (\_) before and after a _word_ or _phrase_.

To bold text, add two asterisks or underscores before and after a **word** or **phrase**.

To emphasize text with bold and italics at the same time, add three asterisks or underscores before and after a _**word**_ or _**phrase**_.

To create a blockquote, add a &gt; in front of a paragraph to create something like this:

> To create a blockquote, add a &gt; in front of a paragraph.

Blockquotes can be nested. Add a &gt;&gt; in front of the paragraph you want to nest.

> We said that:
>
> > They said @\#$%&, and it is not what we want to be corrected in the contract.

### Lists

We can organize items into ordered or unordered lists.

#### Ordered lists

To create an ordered list, add line items with numbers followed by periods. The numbers don’t have to be in numerical order, but the list should start with the number one.

1. first
2. second
3. third

#### Unordered lists

To create an unordered list, add dashes \(-\), asterisks \(\*\), or plus signs \(+\) in front of line items. Indent one or more items to create a nested list.

* first
  * first first
  * first second 
    * first second first
    * first second second
* second
* third

### Insert a code

We can use the pair \`\` to highlight a code or a code block.

For example, if we want to highly `variable = 9` we can just use a pair of \`. But for a code block, we need a pair of \`\`\` as follows:

```python
for i in range(10):
    print(i)
```

To define the above code block is Python-code, we need to put `python` right after the first block of \`\`\`.

### Insert a mathematical formula

To insert a formula, we actually need to insert the latex-interpretation of the formula. This can be done easily online with tool such as [https://www.codecogs.com/latex/eqneditor.php](https://www.codecogs.com/latex/eqneditor.php).

After receiving a latex code for our formular, we just need to put it inside the pair $$...$$ to make it visible in your mardown document.

$$\sum_{n=1}^{10}\left( x^{n} + \frac{x}{n} \right)$$

### Insert images

To add an image, add an exclamation mark \(!\), followed by alt text in brackets, and the path or URL to the image asset in parentheses. You can optionally add a title after the URL in the parentheses.

![Where i currently work](../.gitbook/assets/rhdhv.jpg)

### Insert links
To create a link, enclose the link text in brackets (e.g., [Introduction for Markdown]) and then follow it immediately with the URL in parentheses (e.g., (https://www.markdownguide.org/)), i.e.:

I learn Markdown [in this link](https://www.markdownguide.org/)

