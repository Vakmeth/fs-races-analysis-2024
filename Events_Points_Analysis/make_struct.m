overall = "FSG24_Overall_Scoring_Results.txt";
accel = "FSG24_Acceleration_Scoring_Results.txt";
skidpad = "FSG24_Skidpad_Scoring_Results.txt";
autox = "FSG24_AutoX_Scoring_Results.txt";
endurance_scoring = "FSG24_Endurance_Scoring_Results.txt";
efficiency = "FSG24_Efficiency_Scoring_Results.txt";
endurance_laps = "FSG24_Endurance_Lap_Times.txt";

FSG24_Results.Overall_Results = readtable(overall, 'Delimiter', '\t', "DecimalSeparator",",", "ReadVariableNames",true);
FSG24_Results.Acceleration = readtable(accel, 'Delimiter', '\t', "DecimalSeparator",",", "ReadVariableNames",true);
FSG24_Results.Skidpad = readtable(skidpad, 'Delimiter', '\t', "DecimalSeparator",",", "ReadVariableNames",true);
FSG24_Results.AutoX = readtable(autox, 'Delimiter', '\t', "DecimalSeparator",",", "ReadVariableNames",true);
FSG24_Results.Endurance = readtable(endurance_scoring, 'Delimiter', '\t', "DecimalSeparator",",", "ReadVariableNames",true);
FSG24_Results.Efficiency = readtable(efficiency, 'Delimiter', '\t', "DecimalSeparator",",", "ReadVariableNames",true);
FSG24_Results.Endurance_Laptimes = readtable(endurance_laps, 'Delimiter', '\t', "DecimalSeparator",",", "ReadVariableNames",true);

save("FSG24_Results.mat", "FSG24_Results")

