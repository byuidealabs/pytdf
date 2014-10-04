The Tour de Finance (pytdf)
===========================

The Tour de Finance (Version 2 with a Python Engine)

Building and Loading the Environment
------------------------------------

We recommend running `pydtdf` under a virtual environment. To aid in this, scripts have been included to build or load a local python virtual environment capable of running `pytdf`. 

To build the virtual environment, first install Python 3.4:

    apt-get install python3 python3-dev
    
Then run:
    
    . build_environment
    
The virtual environment is now installed within the TDF project under the directory `/env34/`, which contain the necessary dependencies to run TDF using Python 3.4.
    
The virtual environment only needs to be built once during installation. However, every time the bash is reloaded, the environment will likewise need to be reloaded. To do this:

    . load_environment
    
Running `build_environment` and `load_environment` will create the following environment variables which will aid in running TDF under the virtual environment:

* `$VENV`: Equivalent to `<tdf>/env34/`, where <tdf> is the directory where `pytdf` has been installed. Python scripts which are run under the virtual environment can be run with:
      
    $VENV/bin/python <script.py>
      
* `$VBIN`: An alias of `$VENV/bin`
* `$VPYTHON`: An alias of `$VENV/bin/python`
* `$VPSERVE`: An alias of `$VENV/bin/pserve`

Installing TDF
--------------

First, install `nodejs` using the instructions found [here](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager). In short:
    
    sudo apt-get update
    sudo apt-get install python-software-properties python g++ make
    sudo add-apt-repository ppa:chris-lea/node.js
    sudo apt-get update
    sudo apt-get install nodejs
    
Then install `bower`:

    npm install -g bower

Next, load the virtual environment using the instructions above. Once the virtual environment is loaded, `pytdf` can be installed with:

    $VPYTHON setup.py develop
    
Running the Test Cases
----------------------

To run the test cases:

    $VPYTHON setup.py test

Running the TDF Server
----------------------

Run the server with:  
        
    $VPSERVE development.ini --reload
    
The TDF app can now be opened at [localhost:6543/](http://localhost:6543/).

Building the Documentation
--------------------------

Install the documentation dependencies:

    $VBIN/easy_install sphinx numpydoc sphinxcontrib-bibtex
    
Generate the documentation with:

    $VPYTHON setup.py document
    
The built HTML of the documentation is now available at `public/docs/build/html/`.
