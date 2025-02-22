#### Javier V. Gómez - personal site source

Output hosted at:
http://www.javiervgomez.com - https://jvgomez.github.io

Pelican-based static website. Feel free to use whatever you want :)

#### DEPENDENCIES
In order to be able to create the site with Pelican, the following dependencies must be installed:


- `beautifulsoup4` (required by the extract_toc Pelican plugin)
```bash
$ sudo pip install beautifulsoup4
```

##### Third-party code included in the repo
- `extract_toc` Pelican plugin (create tables of contents).
- `liquid_tags` Pelican plugin (to embed YouTube videos). It required various fixes, detailed [here](https://github.com/getpelican/pelican-plugins/issues/312), [here](https://github.com/getpelican/pelican-plugins/issues/331), [here](https://github.com/getpelican/pelican-plugins/pull/321), and then modifying `youtube.py`to create `/embed/` insead of `/v/` URLs. It has been modified also not to create `<div>` tags so that I can place videos in columns easily.

#### Pelican theme
The code of this site is designed to work with a self-made modification of the `tuxlite_tbs` pelican theme. You can find my version in this repo:

https://github.com/jvgomez/tuxlite_tbs

If you use other themes, some thinkgs would probably fail.

#### Developing
Clone this repo, open a terminal on the folder created and:

    $ pelican

The output folder is what I upload to Github pages. To run locally:

    $ cd output
    $ python -m SimpleHTTPServer

Open a browser and write the IP:port shown in terminal.

##### TODO
- Include Google+ social link (with icon).
- Include ResearchGate social link (with icon).
- Include YouTube social link (with icon).
- Include Biicode social link (with icon).
- Look for a better About Me pic.
- Include LinkedIn and GitHub interactive banners in about me.

