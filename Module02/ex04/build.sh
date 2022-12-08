# python -m venv tmp_env && source tmp_env/bin/activate
python3 -m pip install --upgrade pip setuptools wheel build
python3 -m build
pip install ./dist/my_minipack-1.0.0.tar.gz --force-reinstall
