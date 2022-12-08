# 💡 AOV_dysplasia_Classification
- 십이지장 유두부에 존재하는 선종의 유무를 판단하기 위한 딥러닝 모델 구현(Binary Classification)

## Requirements
- Python 3.6.13
- PyTorch 1.10.2
## Data Curation

  ### Dataset Distribution
  - __내부 정상/비정상 데이터, 외부 비정상 데이터 존재__
  - 내부 데이터의 경우 비정상 데이터가 정상 데이터에 비해 많아, __Data Imbalance__ 문제 존재

  ### Image Cropping
  - 내부 데이터만 이용할 경우 인터페이스가 동일하기 때문에 환자의 curation 정보를 제외한 이미지가 존재하는 __Pixel값을 지정하여 
    Image Cropping을 진행__
  - 외부 데이터를 이용할 경우 __인터페이스가 달라 두가지 이미지 전처리 진행__
     - __Opening 방법__을 통해서 원본 이미지에 있는 text 제거
     - __Canny edge detection 방법__을 이용하여 edge 추출
     - 이렇게 나온 edge를 이용하여 index를 찾아서 cropping을 진행


## Study Design

  ### Pilot Study
  - __Model : Resnet 50(pretrained model)__
  - __Augmentation(Image Augmentation Library, albumnetation 이용)__
     - Resize, RandomScale, RandomRotate90, RandomVerticalFlip, RandomHorizontalFlip, RandomBrightnessContrast
  
## 📋 Experiments List  
  
- __Data Imbalance 문제__를 해결하기 위해 두 가지 방법 적용
  __1. Focal Loss__   
  __2. WeightedRandomSampler 적용__
  
- __Augmentation 추가__(CLAHE)
  
- __Abliation Test (Se_ResNet, Resnet50)__
  
- __Scheduler(Exponential LR(gamma : 0.95))__
  
- 외부 데이터 추가하여 실험
  
- Grad-Cam을 통해서 현재 학습된 모델이 잘 학습되었는지 확인 
