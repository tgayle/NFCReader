* Install dependencies: nfc-bindings for python3


    `sudo apt-get install libusb-dev libpcsclite-dev git cmake swig python3-dev python3-pip python3-tk python3-lxml python3-six`
    

* Install libnfc

    ```bash
    wget http://dl.bintray.com/nfc-tools/sources/libnfc-1.7.1.tar.bz2
    tar -xf libnfc-1.7.1.tar.bz2  
    cd libnfc-1.7.1
    ./configure --prefix=/usr --sysconfdir=/etc
    make
    sudo make install 
    ```
    
* Set up libnfc configuation:

    ```bash
    cd /etc
    sudo mkdir nfc
    sudo nano /etc/nfc/libnfc.conf
    ```
    
* Copy and paste the contents of libnfc.conf into your local file
  * Replace `device.connstring = "pn532_spi:/dev/spidev0.0:500000"` with the string for your form of connection:
    * UART: `pn532_uart:/dev/ttyUSB0:115200`
    * I2C: `pn532_i2c:/dev/i2c-1`
    * SPI: `pn532_spi:/dev/spidev0.0:500000`
    
* Prepare nfc-bindings for Python support.

    ```bash
    git clone https://github.com/xantares/nfc-bindings.git
    cd nfc-bindings
    cmake -DPYTHON_EXECUTABLE:FILEPATH=/usr/bin/python3 -DCMAKE_INSTALL_PREFIX=~/.local .
    make install
    ```
    
    
