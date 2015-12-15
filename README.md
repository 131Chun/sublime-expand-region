[![Build Status](https://travis-ci.org/aronwoost/sublime-expand-region.png?branch=master)](https://travis-ci.org/aronwoost/sublime-expand-region)

# ExpandRegion for Sublime Text

### Like "Expand Selection to Scope". But better!

ExpandRegion works a bit like the build in "Expand Selection to Scope", however it does not depend on Scopes (Scopes are used by ST to "understand" code, i.e. for syntax highlighting). Therefore selection expansion can be more granular and customizable.

It works similar to ExpandRegion for Emacs and "Structural Selection" (Control-W) in the JetBrains IDE's (i.e. IntelliJ IDEA).

## Example

JavaScript (should also work for other c'ish languages like Java).

![](http://aronwoost.github.io/expand-region.gif)

1. Expand selection to sub_word
2. Expand selection to word
3. Expand selection to quotes (content only)
4. Expand selection to quotes (with quotes)
5. Expand selection to square braces
6. Expand selection to expression
7. Expand selection to content of braces (all arguments in this case)
8. Expand selection to line
9. Expand selection to function body (w/o curly brace)
10. Expand selection to function body (with curly brace)

and so on...

HTML

![](http://aronwoost.github.io/expand-to-html.gif)

1. Expand selection to sub_word
2. Expand selection to word
3. Expand selection to quotes (content only)
4. Expand selection to quotes (with quotes)
5. Expand selection to complete self closing tag
6. Expand selection to parent node content
7. Expand selection to complete node
8. Expand selection to parent node content

and so on...

LaTeX (thx [r-stein](https://github.com/r-stein))

![](https://cloud.githubusercontent.com/assets/12573621/11544524/994770b4-9942-11e5-9ffc-9819d50048b6.gif)

1. Expand selection to word
2. Expand selection to command
3. Expand selection to command arguments
4. Expand selection to surrounding command
5. Expand selection to surrounding environment

and so on...

## Installing

**With the Package Control plugin:** The easiest way to install ExpandRegion is through Package Control, which can be found at this site: [http://wbond.net/sublime_packages/package_control](http://wbond.net/sublime_packages/package_control)

Once you install Package Control, restart ST and bring up the Command Palette (`Command+Shift+P` on OS X, `Control+Shift+P` on Linux/Windows). Select "Package Control: Install Package", wait while Package Control fetches the latest package list, then select ExpandRegion when the list appears. The advantage of using this method is that Package Control will automatically keep ExpandRegion up to date with the latest version.

**Without Git:** Download the latest source from [GitHub](https://github.com/aronwoost/sublime-expand-region) and copy the ExpandRegion folder to your Sublime Text "Packages" directory.

**With Git:** Clone the repository in your Sublime Text "Packages" directory:

    git clone https://github.com/aronwoost/sublime-expand-region.git ExpandRegion


The "Packages" directory is located at:

* OS X:

        ~/Library/Application Support/Sublime Text 2/Packages/

* Linux:

        ~/.config/sublime-text-2/Packages/

* Windows:

        %APPDATA%/Sublime Text 2/Packages/

## Using

- Set a shortcut.
  Open "Key Bindings - User" and add to following line: 
``` js
{ "keys": ["super+shift+space"], "command": "expand_region" },
{
  "keys": ["super+u"],
  "command": "expand_region",
  "args": {"undo": true},
  "context": [{ "key": "expand_region_soft_undo" }]
},
```
Note: third party plugins can not properly hook into the history. So soft-undo in basically only a undo expand selection. Soft-redo will not work.


## Develop

## Background

This plugin is inspired by the amazing [expand-region for Emacs](https://github.com/magnars/expand-region.el).

Here a video showing this feature (in Emacs):  

[![](http://img.youtube.com/vi/_RvHz3vJ3kA/0.jpg)](http://www.youtube.com/watch?v=_RvHz3vJ3kA?feature=player_embedded&v=M)

Read more:  
[Extend Selection by Semantic Unit](http://ergoemacs.org/emacs/syntax_tree_walk.html)

## License

MIT
