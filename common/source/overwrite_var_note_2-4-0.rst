.. note::

    With the release of |at| 2.4.0, edits and additions to Inventory host variables now persist beyond an inventory sync as long as ``--overwrite_vars`` is **not** set. To have inventory syncs behave as they did before, it is now required that both ``--overwrite`` and ``--overwrite_vars`` are set.