#include<iostream>
using namespace std;
#define ll long long 

ll sumOfAp(ll n, ll d){
    return (n * (n + 1) * d) / 2;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    ll number;
    cin >> number;
    number--;
    ll numMultiplesOfThree = (number -  3 ) / 3 + 1;
    ll numMultiplesOfFive = (number -  5) / 5  + 1;
    ll numMultiplesOfFifteen = (number - 15)/ 15 + 1;
    cout << sumOfAp(numMultiplesOfThree, 3) + 
    sumOfAp(numMultiplesOfFive, 5) - 
    sumOfAp(numMultiplesOfFifteen, 15) << endl;
}