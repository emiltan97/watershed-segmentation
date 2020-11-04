close all
clear;
clc;
A = imread('sample.png');
figure
imshow(A)
size(A)

figure
imshow(A(:,:,1))
figure
imshow(A(:,:,2))
figure
imshow(A(:,:,3))

[Gmag, Gdir] = imgradient(A(:,:,3),'prewitt');

max(max(Gmag))
figure
imshow(Gmag/max(max(Gmag)))
figure
imshow(Gdir)
