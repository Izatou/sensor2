sudo apt update -y
sudo apt-get install -y libhdf5-dev libc-ares-dev libeigen3-dev gcc gfortran libgfortran5 libatlas3-base libatlas-base-dev libopenblas-dev libopenblas-base libblas-dev liblapack-dev cython3 libatlas-base-dev openmpi-bin libopenmpi-dev python3-dev
sudo apt install -y graphviz
sudo apt install -y pydotplus
sudo pip3 install pip --upgrade
sudo pip3 install keras_applications==1.0.8 --no-deps
sudo pip3 install keras_preprocessing==1.1.0 --no-deps
sudo pip3 install numpy==1.20.3
pip3 uninstall h5py==3.1.0-y
sudo apt install python3-h5py-y
sudo pip3 install pybind11
pip3 install -U --user six wheel mock
sudo wget "https://raw.githubusercontent.com/PINTO0309/Tensorflow-bin/main/tensorflow-2.5.0-cp37-none-linux_armv7l_numpy1195_download.sh"
sudo chmod +x tensorflow-2.5.0-cp37-none-linux_armv7l_numpy1195_download.sh
sudo ./tensorflow-2.5.0-cp37-none-linux_armv7l_numpy1195_download.sh
pip3 uninstall tensorflow
sudo rm /usr/lib/python3/dist-packages/wrapt-1.10.11.egg-info
pip3 install tensorflow-2.5.0-cp37-none-linux_armv7l.whl
