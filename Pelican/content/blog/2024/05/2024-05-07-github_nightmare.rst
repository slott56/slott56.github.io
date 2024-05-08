Git Nightmare
######################

:date: 2024-05-07 08:01
:tags: git,github,memory
:slug: 2024-05-07-github_nightmare
:category: Python
:status: published

My sailing blog, `Team Red Cruising <https://itmaybeahack.com/TeamRedCruising2/index.html>`_
is very large: 859 postings over the last few years. 2,334 image files.

This is a LOT of content.

A few of the files (were) Movies, which tend to create immense files.

The whole mess was so big

**How Big Was It?**

It was so big, the ``git push`` command crashed. Repeatedly.

I researched a lot of Stack Overflow answers on dealing with big files.  Maybe they were helpful.
Maybe they were misleading. I tried a **lot** of things.

The problem was using the following approach.

1. First. Get it all organized.
2. Then. Do a single massive commit of everything.
3. Now. The ``git push``.

This -- it turns out -- is not a good idea. There are too many files and too many huge files.

Beating to Weather
------------------

It seemed sensible to try and preseve the "one big commit with everything in it."

This was -- of course -- a mistake.

It's just too big to preserve. And there's no good reason to preserve it.

It had some HUGE movie and PDF files that are better kept separate from the blog content.
Some of the pictures were exported at **full** size, leading to about 100 image files of 22Mb or larger.
The resulting pack files are huge. Far too big to process.

Trying to get the ``git gc`` and ``git repack`` commands to create some useful approach to uploading one big commit was (in retrospect) a waste of time and brain calories.

Image Resizing
--------------

This was fun. A little program using ``pillow`` to do ``Image.reduce()`` on the 100 or so egregiously large files.

::

    def png_reduce(counts: Counter, path: Path, new: Path) -> None:
        target_image_size =  4_851_306  # about 2202 x 2202.

        counts[path.suffix] += 1
        if not path.suffix.lower() in {".png"}:
            return
        try:
            with Image.open(path) as image:
                if image.width * image.height < target_image_size:
                    counts['small'] += 1
                    return
                counts['reduce'] += 1
                factor = int((image.width * image.height) / target_image_size + 0.5)
                target_width = int(image.width / factor + 0.5)
                target_height = int(image.height / factor + 0.5)
                reduced = image.reduce(factor)
                # Save reduced Image in separate directory. These can then be moved to replace the originals.
                target = new / path.name
                reduced.save(target)
            print(
                f"Reduce {path.name} {path.lstat().st_size // 1024 // 1024}M:"
                f" factor={factor} from {image.width}×{image.height} to {target_width}×{target_height}"
            )
        except UnidentifiedImageError as ex:
            counts['exception'] += 1
            print(path.name, ex)

The target image size was a kind of guess. I divided the range of sizes into 64 bins.
I counted the number of files in each bin to see where the various size lumps occurred.
The bin with 4,851,306 seemed to be on the line between a lot of small files and a few large files.

Tack to a New Course
--------------------

What's the alternative?

Here's what worked.

1. ``git reset`` back to empty. (There was only one commit, so this was easy.)

2. Put in the overhead files: ``README.rst``, ``requirements.txt``, the Pelican configuration files, ``Makefile``, etc.

3. Commit this. And push.

4. Put in the text content files, all 859 of them. Plus the handful of non-blog pages and photo albums.

5. Commit this. And push.

6. The images can be broken into 5 batches of about 400 files. Commit and push each of these.

At the end of the day, it's all there, but it took 7 commits and 7 separate ``git push`` operations to get there.

It went really fast. Error free. No drama.

Doubly aggravating because this could have been completed two days ago.

The Finish Line
---------------

Now, I can do ordinary ``git pull`` and ``git push`` from **any** computer.

I can login to the hosting service from any computer, do a ``git pull`` and a ``make publish``, and the site is updated.

The point is to be able to use an iPad to edit content and leverage my hosting service to do a little more than serve static HTML.

