# Active Learning for Semantic Segmentation for Nuclei in Medical Imagery 
Semantic segmentation, the process of acquiring pixel-by-pixel data labels, requires large amounts of training data and is time consuming. Particularly in segmenting medical imagery, labeling cells requires an expert medical professional to label every pixel of interest. Many conventional deep learning methods achieve their results on the basis of large amounts of semantically segmented data.  The goals of this project are to prioritize data for labeling which provides the maximum model performance given the training data. In active learning we select “the most informative samples to label so that a learning algorithm will perform better with less data than a non-selective approach” (Casanova et al., 2020). We plan to extend a reinforcement learning technique to select the best regions of whole slide images for labeling in order to train a segmentation model to maximize intersection over union (IoU) for segmenting nuclei cells in hematoxylin and eosin (H&E) stained biopsies. Hematoxylin stains the nucleus of a cell and eosin stains the cytoplasmic components, such as red blood cells and various types of fibers (collagen, elastic, and muscle) (Sampias). Successfully identifying morphological features and types of nuclei present in a pathology sample enables diagnosis and prognosis of numerous conditions, including cancer and muscular dystrophy (Zwerger et al., 2011). 

Specifically, the segmentation of nuclei in cells via active reinforcement learning will be explored via pathology datasets sourced from either existing cardiovascular fluorescent microscopy images utilized by the Owen’s Lab or publicly available histopathology datasets such as the Multi-organ nuclei segmentation (MoNuSeg) image set explored by Kumar et al (2020). 

References
Casanova, A., Pinheiro, P. O., Rostamzadeh, N., & Pal, C. J. (2020). Reinforced active              
             learning for image segmentation. arXiv preprint arXiv:2002.06583.
Zwerger M, Ho CY, Lammerding J. Nuclear mechanics in disease. Annu Rev Biomed Eng.             
             2011;13:397-428. doi:10.1146/annurev-bioeng-071910-124736 
Sampias, Rolls, H&E Staining Overview: A Guide to Best Practices, 
             https://www.leicabiosystems.com/knowledge-pathway/he-staining-overview-a-guide-to-best-
             practics/
N. Kumar et al., "A Multi-Organ Nucleus Segmentation Challenge," in IEEE Transactions on 
             Medical Imaging, vol. 39, no. 5, pp. 1380-1391, May 2020, doi: 10.1109/TMI.2019.2947628.


