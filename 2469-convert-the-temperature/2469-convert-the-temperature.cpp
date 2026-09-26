class Solution {
public:
    vector<double> convertTemperature(double celsius) {
        double kelvin = celsius + 273.15 ; 
        double Fahrenheit = celsius * 1.8 + 32 ; 
        return {kelvin , Fahrenheit} ; 
    }
};