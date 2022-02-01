# OS


#include <iostream>
#include<bits/stdc++.h>
#include <fstream>

using namespace std;

void bestFit(int blockSize[], int m, int processSize[], int n)
{
  cout << "BEST FIT: " << endl; 
    // Stores block id of the block allocated to a
    // process
    int allocation[n];
  
    // Initially no block is assigned to any process
    memset(allocation, -1, sizeof(allocation));
  
    // pick each process and find suitable blocks
    // according to its size ad assign to it
    for (int i=0; i<n; i++)
    {
        // Find the best fit block for current process
        int bestIdx = -1;
        for (int j=0; j<m; j++)
        {
            if (blockSize[j] >= processSize[i])
            {
                if (bestIdx == -1)
                    bestIdx = j;
                else if (blockSize[bestIdx] > blockSize[j])
                    bestIdx = j;
            }
        }
  
        // If we could find a block for current process
        if (bestIdx != -1)
        {
            // allocate block j to p[i] process
            allocation[i] = bestIdx;
  
            // Reduce available memory in this block.
            blockSize[bestIdx] -= processSize[i];
        }
    }
  
    cout << "\nProcess No.\tProcess Size\tBlock no.\n";
    for (int i = 0; i < n; i++)
    {
        cout << "   " << i+1 << "\t\t" << processSize[i] << "\t\t";
        if (allocation[i] != -1)
            cout << allocation[i] + 1;
        else
            cout << "Not Allocated";
        cout << endl;
    }
}

// Function to allocate memory to 
// blocks as per First fit algorithm
void firstFit(int blockSize[], int m, int processSize[], int n)
{
  cout << "FIRST FIT: " << endl; 
    // Stores block id of the 
    // block allocated to a process
    int allocation[n];
  
    // Initially no block is assigned to any process
    memset(allocation, -1, sizeof(allocation));
  
    // pick each process and find suitable blocks
    // according to its size ad assign to it
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (blockSize[j] >= processSize[i])
            {
                // allocate block j to p[i] process
                allocation[i] = j;
  
                // Reduce available memory in this block.
                blockSize[j] -= processSize[i];
  
                break;
            }
        }
    }
  
    cout << "\nProcess No.\tProcess Size\tBlock no.\n";
    for (int i = 0; i < n; i++)
    {
        cout << " " << i+1 << "\t\t" 
             << processSize[i] << "\t\t";
        if (allocation[i] != -1)
            cout << allocation[i] + 1;
        else
            cout << "Not Allocated";
        cout << endl;
    }
}

void user_prompt()
{

  cout << "Pick a choice: " << endl;
  cout << "Select 1 for  Best Fit " << endl;
  cout << "Select 2 for First Fit " << endl;
  cout << "Select 0 Quit Program"    << endl; 
  cout << "Choice: ";
}
void user_selection(int ch) 
{
  if(ch==1)
  {
   bestFit(int blockSize[], int m, int processSize[], int n);
  }
  if(ch==2)
  {
   firstFit(int blockSize[], int m, int processSize[], int n);
  }
  if(ch==0) exit;
  if(ch!= (0||1|| 2))
  {
   cout << "ERROR: Input not in range 0-2 try again" << endl;
   exit;
  } 
  
  
}

void convertStrtoArr(string str)
{
    // get length of string str
    int str_length = str.length();
  
    // create an array with size as string
    // length and initialize with 0
    int arr[str_length] = { 0 };
  
    int j = 0, i, sum = 0;
  
    // Traverse the string
    for (i = 0; str[i] != '\0'; i++) {
  
        // if str[i] is ', ' then split
        if (str[i] == ',')
            continue;
         if (str[i] == ' '){
            // Increment j to point to next
            // array location
            j++;
        }
        else {
  
            // subtract str[i] by 48 to convert it to int
            // Generate number by multiplying 10 and adding
            // (int)(str[i])
            arr[j] = arr[j] * 10 + (str[i] - 48);
        }
    }
  
    cout << "arr[] = ";
    for (i = 0; i <= j; i++) {
        cout << arr[i] << " ";
        sum += arr[i]; // sum of array
    }
  
    // print sum of array
   // cout << "\nSum of array is = " << sum << endl;
}

int main() 
{
  convertStrtoArr(bestFit);
  convertStrtoArr(firstFit);
  int m=4;
  int n=4;
    int choice; 
    ifstream file; 
  
    user_prompt();  
    cin >> choice; 
    user_selection(choice);
    ifstream myfile; 
    myfile.open("processes.txt"); 
  
  string input[1000]; 
  string bitesize[4];
  int q=0; 
  int p=0;
  int blockSize[4];
  int curr_index=0;
  int counter=0;
  string processSize[20]; 
  string inpt_cont;
 int c=0;
  
   for(int i=0; i<4;i++) //load Process Array 
   {
    myfile>>p; 
    blockSize[i]=p;
    //cout << p << endl;
   
   }
 
 
 //cout << p;
if(myfile) //Read the remainder of processes 
    {
   
   // Read an item from the file. 
 //getline(myfile, input);
 //myfile>>input[counter];

 // While the last read operation 
 // was successful, continue. 
 while (myfile) 
 {
 // Display the last item read. 
 //cout << input[counter] << endl; 
 // Read the next item.
 //getline(myfile, input);
 myfile>>input[counter];
 
 
counter++; }
    }

 myfile.close();
 
//cout<<counter <<endl;
for(int k=0; k<counter;k++)
{
cout<< input[k] << endl;
inpt_cont = input[k];
if(inpt_cont.size()<8)
{processSize[c]=input[k]; c=c+1;}
    
}

  
  

   
    
  return 0;
}

