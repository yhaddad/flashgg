#include <iostream>
#include <TTree.h>

class maman{
public:
  maman(){}
  
protected:
  int bu;
  TTree *fTree;
};

class file: public maman{
public:
  file(){}
  void setBu(int b){this->bu = b;}
  int  getBu(){return this->bu;}
protected:
  int bi;
  
};

