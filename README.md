create env
'''bash
conda create -n wineq python=3.11.9
'''
activate env
'''bash
conda activate wineq
'''
create req file
install the req
'''bash
pip install -r requirements.txt
'''

Download the data

git init
dvc init
dvc add data_given/winequality.csv
git add .
git commit .m "First commit"
git add README.md...
git commit -m "Update README.md"...
git remote add origin https://github.com/MorrisLesinko/Simple_dvc_demo.git
git branch -M main
git push -u origin main
git branch -M main
git push -u origin main