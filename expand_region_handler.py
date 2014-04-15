try:
  import javascript
  import html
except:
  from . import javascript
  from . import html

def expand(string, start, end, extension=None):

  if(extension == "html"):
    return html.expand(string, start, end)

  return javascript.expand(string, start, end)