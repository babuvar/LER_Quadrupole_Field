void test()
{
const Double_t conversion_angle = TMath::Pi() + 0.0415;

TVector3 point_prime(-9.48741, -7.0, 59.7578 );
point_prime.RotateY( conversion_angle );
cout<<"point-prime = "<<point_prime.x()<<"\t"<<point_prime.y()<<"\t"<<point_prime.z()<<endl;

}
