# News summary: 11 November 2026

A short, sourced summary of the world's news of Wednesday, 11 November 2026.
`main.py` copies the prepared text in `summary.txt` byte-for-byte to
`entry.txt` in the output directory, so the output is fully deterministic.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Without `MAKEFUN_OUTPUT_DIR` set, the output goes to `/output/entry.txt`.
