from .magics import NbDiffMatchPatchMagic

def load_ipython_extension(ipython):
    ipython.register_magics(NbDiffMatchPatchMagic)
