#include<iostream>
#include<stdlib.h>
using namespace std;

int main()
{
float inhour, inminute, minute, hour, angle;

cout<<"Enter the hour and minute: ";
cin>>inhour>>inminute;
minute=inminute*6;
angle=inhour*30+minute/360*30 - minute;
cout<<"Angle and complement angle are: "<<abs(angle)<<"  "<<abs(360-angle);
return 0;
}
