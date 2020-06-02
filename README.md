# nb\_cell\_diff
Simple tools for ad hoc, in notebook, code cell differencing.

Based on the Google [`diff-match-patch`](https://github.com/google/diff-match-patch) Python3 package.


`%load_ext nbcelldiff`


The package currently provides cell block magics that let you compare the current cell with the previously executed cell, an earlier executed cell from its cell run index number, or the contents of the clipboard; and a line magic that lets you compare the contents of two previously executed cells from the cell run index numbers.

See the `demo.ipynb` for examples.