Hosted-Telephone-Reception-System
=================================

Requirements, use-cases and detailed specifications.


Use-cases:
----------

The master version of all use-cases can be found in `/use-cases/`.  Each
use-case has its own subdirectory there.

A use-case is structured as follows:

- Preconditions for the use-case (in `preconditions.md`).
- Name in the wiki (in `name`).
- A subdirectory for each variant of the use-case containing:
  + A description of that variant (in `description.md`).
  + The user view of what happens in that variant of the use-case (in `user.md`).

From these files and patterns stored in `/use-cases/.patterns/`, the following
files are generated for each use-case variant:

+ The system view of what happens in that variant of the use-case (in `system.md`).
+ Sequence diagram sources matching the user and system views (in `user.seq-diag` and `system.seq-diag`).
+ Sequence diagram images matching the user and system views (in `user.seq-diag.png` and `system.seq-diag.png`).
+ An integration test (in Python) for that variant of the use-case (in `test.py`).

To generate these files run:
```shell
make use-cases
```

To collect this information and copy it to the wiki as one page per use-case, run:
```shell
make wiki
```
You still have to review, commit and push any changes to the wiki repository yourself.


Protocol overview:
------------------

To generate an overview of all existing protocol documentation in the public
wikis for the system run:
```shell
make protocol-overview
```


Integration tests:
------------------

To copy integration tests to the [Coverage Tests](https://github.com/AdaHeads/Coverage_Tests)
repository, run:
```shell
make integration-tests
```
You still have to review, commit and push any changes to the coverage
tests repository yourself.

**Note**: The command will fail if you haven't checked out the
coverage tests repository somewhere under your home directory.

