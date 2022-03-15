#Setup on Ubuntu 18.04
sudo apt update

##gem5 prerequisites
sudo apt install build-essential git m4 scons zlib1g zlib1g-dev libprotobuf-dev protobuf-compiler libprotoc-dev libgoogle-perftools-dev python3-dev python3-six python libboost-all-dev pkg-config

##certi prerequisites
sudo apt install cmake bison flex libxml2-dev

##omnet 5.0 prerequisites
sudo apt install openjdk-8-jdk openjdk-8-jre tcl-dev tk-dev qt4-qmake libqt4-dev libqt4-opengl-dev openmpi-bin libopenmpi-dev clang



#Setup on Ubuntu 20.04
sudo apt update

##gem5 prerequisites
sudo apt install build-essential git m4 scons zlib1g zlib1g-dev libprotobuf-dev protobuf-compiler libprotoc-dev libgoogle-perftools-dev python3-dev python3-six python-is-python3 libboost-all-dev pkg-config

##certi prerequisites
sudo apt install cmake bison flex libxml2-dev

##omnet 5.0 prerequisites
sudo add-apt-repository ppa:rock-core/qt4 (https://ubuntuhandbook.org/index.php/2020/07/install-qt4-ubuntu-20-04/)
sudo apt install openjdk-8-jdk openjdk-8-jre tcl-dev tk-dev qt4-qmake libqt4-dev libqt4-opengl-dev openmpi-bin libopenmpi-dev clang


#Manual Installation
`cd $HOME
https://github.com/ntampouratzis/RED-SEA.git
mv -f $HOME/RED-SEA $HOME/COSSIM`

##cCERTI & Our SynchServer Installation
`cd $HOME/COSSIM/cCERTI
mkdir build_certi
cd build_certi
cmake -DCMAKE_INSTALL_PREFIX=$HOME/COSSIM/cCERTI/build_certi $HOME/COSSIM/cCERTI`









