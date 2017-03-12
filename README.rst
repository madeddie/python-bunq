bunq
====

Python wrapper for the `bunq API <https://doc.bunq.com/>`.

Installation
------------

This package has been tested with Python 3.6.0, but probably works fine with 3.3 and later.
Python 2.6 and later should also work, but no guarantees.

To install, use ``setuptools``, run:

``python ./setup.py install``

or for installing locally for the user:

``python ./setup.py install --user``

There is no PyPI package as of yet.

Usage
-----

The module is a thin wrapper around the bunq API and takes care of the following:

* setting the required HTTP headers
* signing of the outgoing message
* verification of the response (still very limited)

The code is blissfully unaware of the API endpoints and the data they need and return.
You will need the bunq API documentation to figure out all the endpoints and required parameters and possible responses.

After installation this module is called simply bunq. You will probably want to import it like:

``from bunq import API``

and instantiate and API object like so:

``my_api_instance = API(private_key, token)``

There are several examples in the ``examples`` directory to give you an idea how this module can be used.

Documentation
-------------

The code itself is documented with docstrings.

External documentation will be coming ASAP.

TODO
----

* better verification of response
* automated session creation
* use a more lightweight crypto library, like https://github.com/sybrenstuvel/python-rsa
* active session awareness
* testing validity of token
* automagically retrieve server public key when not given

Attribution
-----------

All code is licensed under the MIT License. See ``LICENSE``.

`python3-krakenex <https://github.com/veox/python3-krakenex>` was a big inspiration.
