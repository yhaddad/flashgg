Jet Validation Studies
======================


###Comment on the **PFCHS0**

CHS uses normally the vertex 0 as  a default, this is what we call **PFCHS0**.
* The configuration files to run CHS(PV0)
```
process.pfCHS0fpv1 = cms.EDFilter("CandPtrSelector",
                                  src = cms.InputTag("packedPFCandidates"),
								  cut = cms.string("fromPV>0"))
```




