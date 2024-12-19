//Program to implement Hill Climbing Algorithm.
#include <iostream>
#include <cmath>
using namespace std;
int objective_function(int x) 
{
    return -(x * x) + 10 * x;
}
int hill_climbing(int start) 
{
    int current = start;
    int step = 1;
    int current_value = objective_function(current);
    cout << "Starting hill climbing from x = " << current << " with f(x) = " << current_value << endl;
    while (true) 
    {
        int next_value = objective_function(current + step);
        cout << "Checking right neighbor at x = " << current + step << " with f(x) = " << next_value << endl;
        if (next_value > current_value) 
        {
            current += step;
            current_value = next_value;
            cout << "Moving to x = " << current << " with f(x) = " << current_value << endl;
        } 
        else 
        {
            next_value = objective_function(current - step);
            cout << "Checking left neighbor at x = " << current - step << " with f(x) = " << next_value << endl;
            if (next_value > current_value) 
            {
                current -= step;
                current_value = next_value;
                cout << "Moving to x = " << current << " with f(x) = " << current_value << endl;
            } 
            else 
            {
                cout << "No further improvement, stopping search." << endl;
                break;
            }
        }
    }
    return current;
}
int main()
{
    int start = 0;
    int result = hill_climbing(start);
    cout << "Maximum value found at x = " << result << endl;
    return 0;
}