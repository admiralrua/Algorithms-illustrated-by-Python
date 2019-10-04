---
description: >-
  Markdown is a markup-style language which makes writing technical documents
  conveniently.
---

# Markdown for documentation

## Make a header

Header can be made using different numbers of \#-symbol, i.e. \# or \#\# or \#\#\# and so on.

## Styling

To italicize text, add one asterisk \(\*\) or underscore \(\_\) before and after a _word_ or _phrase_.

To bold text, add two asterisks or underscores before and after a **word** or **phrase**.

To emphasize text with bold and italics at the same time, add three asterisks or underscores before and after a _**word**_ or _**phrase**_.

To strikethrough words, use two tilde symbols \(\~~\) ~~before and after~~ the words.

To create a blockquote, add a &gt; in front of a paragraph to create something like this:

> To create a blockquote, add a &gt; in front of a paragraph.

Blockquotes can be nested. Add a &gt;&gt; in front of the paragraph you want to nest.

> We said that:
>
> > They said @\#$%&, and it is not what we want to be corrected in the contract.

## Lists

Items can be organized into ordered or unordered lists.

### Ordered lists

To create an ordered list, add line items with numbers followed by periods. The numbers don’t have to be in numerical order, but the list should start with the number one.

1. first
2. second
3. third

### Unordered lists

To create an unordered list, add dashes \(-\), asterisks \(\*\), or plus signs \(+\) in front of line items. Indent one or more items to create a nested list.

* first
  * first first
  * first second 
    * first second first
    * first second second
* second
* third

## Footnotes

Creating a footnote reference is a little bit tricky atm. I found [this link](https://stackoverflow.com/questions/25579868/how-to-add-footnotes-to-github-flavoured-markdown) to manually fake a footnote. This is not ideal since we have to be responsible for maintaining the numbering of footnotes.

First define the footnote as:

```text
We are referring to a fake footnote <sup>[1](#fn01)</sup>
```

then reference it as:

```text
<a name="fn01">1</a>: This is a fake footnote.
```

We are referring to a fake footnote [1](non-trivial.md#fn01) and another one [3](non-trivial.md#fn02).

[1](non-trivial.md): This is a fake footnote.

[3](non-trivial.md): This is another fake footnote.

## Task Lists

Task lists allow us to create a list of items with checkboxes. To create a task list, add dashes \(-\) and brackets with a space \(\[ \]\) in front of task list items. To select a checkbox, add an x in between the brackets \(\[x\]\).

This block code:

```text
- [x] Start with Markdown;
- [ ] Then the software-engineering algorithms;
- [ ] And the AI/ML/DL algorithms.
```

give us:

* [x] Start with Markdown;
* [ ] Then the software-engineering algorithms;
* [ ] And the AI/ML/DL algorithms.

## Insert a code

A code or a code block can be highlighted by using the pair \`\`.

For example, if we want to highly `variable = 9` we can just use a pair of \`. But for a code block, we need a pair of \`\`\` as follows:

```python
for i in range(10):
    print(i)
```

Markdown supports syntax highlighting for code blocks. This feature allows us to add color highlighting for whatever language our code was written in. To add syntax highlighting, specify a language next to the tick marks before the code block. In the aforementioned example, the above code block is Python-code, therefore, we need to put `python` right after the first block of \`\`\`.

## Insert a mathematical formula

To insert a formula, we actually need to insert the latex-interpretation of the formula. This can be done easily online with tool such as [https://www.codecogs.com/latex/eqneditor.php](https://www.codecogs.com/latex/eqneditor.php).

After receiving a latex code for our formular, we just need to put it inside the pair $$...$$ to make it visible in your mardown document. This code block:

```text
$$\sum_{n=1}^{10}\left( x^{n} + \frac{x}{n} \right)$$
```

result in:

$$\sum_{n=1}^{10}\left( x^{n} + \frac{x}{n} \right)$$

## Insert images

To add an image, add an exclamation mark \(!\), followed by alt text in brackets, and the path or URL to the image asset in parentheses. You can optionally add a title after the URL in the parentheses.

![Where i currently work](../.gitbook/assets/rhdhv.jpg)

## Insert links

To create a link, enclose the link text in brackets \(e.g., \[from this link\]\) and then follow it immediately with the URL in parentheses \(e.g., \([https://www.markdownguide.org/](https://www.markdownguide.org/)\)\):

I learn Markdown [from this link](https://www.markdownguide.org/)

You can optionally add a title for a link by enclosing it in parentheses after the URL. This will appear as a tooltip when the user hovers over the link, e.g.:

I learn Markdown [from this link](https://www.markdownguide.org/)

To quickly turn a URL or email address into a link, enclose it in angle brackets \(\&lt;\).

[https://github.com/admiralrua/Algorithms-illustrated-by-Python](https://github.com/admiralrua/Algorithms-illustrated-by-Python)

[ntchi1983@gmail.com](mailto:ntchi1983@gmail.com)

## Insert tables

To add a table, use three or more hyphens \(---\) to create each column’s header, and use pipes \(\|\) to separate each column. We can optionally add pipes on either end of the table. Noted that cell widths can vary and the rendered output still looks the same. You can align text in the columns to the left, right, or center by adding a colon \(:\) to the left, right, or on both side of the hyphens within the header row.

For example, this code block

```text
| Syntax      | Description | Testing text |
| :---        | :---:       | ---:    | 
| Header      | Title       | Ahihi   |
| Paragraph   | Text        | Alo ola |
```

will result in:

| Syntax | Description | Testing text |
| :--- | :---: | ---: |
| Header | **Title** | Ahihi |
| Paragraph | _Text_ | Alo ola |

We can format the text within tables. For example, we can add links, code \(words or phrases in tick marks \(\`\) only, not code blocks\), and emphasis. However, we can’t add headings, blockquotes, lists, horizontal rules, images, or HTML tags.

