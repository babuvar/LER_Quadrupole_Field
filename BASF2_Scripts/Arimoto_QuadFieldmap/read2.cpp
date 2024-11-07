#include<iostream>
#include<fstream>
#include <iomanip>
#include<cmath>
using namespace std;

int main()
{
double r, phi, z, br, bphi, bz, bx, by;
double max_r=-1.0, max_z=-999.0, min_z=999.0;

ifstream fin; ofstream fout;
fin.open("Varghese3D.dat"); //fout.open("quad.dat");;


while(!fin.eof()){
fin>>r>>phi>>z>>br>>bphi>>bz;

bx = ( br * cos(phi) ) - ( bphi * sin(phi) );
by = ( br * sin(phi) ) + ( bphi * cos(phi) );

//if(phi >=0 && phi <=180){i
//cout<<fixed<<setprecision(9)<<r<<"\t"<<phi<<"\t"<<z<<"\t"<<br<<"\t"<<bphi<<"\t"<<bz<<endl;
cout<<right<<setw(10)<<fixed<<setprecision(4)<<r;
cout<<right<<setw(11)<<fixed<<setprecision(2)<<phi;
cout<<right<<setw(11)<<fixed<<setprecision(4)<<z;
cout<<right<<setw(13)<<fixed<<setprecision(9)<<bx;
cout<<right<<setw(13)<<fixed<<setprecision(9)<<by;
cout<<right<<setw(13)<<fixed<<setprecision(9)<<bz<<'\n';
//}

//Evaluate max/min
if(r > max_r) max_r=r;
if(z > max_z) max_z=z;
if(z < min_z) min_z=z;

}

cout<<"max_r"<< max_r<<endl;
cout<<"max_z"<< max_z<<endl;
cout<<"min_z"<< min_z<<endl;


fin.close(); fout.close();
return 0;
}
