import os
from PIL import Image
import numpy as np

# Training
current_dir=os.getcwd()
img_dir=os.path.join(current_dir,'MoNuSegTrainingData/Tissue Images/')
save_dir=os.path.join(current_dir,'train_500_size/Tissue_Images')

size_img=500


for files in os.listdir(img_dir):
    if not files.startswith('.'):
        img=Image.open(os.path.join(img_dir,files))
        img=np.array(img)
        n=0
        for i in range(0,np.array(img).shape[0],size_img):
            for j in range(0,np.array(img).shape[0],size_img):
                n+=1
                new_img=img[i:i+size_img,j:j+size_img,:]
                new_img=Image.fromarray(new_img)
                new_img.save(os.path.join(save_dir,files[:-4])+'_'+str(n)+'.jpg','JPEG')
            
        

img_dir=os.path.join(current_dir,'MoNuSegTrainingData/Annotations/masks_true/masks_true_jpeg')
save_dir=os.path.join(current_dir,'train_500_size/Annotations')


size_img=500
for files in os.listdir(img_dir):
    if not files.startswith('.'):
        img=Image.open(os.path.join(img_dir,files))
        img=np.array(img)
        n=0
        for i in range(0,np.array(img).shape[0],size_img):
            for j in range(0,np.array(img).shape[0],size_img):
                n+=1
                new_img=img[i:i+size_img,j:j+size_img]
                new_img=Image.fromarray(new_img)
                new_img.save(os.path.join(save_dir,files[:-5])+'_'+str(n)+'.jpg','JPEG')
                
img_dir=os.path.join(current_dir,'MoNuSegTestData/Tissue Images/')
save_dir=os.path.join(current_dir,'test_500_size/Tissue_Images')

#Test data
size_img=500
for files in os.listdir(img_dir):
    if not files.startswith('.'):
        img=Image.open(os.path.join(img_dir,files))
        img=np.array(img)
        n=0
        for i in range(0,np.array(img).shape[0],size_img):
            for j in range(0,np.array(img).shape[0],size_img):
                n+=1
                new_img=img[i:i+size_img,j:j+size_img,:]
                new_img=Image.fromarray(new_img)
                new_img.save(os.path.join(save_dir,files[:-4])+'_'+str(n)+'.jpg','JPEG')
            
                
img_dir=os.path.join(current_dir,'MoNuSegTestData/masks_true/masks_true_jpeg')
save_dir=os.path.join(current_dir,'test_500_size/Annotations')

size_img=500
for files in os.listdir(img_dir):
    if not files.startswith('.'):
        img=Image.open(os.path.join(img_dir,files))
        img=np.array(img)
        n=0
        for i in range(0,np.array(img).shape[0],size_img):
            for j in range(0,np.array(img).shape[0],size_img):
                n+=1
                new_img=img[i:i+size_img,j:j+size_img]
                new_img=Image.fromarray(new_img)
                new_img.save(os.path.join(save_dir,files[:-5])+'_'+str(n)+'.jpg','JPEG')
            
                  