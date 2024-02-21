# Extract-Transform-Unify

This package enables the unification of results from different software performing the same analysis.
It is designed with Plasmodium falciparum genomic data analysis in mind, but can be used for any kind of data.
The tool has taken inspiration from the [hAMRonization](https://github.com/pha4ge/hAMRonization.git) package.

## Installation

```
pip install git+https://github.com/jodyphelan/etu.git
```

## Usage example

```
etu COI PyMOI <input_file> <unified_format_output>
```

## Contribution

Each analysis type must be implemented as a submodule of the package with the following objects defined:
 1. An abstract base class `Interface` defined in `interface.py`
 2. A pydantic data model for the unified format defined in `interfact.py`
 3. A subclass inheriting from `Interface` for each software that defines the `parse` method.

The interface class must define the following methods:
 1. `write_result` which takes the unified format and writes it to a file.
 2. `add_subparser` which takes a subparser and adds the analysis specific arguments to it.

