# Convert `.ipynb` Files to `.py` Easy

- Make sure you have these libraries installed in your Python Environment:
  - `pip install ipython`
  - `pip install nbconvert`

## Convert a single file

`jupyter nbconvert --to script abc.ipynb`

## Convert multiple files

`jupyter nbconvert —-to script abc.ipynb def.ipynb`
`jupyter nbconvert —-to script *.ipynb`
