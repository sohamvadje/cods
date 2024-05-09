#include<iostream>
using namespace std;

void sort(int arr[], int n){
    for(int i = 0; i<n ; i++){
        int min = i;
        for(int j = i; j<n; j++){
            if(arr[j]<arr[min]){
                min = j;
            }
        }
        swap(arr[i], arr[min]);
    }

    cout<<"Sorted array: "<<endl;
    for(int i = 0; i<n; i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}

int main(){
    int n;
    cout<<"Enter total number of elements: ";
    cin>>n;
    int arr[n];
    for(int i = 0; i<n; i++){
        cout<<"Enter an element: ";
        cin>>arr[i];
    }

    sort(arr, n);

    return 0;
}