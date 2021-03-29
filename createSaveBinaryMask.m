%basedir = '/home/pm2kb/RL_proj/MoNuSegTestData';
basedir = '/home/pm2kb/RL_proj/MoNuSegTrainingData/Annotations';
files = dir([basedir '/*.xml']);
showFigures = 0;
% note, you might run out of memory and have to load some files manually 
for file = files'
    [pathstr, name, ext] = fileparts(file.name);
    [binary_mask,color_mask] = he_to_binary_mask_final(name,showFigures);
    save(fullfile(basedir,'/masks_true/',strcat(name,'.mat')),'binary_mask')
    clear binary_mask color_mask
end

