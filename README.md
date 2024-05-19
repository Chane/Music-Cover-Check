Assumes music collection is stored with folders per album / single. THis script will check that a cover is stored lcocally next to the music.
This does not check for any name convention (yet) just that there is an image there.

Expects a config.py file in the root of the format:

```
BASEPATH = "/Path/To/Mp3/Albums"
```
Will generate a `missing_art.txt` file in that directory with any folder that doesn't contain a .jpg or .jpeg file.
