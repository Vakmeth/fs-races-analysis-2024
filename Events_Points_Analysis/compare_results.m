close all
clear all
load FSG24_Results.mat;

Results = FSG24_Results; % make it easier to use for structs with other names
clear FSG24_Results

% select number of teams to compare
n_nextbetter = 2;
n_nextworse = 2;
%%
% select reference team
reference_car_nr = 107;
rowIndex = find(Results.Overall_Results.Car == reference_car_nr); % find row index of reference team
% overall list is sorted for end result, display numbers of competitor cars
CarNumbers = Results.Overall_Results.Car(rowIndex-n_nextbetter:rowIndex+n_nextworse)
% display team names
TeamNames = Results.Overall_Results.City_University(rowIndex-n_nextbetter:rowIndex+n_nextworse)

