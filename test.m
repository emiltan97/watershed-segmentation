rgb = imread('sample.png');
I = rgb2gray(rgb);
imshow(I)

text(732,501,'Image courtesy of Corel(R)',...
     'FontSize',7,'HorizontalAlignment','right')
gmag = imgradient(I);
figure(2)
imshow(gmag,[])
title('Gradient Magnitude')
L = watershed(gmag);
Lrgb = label2rgb(L);
figure(3)
imshow(Lrgb)
title('Watershed Transform of Gradient Magnitude')
se = strel('disk',20);
Io = imopen(I,se);
figure(4)
imshow(Io)
title('Opening')
Ie = imerode(I,se);
Iobr = imreconstruct(Ie,I);
figure(5)
imshow(Iobr)
title('Opening-by-Reconstruction')
Ioc = imclose(Io,se);
figure(6)
imshow(Ioc)
title('Opening-Closing')
Iobrd = imdilate(Iobr,se);
Iobrcbr = imreconstruct(imcomplement(Iobrd),imcomplement(Iobr));
Iobrcbr = imcomplement(Iobrcbr);
figure(7)
imshow(Iobrcbr)
title('Opening-Closing by Reconstruction')
fgm = imregionalmax(Iobrcbr);
figure(8)
imshow(fgm)
title('Regional Maxima of Opening-Closing by Reconstruction')
I2 = labeloverlay(I,fgm);
figure(9)
imshow(I2)
title('Regional Maxima Superimposed on Original Image')
se2 = strel(ones(5,5));
fgm2 = imclose(fgm,se2);
fgm3 = imerode(fgm2,se2);
fgm4 = bwareaopen(fgm3,20);
I3 = labeloverlay(I,fgm4);
figure(10)
imshow(I3)
title('Modified Regional Maxima Superimposed on Original Image')
bw = imbinarize(Iobrcbr);
figure(11)
imshow(bw)
title('Thresholded Opening-Closing by Reconstruction')

inv = imcomplement(bw);
figure(16)
imshow(inv)
title('Complement')

D = bwdist(inv);
DL = watershed(D);
bgm = DL == 0;
figure(12)
imshow(bgm)
title('Watershed Ridge Lines')
gmag2 = imimposemin(gmag, bgm | fgm4);
L = watershed(gmag2);
labels = imdilate(L==0,ones(3,3)) + 2*bgm + 3*fgm4;
I4 = labeloverlay(I,labels);
figure(13)
imshow(I4)
title('Markers and Object Boundaries Superimposed on Original Image')
Lrgb = label2rgb(L,'jet','w','shuffle');
figure(14)
imshow(Lrgb)
title('Colored Watershed Label Matrix')
figure(15)
imshow(I)
hold on
himage = imshow(Lrgb);
himage.AlphaData = 0.3;
title('Colored Labels Superimposed Transparently on Original Image')

% 
% D2 = bwdist(inv);
% DL2 = watershed(D2);
% bgm2 = DL2 == 0;
% figure(17)
% imshow(bgm2)
% title('Watershed Ridge Lines')
% gmag3 = imimposemin(gmag, bgm2 | fgm4);
% L2 = watershed(gmag3);
% labels = imdilate(L2==0,ones(3,3)) + 2*bgm2 + 3*fgm4;
% I5 = labeloverlay(I,labels);
% figure(18)
% imshow(I5)
% title('Markers and Object Boundaries Superimposed on Original Image')
% Lrgb2 = label2rgb(L2,'jet','w','shuffle');
% figure(19)
% imshow(Lrgb2)
% title('Colored Watershed Label Matrix')
% figure(20)
% imshow(I)
% hold on
% himage2 = imshow(Lrgb2);
% himage2.AlphaData = 0.3;
% title('Colored Labels Superimposed Transparently on Original Image')