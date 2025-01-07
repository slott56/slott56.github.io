# S.Lott -- Software Architect

https://slott56.github.io

## Installation

Pelican: [pelican](https://github.com/getpelican/pelican)

Python Markdown: [python-markdown](https://python-markdown.github.io/reference/#extensions)

PyMdown Extensions Arithmatex: [Arithmatex](https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/)

An alternative is  Python Markdown Math: [python-markdown-math](https://github.com/mitya57/python-markdown-math)
This offers a few options that don't seem helpful.

Navtools: /Users/slott/github/local/navtools

```commandline
python -m pip install install "pelican[markdown]"
python -m pip install pymdown-extensions
python -m pip install -e ~/github/local/navtools
python -m pip install ghp-import
```

Theme Installation

```commandline
git clone https://github.com/getpelican/pelican-themes.git
cd Pelican
pelican-themes -i ~/Documents/Writing/Blogs/pelican-themes/pelican-bootstrap3
```

Update `pelicanconf.py` to include `THEME=pelican-bootstrap3`


## Updates

See https://docs.getpelican.com/en/4.8.0/tips.html#user-pages

Change to the `Pelican/content` directory to access the source. Make changes.

Test with

```commandline
pelican --autoreload --listen
```

Or `make devserver`.

If the site can't be served by the devserver, it means a file has a bad slug, and is 
creating a ``.html`` file. Read this ``output/.html`` file to find this bad entry with the bad slug.

Publish with:

```commandline
pelican content -o .. -s pelicanconf.py
git commit -m "Blog updates through yyyy-mmm-dd"
git push origin master
```

Or, better yet:

```commandline
make github
git commit -m "Blog updates through yyyy-mmm-dd"
git push origin master
```

