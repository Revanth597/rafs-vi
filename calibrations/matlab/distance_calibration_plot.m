clc;
clear;
close all;

% ============================================================
% DATA : for example "PERSON"
% ============================================================

ground_truth = [0.5 1.0 1.5 2.0 2.5 3.0]; 

bbox_width  = [212.90 105.75 75.65 59.55 48.00 41.60];
bbox_height = [240 220.10 189.65 157.70 139.75 123.25];

% ============================================================
% GRAPH 1
% Ground Truth Distance vs Bounding Box Width
% ============================================================

figure;

plot(bbox_width, ground_truth, '-o', ...
    'LineWidth',2, ...
    'MarkerSize',8);

grid on;

xlabel('Bounding Box Width (px)');
ylabel('Ground Truth Distance (m)');

title('Ground Truth Distance vs Bounding Box Width');

xlim([0 250]);   % Start x-axis from 0
ylim([0 3.5]);   % Start y-axis from 0

% ============================================================
% GRAPH 2
% Ground Truth Distance vs Bounding Box Height
% ============================================================

figure;

plot(bbox_height, ground_truth, '-s', ...
    'LineWidth',2, ...
    'MarkerSize',8);

grid on;

xlabel('Bounding Box Height (px)');
ylabel('Ground Truth Distance (m)');

title('Ground Truth Distance vs Bounding Box Height');

xlim([0 250]);   % Start x-axis from 0
ylim([0 3.5]);   % Start y-axis from 0