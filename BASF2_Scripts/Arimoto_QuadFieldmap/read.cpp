#include<iostream>
#include<fstream>
#include <iomanip>
#include<cmath>
using namespace std;

int main()
{
const double pi2=360.0;
double content[72][6];
double max_r=-1.0, max_z=-999.0, min_z=999.0;

ifstream fin; ofstream fout;
fin.open("Varghese3D.dat"); //fout.open("quad.dat");;

int i=-1;
while(!fin.eof()){
i++;

fin>>content[i][0]>>content[i][1]>>content[i][2]>>content[i][3]>>content[i][4]>>content[i][5];


//if(phi >=0 && phi <=180){i
//cout<<fixed<<setprecision(9)<<r<<"\t"<<phi<<"\t"<<z<<"\t"<<br<<"\t"<<bphi<<"\t"<<bz<<endl;
cout<<right<<setw(10)<<fixed<<setprecision(4)<<content[i][0];
cout<<right<<setw(11)<<fixed<<setprecision(2)<<content[i][1];
cout<<right<<setw(11)<<fixed<<setprecision(4)<<content[i][2];
cout<<right<<setw(13)<<fixed<<setprecision(9)<<content[i][3];
cout<<right<<setw(13)<<fixed<<setprecision(9)<<content[i][4];
cout<<right<<setw(13)<<fixed<<setprecision(9)<<content[i][5]<<'\n';
//}
if(i==71){
i=-1; 
cout<<right<<setw(10)<<fixed<<setprecision(4)<<content[0][0];
cout<<right<<setw(11)<<fixed<<setprecision(2)<<pi2;
cout<<right<<setw(11)<<fixed<<setprecision(4)<<content[0][2];
cout<<right<<setw(13)<<fixed<<setprecision(9)<<content[0][3];
cout<<right<<setw(13)<<fixed<<setprecision(9)<<content[0][4];
cout<<right<<setw(13)<<fixed<<setprecision(9)<<content[0][5]<<'\n';
}


}



fin.close(); fout.close();
return 0;
}
