pytdf
=====

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

Installing TDF
--------------

Once the virtual environment has been loaded, `pydf` can be installed with:

    $VPYTHON setup.py develop
    
Running the Test Cases
----------------------

To run the test cases:

    $VPYTHON setup.py test
