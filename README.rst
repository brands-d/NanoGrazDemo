# NanoGrazDemo
This is a demo project for the NanoGraz meeting on October 30th, 2025.

Project Overview
================
NanoGrazDemo is a demonstration project created for the NanoGraz meeting on October 30th, 2025. It showcases key concepts, workflows, and best practices for collaborative software development.

Quick Start
===========

.. code-block:: bash

    pip install .; python -m nanograz

Installation
============

For certain platforms we provide pre-compiled binaries. Please check the host website for more details. To build from source, follow these steps:

1. Either download the ZIP file from the GitHub repository or clone it using git:

.. code-block:: bash

   git clone https://github.com/brands-d/NanoGrazDemo.git

2. Navigate to the project directory:

.. code-block:: bash

   cd NanoGrazDemo


3. (Optional) Create and activate a virtual environment:

.. code-block:: bash

   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

4. Install nanograz:

.. code-block:: bash

   python3 -m pip install --upgrade pip
   python3 -m pip install . # On Unix use `make install`

5. (Optional) Run tests to verify the installation:

.. code-block:: bash

   python3 -m pip install pytest
   python3 -m pytest ./tests

Usage
=====
Run the package from the command line:

.. code-block:: bash

   python3 -m nanograz

Or take a look at the example scripts in the `demo/` directory.

Documentation
=============
Comprehensive documentation is available at https://nanograzdemo.readthedocs.io/ or for offline use open the `docs/build/index.html` file in your web browser.

Contributing
============
Contributions are welcome! Please submit pull requests or open issues for suggestions and bug reports.

License
=======
This project is licensed under the MIT License. See `LICENSE` for details.

Author
======
- Dominik Brandstetter (dominik.brandstetter@uni-graz.at)

How to cite
===========
Please cite the following publication when using this software: https://doi.org/10.12345/abcde.67890