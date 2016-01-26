from ROOT import *
from os import listdir

def getall(d, basepath="/"):
    "Generator function to recurse into a ROOT file/dir and yield (path, obj) pairs"
    for key in d.GetListOfKeys():
        kname = key.GetName()
#        print kname,key.IsFolder(),d.Get(kname).ClassName()
        if key.IsFolder() and d.Get(kname).ClassName() != "TTree":
            # TODO: -> "yield from" in Py3
            for i in getall(d.Get(kname), basepath+kname+"/"):
                yield i
        else:
            yield basepath+kname, d.Get(kname)

for fn in listdir("/vols/cms04/yhaddad/output_data_validation_with_rmscut"):
    if fn.count(".root"):
        fp = "/vols/cms04/yhaddad/output_data_validation_with_rmscut/%s" % fn
        tf = TFile.Open(fp)
        for k,o in getall(tf):
#            print o.ClassName(), k
            if o.ClassName() == "TTree":
                print fn,o.FindBranch("lumiFactor")
                break
#        tf.cd("vbfTagDumper/trees")
#        tf.ls()
#        print fp
#        tt = tf.Get("vbfTagDumper/trees/dy_toll_m50_13TeV_VBFDiJet")
#        print fn,tt.FindBranch("lumiFactor")

