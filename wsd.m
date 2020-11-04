close all
clear;
clc;
A = imread('sample.png');
figure
imshow(A)

A = A(:, :, 3);
figure
imshow(A)

se = strel('disk', 140); 
Ie = imerode(A, se); 
Iobr = imreconstruct(Ie, A); 
figure
imshow(Iobr)

Iobrd = imdilate(Iobr, se);
Iobrcbr = imreconstruct(imcomplement(Iobrd), imcomplement(Iobr)); 
Iobrcbr = imcomplement(Iobrcbr); 
figure
imshow(Iobrcbr)

fgm = imregionalmin(Iobrcbr); 
figure
imshow(fgm)

A2 = labeloverlay(A, fgm); 
figure
imshow(A2)

% se2 = strel(ones(5,5)); 
% fgm2 = imclose(fgm, se2); 
% fgm2 = imerode(fgm2, se2);
% figure
% imshow(fgm2)

% gmag = imgradient(A);
% gmag = gmag / max( max(gmag) );

bw = fgm; 
DL = watershed(bw);
bgm = DL == 0; 
figure
imshow(bw)