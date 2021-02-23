# transpose - command-line tool for transposing data

This is a short Python script for transposing data for easier navigation and probably other uses. You pipe in data, tell it the delimiters and out comes the transposed version. It can also add row numbering.

## Options

```sh
$ transpose -h
usage: Command-line tool to transpose some data from std-in
       [-h] [-t T] [-n] [-n0] [-o O]

optional arguments:
  -h, --help  show this help message and exit
  -t T        Delimiter (default=\t)
  -n          Number output rows from one
  -n0         Number output rows from zero
  -o O        Alternative output delimiter

```

## Example Usage

Here is example usage using data from [CancerMine](https://doi.org/10.5281/zenodo.1156241).

```sh
$ head -n 2 cancermine_collated.tsv
matching_id     role    cancer_id       cancer_normalized       gene_hugo_id    gene_entrez_id  gene_normalized citation_count
f952c5ad7bfa3a24e85e9c3326cdeb4f        Oncogene        DOID:1612       breast cancer   HGNC:3430       2064    ERBB2   726
```

```sh
$ head -n 2 cancermine_collated.tsv | transpose -n
1       matching_id     f952c5ad7bfa3a24e85e9c3326cdeb4f
2       role    Oncogene
3       cancer_id       DOID:1612
4       cancer_normalized       breast cancer
5       gene_hugo_id    HGNC:3430
6       gene_entrez_id  2064
7       gene_normalized ERBB2
8       citation_count  726
```

