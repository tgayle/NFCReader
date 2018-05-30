* Install nfc-bindings for python3
    sudo apt-get install git cmake swig python3-dev python3-pip python3-tk python3-lxml python3-six
    git clone https://github.com/xantares/nfc-bindings.git
    cd nfc-bindings
    cmake -DPYTHON_EXECUTABLE:FILEPATH=/usr/bin/python3 -DCMAKE_INSTALL_PREFIX=~/.local .
    make install
