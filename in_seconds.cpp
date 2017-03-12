
#include<iostream>
using namespace std;

int main()
{
    int hours, minutes, seconds;
    cout<<"Enter the number of hours, minutes and seconds:\n";
    cin>>hours>>minutes>>seconds;
    cout<<"The duration in seconds is: "<<seconds + hours*3600 + minutes*60;
    return 0;
}
