Sublime Writing Tools
=====================

Might be only useful for me.

## Command "List Figures"

When writing with [pandoc][pandoc] flavored markdown it is nice to use the [pandoc-fignos][fignos] plugin. The List Figures command allows to query the text for figure declarations and insert the selected one from the quick panel at the cursors position.  

### Prerequisites  

- [Pandoc - About pandoc][pandoc]
- [tomduck/pandoc-fignos: A pandoc filter for numbering figures and figure references.][fignos]

[pandoc]: https://pandoc.org/ 
[fignos]: https://github.com/tomduck/pandoc-fignos 

## Command "Show Text Statistics"

This command show some statistics about the text. These are not accurate yet. It roughly counts characters, words and paragraphs. There needs to be some filtering to get the pure text excluding all the markdown syntax.  

### Prerequisites

Needs [Python Markdown](https://pythonhosted.org/Markdown/index.html) and [Beautiful Soup Documentation — Beautiful Soup 4.4.0 documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#).  

    pip install markdown
    pip install beautifulsoup4