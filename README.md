# ๐ก AOV_dysplasia_Classification
## __Purpose__   
์ญ์ด์ง์ฅ ์ ๋๋ถ์ ์กด์ฌํ๋ ์ ์ข์ ์ ๋ฌด๋ฅผ ํ๋จํ๊ธฐ ์ํ ๋ฅ๋ฌ๋ ๋ชจ๋ธ ๊ตฌํ(Binary Classification)

## Requirements
- Python 3.6.13
- PyTorch 1.10.2
## Data Curation

  ### Dataset Distribution
  - __๋ด๋ถ ์ ์/๋น์ ์ ๋ฐ์ดํฐ, ์ธ๋ถ ๋น์ ์ ๋ฐ์ดํฐ ์กด์ฌ__
  - ๋ด๋ถ ๋ฐ์ดํฐ์ ๊ฒฝ์ฐ ๋น์ ์ ๋ฐ์ดํฐ๊ฐ ์ ์ ๋ฐ์ดํฐ์ ๋นํด ๋ง์, __Data Imbalance__ ๋ฌธ์  ์กด์ฌ

  ### Image Cropping
  - ๋ด๋ถ ๋ฐ์ดํฐ๋ง ์ด์ฉํ  ๊ฒฝ์ฐ ์ธํฐํ์ด์ค๊ฐ ๋์ผํ๊ธฐ ๋๋ฌธ์ ํ์์ curation ์ ๋ณด๋ฅผ ์ ์ธํ ์ด๋ฏธ์ง๊ฐ ์กด์ฌํ๋ __Pixel๊ฐ์ ์ง์ ํ์ฌ 
    Image Cropping์ ์งํ__
  - ์ธ๋ถ ๋ฐ์ดํฐ๋ฅผ ์ด์ฉํ  ๊ฒฝ์ฐ __์ธํฐํ์ด์ค๊ฐ ๋ฌ๋ผ ๋๊ฐ์ง ์ด๋ฏธ์ง ์ ์ฒ๋ฆฌ ์งํ__
     - __Opening ๋ฐฉ๋ฒ__์ ํตํด์ ์๋ณธ ์ด๋ฏธ์ง์ ์๋ text ์ ๊ฑฐ
     - __Canny edge detection ๋ฐฉ๋ฒ__์ ์ด์ฉํ์ฌ edge ์ถ์ถ
     - ์ด๋ ๊ฒ ๋์จ edge๋ฅผ ์ด์ฉํ์ฌ index๋ฅผ ์ฐพ์์ cropping์ ์งํ

## __DataSplit__
- ๊ฐ ์ค์ฆ๋ ๋ณ๋ก Patient๋ฅผ ๊ธฐ์ค์ผ๋ก 8:1:1, 7:1.5:1.5 ๋น์จ๋ก Split

## Study Design

  ### Pilot Study
  - __Model : Resnet 50(pretrained model)__
  - __Augmentation(Image Augmentation Library, albumnetation ์ด์ฉ)__
     - Resize, RandomScale, RandomRotate90, RandomVerticalFlip, RandomHorizontalFlip, RandomBrightnessContrast
  - Threshold(accuracy) : 0.5
  - Epoch : 100
  - Optimizer : Adam
  - Loss Functioin : BCE(Binary Cross Entropy)
  - Batch Size : 16
  - Learning Rate : 0.0001
  
## ๐ Experiments List  
  
- __Data Imbalance ๋ฌธ์ __๋ฅผ ํด๊ฒฐํ๊ธฐ ์ํด ๋ ๊ฐ์ง ๋ฐฉ๋ฒ ์ ์ฉ
  __1. Focal Loss__   
  __2. WeightedRandomSampler ์ ์ฉ__
  
- __Augmentation ์ถ๊ฐ__(CLAHE)
  
- __Abliation Test (Se_ResNet, Resnet50)__
  
- __Scheduler(Exponential LR(gamma : 0.95))__
  
- ์ธ๋ถ ๋ฐ์ดํฐ ์ถ๊ฐํ์ฌ ์คํ
  
- Grad-Cam์ ํตํด์ ํ์ฌ ํ์ต๋ ๋ชจ๋ธ์ด ์ ํ์ต๋์๋์ง ํ์ธ 
