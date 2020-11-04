close all;
clear;
clc;

img = imread('sample.png'); 
figure;
imshow(img); 

se = strel('disk', 20); 
io = imopen(img, se); 
figure; 
imshow(io);

hist = histeq(io);
figure;
imshow(hist);

hist = hist(:, :, 3); 
figure;
imshow(hist);

mask = hist < 50; 
figure; 
imshow(mask);

maskedImg = labeloverlay(img, mask); 
figure; 
imshow(maskedImg);

% img = img(:, :, 3); 
% figure;
% imshow(img);
% 
% hist = histeq(img);
% figure;
% imshow(hist);
% 
% se = strel('disk', 100); 
% io = imopen(hist, se); 
% ie = imerode(hist, se); 
% iobr = imreconstruct(ie, hist);
% figure;
% imshow(iobr);
% 
% mask = iobr < 80;
% figure;
% imshow(mask);
% 
% maskedImg = labeloverlay(img, mask); 
% figure; 
% imshow(maskedImg);