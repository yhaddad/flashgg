#!/usr/bin/python

import ROOT, sys

f =  ROOT.TFile.Open(str(sys.argv[0]))
t = f.Get('vbfTagDumper/trees/vbfh_13TeV_all')
t.Scan('leadPt:leadEt:leadEta:leadPhi')

